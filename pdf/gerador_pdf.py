"""Geração de PDFs para assinatura dos motoristas com ReportLab."""
from datetime import date
from pathlib import Path
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib import colors

OUTPUT_DIR = Path("pdfs_gerados")


def gerar_pdf_motorista(motorista: dict, categoria: str) -> str:
    pasta = OUTPUT_DIR / categoria
    pasta.mkdir(parents=True, exist_ok=True)
    nome_arq = f"{motorista['CODPESSOA']}_{motorista['NOME'].replace(' ', '_')}.pdf"
    caminho = str(pasta / nome_arq)

    doc = SimpleDocTemplate(caminho, pagesize=A4,
                            rightMargin=2*cm, leftMargin=2*cm,
                            topMargin=2*cm, bottomMargin=2*cm)
    styles = getSampleStyleSheet()
    titulo = ParagraphStyle("T", parent=styles["Heading1"], fontSize=14, alignment=1)
    corpo  = ParagraphStyle("C", parent=styles["Normal"], fontSize=11, leading=16)

    elementos = [
        Paragraph("DECLARAÇÃO DE RECEBIMENTO DE DOCUMENTOS", titulo),
        Spacer(1, .5*cm),
        Paragraph(
            f"Eu, <b>{motorista['NOME']}</b>, cód. <b>{motorista['CODPESSOA']}</b>, "
            f"admitido em <b>{motorista['DATAADMISSAO']}</b>, setor <b>{motorista['SETOR']}</b>, "
            f"declaro ter recebido os documentos abaixo em {date.today().strftime('%d/%m/%Y')}.",
            corpo
        ),
        Spacer(1, .8*cm),
    ]

    tabela = Table(
        [["Documento", "Recebido"],
         ["Manual do Colaborador", "( )"],
         ["Política de Uso de Veículos", "( )"],
         ["Termo de Responsabilidade", "( )"]],
        colWidths=[13*cm, 3*cm]
    )
    tabela.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,0), colors.grey),
        ("TEXTCOLOR", (0,0), (-1,0), colors.white),
        ("FONTNAME", (0,0), (-1,0), "Helvetica-Bold"),
        ("GRID", (0,0), (-1,-1), .5, colors.black),
        ("ALIGN", (0,0), (-1,-1), "CENTER"),
    ]))

    elementos += [tabela, Spacer(1, 1.5*cm),
                  Paragraph("_" * 60, corpo),
                  Paragraph(f"Assinatura: {motorista['NOME']}", corpo),
                  Spacer(1, .3*cm),
                  Paragraph("Data: ____/____/________", corpo)]

    doc.build(elementos)
    return caminho


def gerar_todos_pdfs(acima_5, abaixo_5) -> dict:
    gerados = {"acima_5_anos": [], "abaixo_5_anos": []}
    for m in acima_5:
        p = gerar_pdf_motorista(m, "acima_5_anos")
        gerados["acima_5_anos"].append(p)
        print(f"  [✓] {p}")
    for m in abaixo_5:
        p = gerar_pdf_motorista(m, "abaixo_5_anos")
        gerados["abaixo_5_anos"].append(p)
        print(f"  [✓] {p}")
    return gerados
