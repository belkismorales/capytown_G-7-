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

## Responsabilidad del proyecto

Proyecto desarrollado individualmente.
Las actividades de integracion, control, planificacion
y percepcion son realizadas por una sola estudiante.

## Entrega final

Evidencias del simulador disponibles:
- sim_log.txt
- docs/rc1_rqt_graph.jpeg
- csv/metricas_simulador.csv
- csv/resumen_exp3_simulador.csv
- csv/hoja_resultados.csv
- plots/

Pendientes: pruebas fisicas, completar informe.pdf
y crear el tag v1.0-rc1.

Las ganancias del simulador deben validarse
antes de aplicarlas al robot fisico.


## Resultados destacados del simulador

- Recta 1D (PID): error final de 0.24 cm y asentamiento de 5.833 s.
- Giro 2F: sobreimpulso de 0%, asentamiento de 1.214 s
  y error final de 0.395 grados.
- Cuadrado 3C con ruido bajo: cierre promedio de 22.03 cm
  medido mediante /sim/pose.

El topico /sim/pose representa la referencia del simulador,
no una medicion del robot fisico.

## Guia para el laboratorio

Consultar docs/guia_laboratorio_rc1.md antes de las
pruebas con el robot fisico.
