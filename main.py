"""
automatizar_documentos — Script principal.

Fluxo:
  1. Busca motoristas no TOTVS RM (Oracle).
  2. Classifica por tempo de empresa (+5 / -5 anos).
  3. Gera PDFs organizados por categoria.

Uso:
    python main.py           # produção (Oracle real)
    python main.py --mock    # testes (dados fictícios)
"""
import argparse
from database.conexao import buscar_motoristas
from database.mock_data import MOTORISTAS_MOCK
from utils.classificador import separar_por_tempo
from pdf.gerador_pdf import gerar_todos_pdfs


def main(mock: bool = False):
    print("=" * 50)
    print("  GERADOR DE DOCUMENTOS — MOTORISTAS")
    print("=" * 50)

    print("\n[1/3] Buscando motoristas...")
    motoristas = MOTORISTAS_MOCK if mock else buscar_motoristas()
    print(f"      {len(motoristas)} motorista(s) encontrado(s).")

    print("\n[2/3] Classificando por tempo de empresa...")
    acima, abaixo = separar_por_tempo(motoristas)
    print(f"      +5 anos : {len(acima)} | -5 anos : {len(abaixo)}")

    print("\n[3/3] Gerando PDFs...")
    resultado = gerar_todos_pdfs(acima, abaixo)

    total = sum(len(v) for v in resultado.values())
    print(f"\n✅  {total} PDF(s) em ./pdfs_gerados/")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--mock", action="store_true")
    main(mock=ap.parse_args().mock)
