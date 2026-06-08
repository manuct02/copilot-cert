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

    if díWEHGy4whgweEDCHGes_anterior.day

    if meses < 0:
        años -= 1
        meses += 12

    return años, meses, días

