# 🚛 Automatizar Documentos — Integração TOTVS RM

Automação completa para geração de documentos de assinatura de motoristas, com dados extraídos diretamente do **TOTVS RM (Oracle)**. O processo que antes levava horas passou a ser executado em minutos.

## ✨ Funcionalidades

- Conexão segura ao Oracle via variáveis de ambiente
- Extração de dados de motoristas ativos via SQL no TOTVS RM
- Separação automática por tempo de empresa: **+5 anos** e **-5 anos**
- Geração de PDFs formatados e prontos para assinatura
- Organização automática em pastas por categoria
- Modo `--mock` para testes sem banco de dados

## 🛠️ Stack

| Camada | Tecnologia |
|--------|-----------|
| Linguagem | Python 3.10+ |
| Banco de dados | Oracle (TOTVS RM via cx_Oracle) |
| Manipulação de dados | Pandas |
| Geração de PDF | ReportLab |
| Automação web | Selenium |

## 📁 Estrutura

```
automatizar_documentos/
├── main.py                  # Ponto de entrada
├── database/
│   ├── conexao.py           # Conexão Oracle + queries SQL
│   └── mock_data.py         # Dados fictícios para testes
├── utils/
│   └── classificador.py     # Lógica de classificação por tempo
├── pdf/
│   └── gerador_pdf.py       # Geração e organização de PDFs
├── .env.example             # Modelo de variáveis de ambiente
└── requirements.txt
```

## 🚀 Como rodar

```bash
# 1. Clone e instale dependências
pip install -r requirements.txt

# 2. Configure credenciais
cp .env.example .env
# edite .env com seus dados

# 3. Execute
python main.py           # Produção (Oracle real)
python main.py --mock    # Teste (dados fictícios)
```

## 📊 Impacto

- ✅ Redução de **horas para minutos** no processo
- ✅ Eliminação de erros manuais
- ✅ PDFs organizados automaticamente por categoria
- ✅ Processo replicável para outros tipos de colaboradores

---
Desenvolvido por **Raquel Daud** — [LinkedIn](https://www.linkedin.com/in/raquel-daud-72a3991a2/)
