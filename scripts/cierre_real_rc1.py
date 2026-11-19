#!/usr/bin/env python3
"""RC-1: registra /odom y /sim/pose (simulador), calcula cierre y grafica.
Uso: python3 cierre_real_rc1.py --csv ... --png ... --lado 2.0
Iniciar ANTES que cuadrado_controller.py; detener con Ctrl+C DESPUÉS de FIN.
No altera ni publica comandos al robot. Requiere ROS 2 Humble, numpy, matplotlib.
"""
import argparse
import csv
import math
from pathlib import Path

import rclpy
from rclpy.node import Node
from nav_msgs.msg import Odometry
from geometry_msgs.msg import PoseStamped


def yaw_from_quat(q):
    return math.atan2(2 * (q.w*q.z + q.x*q.y), 1 - 2 * (q.y*q.y + q.z*q.z))


def normalize_angle(a):
    return math.atan2(math.sin(a), math.cos(a))


class Recorder(Node):
    def __init__(self):
        super().__init__('rc1_cierre_real_recorder')
        self.records = {'odom': [], 'real': []}
        self.create_subscription(Odometry, '/odom', self.on_odom, 20)
        self.create_subscription(PoseStamped, '/sim/pose', self.on_real, 20)
        self.get_logger().info('Grabando /odom y /sim/pose. Inicia el controlador en otra terminal; al terminar presiona Ctrl+C aqui.')

    def add(self, topic, pose):
        t = self.get_clock().now().nanoseconds / 1e9
        self.records[topic].append((t, float(pose.position.x), float(pose.position.y), yaw_from_quat(pose.orientation)))

    def on_odom(self, msg):
        self.add('odom', msg.pose.pose)

    def on_real(self, msg):
        self.add('real', msg.pose)


def relative_trace(samples):
    """Coordinates relative to each topic's own start; rotate axes by initial heading."""
    t0, x0, y0, yaw0 = samples[0]
    c, s = math.cos(yaw0), math.sin(yaw0)
    out = []
    unwrapped = yaw0
    last = yaw0
    for t, x, y, yaw in samples:
        dx, dy = x - x0, y - y0
        unwrapped += normalize_angle(yaw - last)
        last = yaw
        out.append((t-t0, c*dx+s*dy, -s*dx+c*dy, math.degrees(unwrapped-yaw0)))
    return out


def metrics(trace):
    end = trace[-1]
    return (100*math.hypot(end[1], end[2]), end[3], trace[-1][0])


def main():
    parser = argparse.ArgumentParser(description='RC-1: cierre odometria vs pose real simulada')
    parser.add_argument('--csv', required=True, help='CSV de salida con ambas trayectorias')
    parser.add_argument('--png', required=True, help='PNG de salida')
    parser.add_argument('--lado', type=float, default=2.0)
    args = parser.parse_args()
    rclpy.init()
    node = Recorder()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        print('\nGrabacion detenida por el usuario.')
    except RuntimeError as e:
        print(f'\nADVERTENCIA: error de ROS 2: {e}')
        print('Se intentaran guardar las muestras recibidas.')
    finally:
        records = node.records
        try:
            node.destroy_node()
        except Exception as e:
            print(f'Advertencia al destruir el nodo: {e}')
        if rclpy.ok():
            try:
                rclpy.shutdown()
            except Exception as e:
                print(f'Advertencia al cerrar ROS 2: {e}')

    if not records['odom'] or not records['real']:
        print('ERROR: no se recibieron ambos topicos. No se calcularon resultados.')
        return 1
    rel = {key: relative_trace(val) for key, val in records.items()}
    csv_path = Path(args.csv).expanduser()
    png_path = Path(args.png).expanduser()
    csv_path.parent.mkdir(parents=True, exist_ok=True)
    png_path.parent.mkdir(parents=True, exist_ok=True)
    with csv_path.open('w', newline='') as f:
        wr = csv.writer(f)
        wr.writerow(['topic', 't_rel_s', 'x_rel_m', 'y_rel_m', 'yaw_acum_deg'])
        for key in ('odom', 'real'):
            for row in rel[key]:
                wr.writerow([key] + [f'{v:.6f}' for v in row])
    odom_metrics = metrics(rel['odom'])
    real_metrics = metrics(rel['real'])
    print(f'Muestras: /odom={len(rel["odom"])}, /sim/pose={len(rel["real"])}')
    print('Cierre segun /odom: {:.2f} cm, yaw acumulado: {:.2f} deg'.format(*odom_metrics[:2]))
    print('Cierre REAL simulado: {:.2f} cm, yaw acumulado: {:.2f} deg'.format(*real_metrics[:2]))
    # The difference between the final displacement VECTORS is not the difference of their norms.
    ex = rel['real'][-1][1] - rel['odom'][-1][1]
    ey = rel['real'][-1][2] - rel['odom'][-1][2]
    print('Diferencia vectorial del desplazamiento final: {:.2f} cm'.format(100*math.hypot(ex,ey)))
    print('ATENCION: los cierres son validos solo si la grabacion empieza ANTES del movimiento y termina DESPUES de detener el robot.')
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    fig, ax = plt.subplots(figsize=(7, 7))
    for key,label in [('odom','/odom (estimada)'),('real','/sim/pose (real simulada)')]:
        x = [a[1] for a in rel[key]]
        y = [a[2] for a in rel[key]]
        ax.plot(x,y,linewidth=1.5,label=label)
        ax.scatter([x[0]],[y[0]],marker='o',s=30)
        ax.scatter([x[-1]],[y[-1]],marker='x',s=60)
    if args.lado > 0:
        l = args.lado
        ax.plot([0,l,l,0,0],[0,0,l,l,0],linestyle='--',color='gray',label=f'Cuadrado ideal {l:g} m (orientativo)')
    ax.axis('equal')
    ax.grid(True,alpha=.3)
    ax.set_xlabel('Desplazamiento X desde el inicio (m)')
    ax.set_ylabel('Desplazamiento Y desde el inicio (m)')
    ax.set_title('RC-1: trayectoria estimada y real simulada')
    ax.legend(loc='best')
    fig.tight_layout()
    fig.savefig(png_path,dpi=160)
    plt.close(fig)
    print('CSV:',csv_path)
    print('PNG:',png_path)
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
