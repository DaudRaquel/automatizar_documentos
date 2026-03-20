"""Testes para o classificador de motoristas por tempo de empresa."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from datetime import date, timedelta
import pytest
from utils.classificador import calcular_anos_empresa, separar_por_tempo


def test_calcular_anos_empresa_string():
    data = (date.today() - timedelta(days=365 * 3)).strftime("%Y-%m-%d")
    anos = calcular_anos_empresa(data)
    assert 2.9 <= anos <= 3.1

def test_calcular_anos_empresa_objeto_date():
    data = date.today() - timedelta(days=365 * 7)
    anos = calcular_anos_empresa(data)
    assert 6.9 <= anos <= 7.1

def test_separar_acima_5_anos():
    motoristas = [
        {"CODPESSOA": 1, "NOME": "João", "DATAADMISSAO":
         (date.today() - timedelta(days=365*6)).strftime("%Y-%m-%d"),
         "CARGO": "MOTORISTA", "SETOR": "LOG"},
    ]
    acima, abaixo = separar_por_tempo(motoristas)
    assert len(acima) == 1
    assert len(abaixo) == 0

def test_separar_abaixo_5_anos():
    motoristas = [
        {"CODPESSOA": 2, "NOME": "Maria", "DATAADMISSAO":
         (date.today() - timedelta(days=365*2)).strftime("%Y-%m-%d"),
         "CARGO": "MOTORISTA", "SETOR": "LOG"},
    ]
    acima, abaixo = separar_por_tempo(motoristas)
    assert len(acima) == 0
    assert len(abaixo) == 1

def test_separar_adiciona_anos_empresa():
    motoristas = [
        {"CODPESSOA": 3, "NOME": "Pedro", "DATAADMISSAO":
         (date.today() - timedelta(days=365*4)).strftime("%Y-%m-%d"),
         "CARGO": "MOTORISTA", "SETOR": "LOG"},
    ]
    acima, abaixo = separar_por_tempo(motoristas)
    todos = acima + abaixo
    assert "ANOS_EMPRESA" in todos[0]
    assert isinstance(todos[0]["ANOS_EMPRESA"], float)

def test_lista_vazia():
    acima, abaixo = separar_por_tempo([])
    assert acima == [] and abaixo == []
