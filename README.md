# 📊 Análise de Dados da Netflix com Streamlit

Este repositório contém um projeto de análise exploratória de dados utilizando Python, com foco no catálogo da plataforma Netflix. Além da análise, foi desenvolvido um **dashboard interativo** com a biblioteca **Streamlit**, que permite explorar os dados de forma visual e dinâmica.

---

## ✅ Funcionalidades

- Limpeza e preparação dos dados
- Análise estatística e visualizações com Pandas, Matplotlib e Plotly
- Dashboard interativo com filtros por:
  - Tipo de conteúdo (Filme/Série)
  - Intervalo de anos
  - País de produção
- Gráficos interativos (linha, pizza, barras)
- Tabela dinâmica de dados filtrados

---

## 📁 Estrutura do Projeto

```
📆 netflix-dashboard/
 ├️ 📊 netflix_titles.csv        # Dataset principal
 ├️ 📄 netflix-analise-pt1.py    # Versão com matplotlib e exploração básica            
 ├️ 📄 netflix-analise-pt2.py    # Código principal do dashboard Streamlit
 ├️ 📄 README.md                 # Este arquivo
```

---

## 📌 Pré-requisitos

Certifique-se de ter o Python 3.10+ instalado e crie um ambiente virtual:

```bash
python -m venv venv
source venv/bin/activate  # ou .\venv\Scripts\activate no Windows
pip install -r requirements.txt
```

**Dependências principais:**

```bash
pip install streamlit pandas matplotlib plotly
```

---

## 🚀 Como Executar o Dashboard

1. Baixe o dataset `netflix_titles.csv` (disponível no Kaggle).
2. Coloque o arquivo na raiz do projeto.
3. Execute o dashboard com:

```bash
streamlit run app.py
```

4. O navegador abrirá com a aplicação interativa.

---

## 📷 Capturas de Tela

*(Adicione imagens reais do seu dashboard na pasta **`imagens/`** e referencie aqui.)*

```markdown
![Dashboard - Filtros Ativos](imagens/filtros.png)
![Gráfico de Países](imagens/paises.png)
```

---

## 📚 Dataset

- **Fonte:** Kaggle – [Netflix Movies and TV Shows](https://www.kaggle.com/datasets/shivamb/netflix-shows)
- **Tamanho:** \~8.800 registros
- **Campos:** título, tipo, país, data de adição, ano de lançamento, duração, etc.

---

## 🧓‍♂️ Autores

- Gabriel Tiburcio
- Pedro Castro

---

## 💡 Melhorias Futuras

- Análise de notas e avaliações (caso disponíveis)
- Integração com APIs externas (ex: TMDB)
- Implementação de sistema de recomendações
- Análise mais profunda de gêneros e duração dos títulos

