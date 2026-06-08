from datetime import datetime, timedelta, date


def tiempo_transcurrido(fecha_str, fecha_actual=None):
    fecha_inicio = datetime.strptime(fecha_str, "%d/%m/%Y").date()

    if fecha_actual is None:
        fecha_actual = date.today()
    elif isinstance(fecha_actual, datetime):
        fecha_actual = fecha_actual.date()

    if fecha_actual < fecha_inicio:
        raise ValueError("La fecha debe ser anterior o igual a hoy")

    años = fecha_actual.year - fecha_inicio.year
    meses = fecha_actual.month - fecha_inicio.month
    días = fecha_actual.day - fecha_inicio.day

    if días < 0:
        meses -= 1
        primer_dia_mes_actual = date(fecha_actual.year, fecha_actual.month, 1)
        ultimo_dia_mes_anterior = primer_dia_mes_actual - timedelta(days=1)
        días += ultimo_dia_mes_anterior.day

    if meses < 0:
        años -= 1
        meses += 12

    return años, meses, días