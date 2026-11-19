# RC-1 - Control PID: del simulador al robot real

**Grupo:** 7
**Curso:** Robotica - ESAN 2026-2
**Entorno:** ROS 2 Humble y CapyTown

## Estado del proyecto

Las pruebas en el simulador estan realizadas.
Las pruebas con el robot fisico estan pendientes para el laboratorio.

## Experimentos del simulador

- Experimento 1: Recta con Bang-bang, P, PD y PID.
- Experimento 2: Giro de 90 grados con seis configuraciones.
- Experimento 3: Cuadrado de 2 x 2 m con lazo abierto, PID y PID+Ki.

El controlador 1D obtuvo un error lateral medio de 2.51 cm
y un error final de 0.24 cm.

## Contenido

- config/: ganancias PID documentadas.
- csv/: datos y hoja_resultados.csv.
- plots/: graficas de las pruebas.
- scripts/: programas Python utilizados.
- bags/: registros del robot fisico pendientes.
- docs/: documentacion complementaria.

## Entorno

ROS 2 Humble, Ubuntu y simulador CapyTown.

Para preparar ROS 2:

    source /opt/ros/humble/setup.bash
    source ~/capytown_ws/install/setup.bash

## Pruebas fisicas pendientes

- Verificar odometria y EKF.
- Medir giro de 90 grados con transportador.
- Ejecutar recta 1D tres veces.
- Ejecutar cuadrado 3A una vez.
- Ejecutar cuadrado 3B tres veces.
- Guardar bags de /odom, /cmd_vel y /tf.
- Medir errores reales con cinta metrica.
- Completar hoja de resultados e informe.pdf.

## Integrantes y roles

- Integracion: pendiente
- Control: pendiente
- Planificacion: pendiente
- Percepcion: pendiente

## Entrega final

Pendientes: sim_log.txt, captura de rqt_graph,
informe.pdf, pruebas fisicas y tag v1.0-rc1.

Las ganancias del simulador deben validarse
antes de aplicarlas al robot fisico.
