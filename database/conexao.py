"""
Módulo de conexão com banco Oracle (TOTVS RM).
Usa variáveis de ambiente - nunca coloque credenciais no código.
"""
import os
import cx_Oracle
from dotenv import load_dotenv

load_dotenv()


def get_connection():
    """Retorna conexão com o Oracle via variáveis de ambiente."""
    dsn = cx_Oracle.makedsn(
        host=os.getenv("ORACLE_HOST"),
        port=int(os.getenv("ORACLE_PORT", 1521)),
        service_name=os.getenv("ORACLE_SERVICE"),
    )
    return cx_Oracle.connect(
        user=os.getenv("ORACLE_USER"),
        password=os.getenv("ORACLE_PASSWORD"),
        dsn=dsn,
    )


def buscar_motoristas() -> list[dict]:
    """Busca motoristas ativos no TOTVS RM."""
    query = """
        SELECT F.CODPESSOA, P.NOME, F.DATAADMISSAO,
               C.DESCRICAO AS CARGO, S.NOMEDEPARTAMENTO AS SETOR
        FROM PRFUNCIONARIO F
        JOIN PPESSOA P ON P.CODPESSOA = F.CODPESSOA
        JOIN PFUNCAO C ON C.CODFUNCAO = F.CODFUNCAO
        JOIN PDEPTO  S ON S.CODDEPTO  = F.CODDEPTO
        WHERE C.DESCRICAO LIKE '%MOTORISTA%'
          AND F.CODSITUACAO = 'A'
        ORDER BY P.NOME
    """
    conn = get_connection()
    try:
        cur = conn.cursor()
        cur.execute(query)
        cols = [c[0] for c in cur.description]
        return [dict(zip(cols, row)) for row in cur.fetchall()]
    finally:
        conn.close()
