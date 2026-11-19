from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Table, TableStyle,
    Spacer, KeepTogether
)
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm

archivo = "informe.pdf"

doc = SimpleDocTemplate(
    archivo,
    pagesize=A4,
    rightMargin=1.5*cm,
    leftMargin=1.5*cm,
    topMargin=1.2*cm,
    bottomMargin=1.2*cm
)

estilos = getSampleStyleSheet()
estilos.add(ParagraphStyle(
    name="TituloRC1",
    parent=estilos["Heading1"],
    fontSize=13,
    leading=15,
    alignment=TA_CENTER,
    spaceAfter=8
))
estilos.add(ParagraphStyle(
    name="SeccionRC1",
    parent=estilos["Heading2"],
    fontSize=9,
    leading=11,
    spaceBefore=7,
    spaceAfter=3
))
estilos.add(ParagraphStyle(
    name="TextoRC1",
    parent=estilos["Normal"],
    fontSize=8,
    leading=10,
    spaceAfter=4
))

historia = []

def titulo(texto):
    historia.append(Paragraph(texto, estilos["TituloRC1"]))

def seccion(texto):
    historia.append(Paragraph(texto, estilos["SeccionRC1"]))

def texto(contenido):
    historia.append(Paragraph(contenido, estilos["TextoRC1"]))

def tabla(filas, anchos):
    t = Table(filas, colWidths=anchos, repeatRows=1)
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#DDE7F0")),
        ("GRID", (0, 0), (-1, -1), 0.35, colors.grey),
        ("FONTSIZE", (0, 0), (-1, -1), 7),
        ("LEADING", (0, 0), (-1, -1), 9),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("LEFTPADDING", (0, 0), (-1, -1), 5),
        ("RIGHTPADDING", (0, 0), (-1, -1), 5),
        ("TOPPADDING", (0, 0), (-1, -1), 3),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
    ]))
    historia.append(t)

titulo("RC-1 | Control PID: del simulador al robot real")
texto(
    "<b>Grupo:</b> 7 | <b>Modalidad:</b> desarrollo individual | "
    "<b>Curso:</b> Robotica - ESAN 2026-2 | "
    "<b>Entorno:</b> ROS 2 Humble / CapyTown"
)

seccion("1. Experimento 1: seguimiento de recta")
tabla([
    ["Controlador", "Error final", "Asentamiento (+/-2 cm)"],
    ["1A - Bang-bang", "0.59 cm", "10.352 s"],
    ["1B - P", "0.74 cm", "10.281 s"],
    ["1C - PD", "2.12 cm", "No alcanzado"],
    ["1D - PID", "0.24 cm", "5.833 s"],
], [5*cm, 4*cm, 8*cm])
texto(
    "El PID 1D obtuvo un error lateral medio de 2.51 cm "
    "y un error final de 0.24 cm, cumpliendo el limite "
    "de 2 cm de error final."
)

seccion("2. Experimento 2: giro de 90 grados")
tabla([
    ["Prueba", "Sobreimpulso", "Asentamiento (+/-2 grados)", "Error final"],
    ["2A", "0.000 %", "3.853 s", "1.501 grados"],
    ["2B", "5.488 %", "1.276 s", "0.006 grados"],
    ["2C", "0.000 %", "1.877 s", "0.412 grados"],
    ["2D", "7.672 %", "1.567 s", "0.011 grados"],
    ["2E", "0.000 %", "1.242 s", "0.515 grados"],
    ["2F", "0.000 %", "1.214 s", "0.395 grados"],
], [2*cm, 3.5*cm, 7.5*cm, 4*cm])
texto(
    "Las configuraciones propias 2D, 2E y 2F cumplen "
    "sobreimpulso <= 10 % y asentamiento <= 3 s. "
    "La configuracion 2F fue la mas rapida entre ellas."
)

seccion("3. Experimento 3: cuadrado de 2 x 2 m")
tabla([
    ["Controlador", "Cierre medio, ruido bajo", "Cierre registrado, ruido medio"],
    ["3A - Abierto", "23.27 cm (3 corridas)", "71.27 cm"],
    ["3B - PID", "45.63 cm (3 corridas)", "118.72 cm (corrida 3)"],
    ["3C - PID + Ki", "22.03 cm (3 corridas)", "41.76 cm"],
], [4.5*cm, 6.3*cm, 6.2*cm])
texto(
    "Los cierres anteriores se calcularon con /sim/pose "
    "(referencia del simulador). La odometria puede indicar "
    "cierres menores que la referencia; por ello se deben "
    "comparar ambas fuentes. Las condiciones iniciales "
    "no fueron identicas en todas las corridas. En ruido "
    "medio hubo registros incompletos y una colision, "
    "excluidos de los cierres completados."
)

seccion("4. Interpretacion y transferencia al robot fisico")
texto(
    "El ajuste PID mejoro el seguimiento de recta y permitio "
    "giros con sobreimpulso controlado. En el cuadrado, "
    "el cierre estimado por odometria no siempre representa "
    "el desplazamiento real. En el robot fisico se deberan "
    "validar ganancias, medir el cierre con cinta metrica "
    "y registrar /odom, /cmd_vel y /tf."
)

seccion("5. Pendientes de validacion fisica")
texto(
    "Giro real de 90 grados; tres rectas con PID 1D; "
    "un cuadrado 3A y tres cuadrados 3B; comparacion "
    "odom/cinta; hasta tres reajustes de un parametro "
    "por vez. Objetivo: cierre promedio 3B <= 25 cm "
    "y menor que 3A. Las mediciones fisicas aun "
    "no estan disponibles."
)

seccion("6. Evidencias y proximos cambios")
texto(
    "Datos: csv/hoja_resultados.csv, csv/metricas_simulador.csv "
    "y csv/resumen_exp3_simulador.csv. Graficas: plots/. "
    "Topicos y grafo: sim_log.txt y docs/rc1_rqt_graph.jpeg. "
    "Para RC-2: revisar diferencias odometria/referencia, "
    "validar estimacion y reajustar ganancias con mediciones fisicas. "
    "Predicciones previas: no documentadas; no se reconstruyen."
)

doc.build(historia)
print("Informe creado:", archivo)
