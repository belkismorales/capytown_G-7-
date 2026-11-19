# RC-1 — Guía de pruebas con robot físico

## Antes de comenzar

- [ ] Confirmar que la Raspberry Pi 5 y el robot estén encendidos.
- [ ] Confirmar que ROS 2 Humble esté configurado.
- [ ] Verificar que se publique `/odom`.
- [ ] Verificar el funcionamiento de la estimación EKF.
- [ ] Comprobar que `/cmd_vel` detenga el robot cuando no recibe comandos durante 0.5 s.
- [ ] Delimitar un cuadrado de 2 x 2 m con 15 cm de espacio libre adicional.
- [ ] Tener cinta métrica, transportador y computadora para registrar datos.

## Prueba 1 — Giro suave de 90 grados

- [ ] Ejecutar un giro suave.
- [ ] Medir el ángulo real con transportador.
- [ ] Registrar el error angular.
- [ ] Comparar con el objetivo de error <= 3 grados.

## Prueba 2 — Recta con PID 1D

- [ ] Ejecutar tres recorridos.
- [ ] Medir desviación lateral con cinta métrica.
- [ ] Registrar las tres mediciones.
- [ ] Comparar con el objetivo de desviación <= 5 cm.

## Prueba 3 — Cuadrado de 2 x 2 m

- [ ] Ejecutar 3A (lazo abierto) una vez.
- [ ] Ejecutar 3B (PID) tres veces.
- [ ] Medir el error de cierre real con cinta métrica.
- [ ] Registrar el giro acumulado.
- [ ] Comparar los resultados de 3A y 3B.
- [ ] Verificar si el cierre promedio de 3B es <= 25 cm.
- [ ] Registrar hasta tres reajustes, cambiando solo un parámetro por vez.

## Evidencias ROS 2

Verificar los tópicos antes de grabar:

    ros2 topic list
    ros2 topic hz /odom

Grabar una bolsa por prueba, usando un nombre diferente:

    ros2 bag record -o bags/NOMBRE_PRUEBA /odom /cmd_vel /tf

Detener la grabación con Ctrl+C.

IMPORTANTE: Ejecutar estos comandos en el entorno ROS 2
correctamente configurado y desde la raíz del repositorio.
Si los tópicos tienen otros nombres, verificarlos primero.

## Registro de resultados físicos

Para cada ejecución anotar:

- Identificador de prueba.
- Fecha y hora.
- Parámetros PID utilizados.
- Distancia o ángulo medido físicamente.
- Resultado estimado por odometría.
- Error de cierre medido con cinta.
- Observaciones, colisiones o interrupciones.
- Nombre del archivo ROS bag.

No sustituir mediciones físicas por `/sim/pose`:
ese tópico representa la verdad de referencia del simulador.

## Al terminar

- [ ] Copiar los ROS bags a `bags/`.
- [ ] Guardar los CSV y gráficos físicos.
- [ ] Completar el bloque `robot_fisico` en `config/rc1_pid.yaml`.
- [ ] Completar la hoja de resultados.
- [ ] Finalizar `informe.pdf`.
- [ ] Actualizar README.md.
- [ ] Subir los cambios a GitHub.
- [ ] Crear el tag `v1.0-rc1` solo cuando todo esté completo.
