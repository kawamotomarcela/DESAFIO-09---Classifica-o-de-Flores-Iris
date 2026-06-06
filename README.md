# 🌺 Classificação de Flores Iris — P2

Aplicação de Machine Learning feita em **Python + Streamlit** para classificar flores Iris em uma das três espécies: **Setosa**, **Versicolor** ou **Virginica**.

O projeto faz parte da P2 do **Desafio 09 - Iris**, desenvolvido pelo **Grupo 09**.

---

## 👥 Integrantes

| Nome | RA |
|---|---|
| Felipe Estevo Freitas | 1990153 |
| Marcela Kawamoto | 2224453 |

---

## 📖 Sobre o Projeto

Este projeto tem como objetivo classificar corretamente a espécie de uma flor Iris a partir de quatro medidas simples:

- comprimento da sépala;
- largura da sépala;
- comprimento da pétala;
- largura da pétala.

O dataset utilizado foi o **Iris**, carregado diretamente pela biblioteca `scikit-learn`.

Na P2, o projeto foi melhorado em relação à P1. O notebook foi reorganizado, o relatório foi atualizado, o modelo final foi salvo e a aplicação em Streamlit foi criada para permitir o teste do modelo de forma visual e prática.

---

## 🧠 Modelos Utilizados

Foram comparados três modelos de classificação:

- KNN;
- Regressão Logística;
- Random Forest.

A escolha do modelo final foi feita com base nas métricas de avaliação, principalmente o **F1 Score Macro** na validação cruzada.

O modelo final salvo no projeto foi:

**Regressão Logística**

---

## 📈 Resultados no Conjunto de Teste

| Métrica | Resultado |
|---|---:|
| Acurácia | 0.933 |
| Precisão Macro | 0.944 |
| Recall Macro | 0.933 |
| F1 Score Macro | 0.933 |

Os resultados mostram que o modelo teve um bom desempenho geral. A espécie **Setosa** foi a mais fácil de classificar, enquanto as maiores dificuldades ficaram entre **Versicolor** e **Virginica**, que possuem medidas mais parecidas em alguns casos.

---

## 📱 Aplicação Streamlit

A aplicação permite que o usuário informe as quatro medidas da flor e receba a espécie prevista pelo modelo.

**Link do app Streamlit:**  

https://desafio-09---classifica-o-de-flores-iris-rsm3to3kedfam67ka9edf.streamlit.app/

---

## 🏗️ Estrutura do Projeto

```text
projeto-iris-p2-grupo09/
│
├── app.py
├── requirements.txt
├── runtime.txt
├── README.md
│
├── assets/
│   └── style.css
│
├── notebooks/
│   └── notebook_atualizado.ipynb
│
├── model/
│   ├── modelo_final.pkl
│   ├── modelo_final.joblib
│   └── target_names.joblib
│
├── reports/
│   └── relatorio_atualizado.pdf
│
└── data/
    └── dataset.csv
```

---

## 🚀 Como Rodar o Projeto

Use o **Python 3.12**.

Não é recomendado usar Python 3.14, pois algumas bibliotecas de Machine Learning podem apresentar erro de instalação.

Para conferir as versões instaladas na máquina:

```bash
py -0
```

O ideal é aparecer algo parecido com:

```text
-V:3.14          Python 3.14.3
-V:3.12          Python 3.12
```

Neste projeto, deve ser usado o **Python 3.12**.

Dentro da pasta do projeto, crie o ambiente virtual com Python 3.12:

```bash
py -3.12 -m venv venv
```

No PowerShell, caso a ativação seja bloqueada, use:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned
.\venv\Scripts\Activate.ps1
```

Esse comando libera a execução de scripts apenas na janela atual do terminal.

No Prompt de Comando, a ativação pode ser feita com:

```cmd
venv\Scripts\activate
```

Quando o ambiente estiver ativo, deve aparecer algo como:

```text
(venv)
```

Com o ambiente virtual ativo, instale as dependências:

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

Se o VS Code não reconhecer o ambiente virtual como kernel do notebook, instale o `ipykernel`:

```bash
python -m pip install ipykernel
```

Caso ainda não apareça o kernel no VS Code, registre o ambiente manualmente:

```bash
python -m ipykernel install --user --name iris-p2 --display-name "Python 3.12 - Iris P2"
```

Depois, abra o notebook:

```text
notebooks/notebook_atualizado.ipynb
```

No VS Code, selecione o kernel do ambiente virtual:

```text
Python 3.12 - Iris P2
```

ou:

```text
venv
```

Depois clique em:

```text
Run All
```

Ao final da execução do notebook, os arquivos do modelo devem ser gerados ou atualizados na pasta:

```text
model/
```

Arquivos esperados:

```text
modelo_final.joblib
modelo_final.pkl
target_names.joblib
```

Depois que o modelo estiver salvo, execute o app Streamlit:

```bash
streamlit run app.py
```

Acesse no navegador:

```text
http://localhost:8501
```

---

## ☁️ Deploy no Streamlit Cloud

Para o deploy no Streamlit Cloud, o projeto utiliza o arquivo:

```text
runtime.txt
```

Esse arquivo define a versão do Python usada no ambiente online.

Conteúdo do `runtime.txt`:

```text
python-3.12
```

O arquivo `requirements.txt` é responsável por instalar as bibliotecas necessárias para o projeto funcionar.

---

## 🔧 Tecnologias Utilizadas

- Python 3.12;
- Streamlit;
- Pandas;
- NumPy;
- Scikit-learn;
- Matplotlib;
- Seaborn;
- Joblib;
- CSS personalizado.

---

## ✅ Conclusão

O projeto final da P2 apresenta uma versão mais organizada da P1. O notebook foi melhorado, os modelos foram comparados com validação cruzada, o modelo final foi salvo e a aplicação Streamlit permite testar a classificação de forma simples.

A entrega final ficou mais coerente porque o notebook, o relatório, o modelo salvo e o aplicativo usam os mesmos resultados e a mesma escolha de modelo.
