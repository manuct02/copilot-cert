from datetime import date

from gh_300 import tiempo_transcurrido


def test_tiempo_transcurrido_same_day():
    assert tiempo_transcurrido("01/03/2024", date(2024, 3, 1)) == (0, 0, 0)


def test_tiempo_transcurrido_future_date_raises():
    try:
        tiempo_transcurrido("02/03/2024", date(2024, 3, 1))
    except ValueError as exc:
        assert "anterior o igual a hoy" in str(exc)
    else:
        raise AssertionError("Expected ValueError for future date")


def test_tiempo_transcurrido_month_borrow():
    assert tiempo_transcurrido("20/01/2024", date(2024, 3, 1)) == (0, 1, 10)


def test_tiempo_transcurrido_year_month_difference():
    assert tiempo_transcurrido("05/02/2023", date(2025, 5, 10)) == (2, 3, 5)