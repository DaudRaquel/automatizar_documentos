"""Testes para os dados mock."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from database.mock_data import MOTORISTAS_MOCK

def test_mock_tem_campos_obrigatorios():
    campos = {"CODPESSOA", "NOME", "DATAADMISSAO", "CARGO", "SETOR"}
    for m in MOTORISTAS_MOCK:
        assert campos.issubset(m.keys()), f"Campos faltando em: {m}"

def test_mock_nao_vazio():
    assert len(MOTORISTAS_MOCK) > 0

def test_mock_codpessoa_unico():
    ids = [m["CODPESSOA"] for m in MOTORISTAS_MOCK]
    assert len(ids) == len(set(ids)), "CODPESSOA duplicado no mock"
