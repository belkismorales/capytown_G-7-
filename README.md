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

## ROS_DOMAIN_ID

En la verificacion final de Ubuntu, la variable
ROS_DOMAIN_ID no estaba definida. ROS 2 utiliza
normalmente el dominio 0 en ese caso.

El dominio utilizado durante cada ejecucion historica
del simulador no fue registrado explicitamente.

Para verificar el dominio actual:

    echo "${ROS_DOMAIN_ID:-0}"

Antes de conectar el robot fisico, comprobar que
la computadora y el robot utilicen el mismo dominio.
No cambiar ROS_DOMAIN_ID sin verificar primero
la configuracion del laboratorio.

## Condiciones del simulador

### Experimento 1: recta de 2 m

- Desplazamiento lateral inicial: line_offset = 0.10 m.
- Sesgo angular inyectado: bias_w = 0.06 rad/s.
- Nivel de ruido: low.
- Controladores comparados: Bang-bang, P, PD y PID.

### Experimento 2: giro de 90 grados

- Nivel de ruido: low.
- Se compararon seis configuraciones de control angular.
- Las metricas incluyen sobreimpulso, tiempo de
  asentamiento y error angular final.

### Experimento 3: cuadrado de 2 x 2 m

- Controladores: 3A abierto, 3B PID y 3C PID+Ki.
- Tres corridas por controlador con ruido low.
- Pruebas adicionales con ruido medium.
- bias_w documentado: 0.03 rad/s para 3B
  y 0.05 rad/s para 3C.
- Los niveles low y medium identifican las
  configuraciones de ruido utilizadas.
- No se atribuye la diferencia entre 3B y 3C
  exclusivamente a Ki porque tambien cambia bias_w.

### Interpretacion de los datos

- /odom: estimacion de posicion por odometria.
- /sim/pose: posicion de referencia del simulador.
- Los CSV que incluyen "real" en su nombre pueden
  referirse a /sim/pose; NO son mediciones fisicas.
- El cierre fisico del robot se medira con cinta metrica.
- Los valores numericos internos de ruido low y medium
  no quedaron documentados en estas evidencias.
