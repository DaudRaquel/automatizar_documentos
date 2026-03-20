"""Classificação de motoristas por tempo de empresa."""
from datetime import date, datetime


def calcular_anos_empresa(data_admissao) -> float:
    if isinstance(data_admissao, str):
        data_admissao = datetime.strptime(data_admissao, "%Y-%m-%d").date()
    return (date.today() - data_admissao).days / 365.25


def separar_por_tempo(motoristas: list[dict]) -> tuple[list, list]:
    """Retorna (acima_5_anos, abaixo_5_anos)."""
    acima, abaixo = [], []
    for m in motoristas:
        anos = calcular_anos_empresa(m["DATAADMISSAO"])
        m["ANOS_EMPRESA"] = round(anos, 1)
        (acima if anos >= 5 else abaixo).append(m)
    return acima, abaixo
