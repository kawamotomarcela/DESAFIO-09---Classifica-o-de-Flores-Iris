from pathlib import Path

import joblib
import pandas as pd
import streamlit as st


BASE_DIR = Path(__file__).resolve().parent
MODEL_PATH = BASE_DIR / "model" / "modelo_final.joblib"
CLASSES_PATH = BASE_DIR / "model" / "target_names.joblib"
CSS_PATH = BASE_DIR / "assets" / "style.css"

FEATURES = [
    "sepal length (cm)",
    "sepal width (cm)",
    "petal length (cm)",
    "petal width (cm)",
]

SPECIES_INFO = {
    "setosa": {
        "nome": "Iris-setosa",
        "emoji": "🌸",
        "texto": "Geralmente é a espécie mais fácil de separar, principalmente pelas pétalas menores.",
    },
    "versicolor": {
        "nome": "Iris-versicolor",
        "emoji": "🌺",
        "texto": "Costuma ficar em uma região intermediária e pode se aproximar da virginica em algumas medidas.",
    },
    "virginica": {
        "nome": "Iris-virginica",
        "emoji": "🌷",
        "texto": "Normalmente apresenta pétalas maiores, mas pode ser confundida com a versicolor em alguns casos.",
    },
}


st.set_page_config(
    page_title="Classificação Iris - Grupo 09",
    page_icon="🌺",
    layout="centered",
    initial_sidebar_state="expanded",
)


def load_css() -> None:
    if CSS_PATH.exists():
        css = CSS_PATH.read_text(encoding="utf-8")
        st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)


@st.cache_resource(show_spinner="Carregando modelo final...")
def load_model():
    model = joblib.load(MODEL_PATH)
    classes = joblib.load(CLASSES_PATH)
    return model, classes


def predict_species(model, classes, values: dict) -> tuple[str, pd.DataFrame]:
    input_df = pd.DataFrame([values], columns=FEATURES)
    prediction = model.predict(input_df)[0]
    species = classes[prediction]
    return species, input_df


def render_header() -> None:
    st.markdown(
        """
        <div class="hero">
            <div class="hero-badge">🌺 Machine Learning - Iris</div>
            <h1>Classificador de Flores Iris</h1>
            <p>
                Aplicação em Streamlit do Grupo 09 para classificar flores Iris em
                <b>setosa</b>, <b>versicolor</b> ou <b>virginica</b>.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_sidebar() -> None:
    with st.sidebar:
        st.markdown("## 🌿 Sobre o projeto")
        st.write(
            "O modelo foi treinado com o dataset Iris, usando as medidas de sépala "
            "e pétala para prever a espécie da flor."
        )

        st.markdown("---")

        st.markdown("### 👥 Grupo 09")
        st.caption("Felipe Estevo Freitas - RA: 1990153")
        st.caption("Marcela Kawamoto - RA: 2224453")

        st.markdown("---")

        st.markdown("### 📌 Espécies")
        st.write("🌸 Iris-setosa")
        st.write("🌺 Iris-versicolor")
        st.write("🌷 Iris-virginica")


def render_form():
    st.markdown("## 📊 Informe as medidas da flor")

    with st.form("iris_form"):
        col1, col2 = st.columns(2)

        with col1:
            sepal_length = st.number_input(
                "Comprimento da sépala (cm)",
                min_value=0.0,
                max_value=10.0,
                value=5.1,
                step=0.1,
            )

            petal_length = st.number_input(
                "Comprimento da pétala (cm)",
                min_value=0.0,
                max_value=10.0,
                value=1.4,
                step=0.1,
            )

        with col2:
            sepal_width = st.number_input(
                "Largura da sépala (cm)",
                min_value=0.0,
                max_value=10.0,
                value=3.5,
                step=0.1,
            )

            petal_width = st.number_input(
                "Largura da pétala (cm)",
                min_value=0.0,
                max_value=10.0,
                value=0.2,
                step=0.1,
            )

        submitted = st.form_submit_button("🔮 Classificar flor")

    values = {
        "sepal length (cm)": sepal_length,
        "sepal width (cm)": sepal_width,
        "petal length (cm)": petal_length,
        "petal width (cm)": petal_width,
    }

    return submitted, values


def render_result(species: str, input_df: pd.DataFrame) -> None:
    info = SPECIES_INFO.get(species, {})

    st.markdown(
        f"""
        <div class="result-card">
            <div class="result-icon">{info.get("emoji", "🌺")}</div>
            <div>
                <p class="result-label">Resultado da classificação</p>
                <h2>{info.get("nome", species)}</h2>
                <p>{info.get("texto", "")}</p>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    with st.expander("Ver dados enviados ao modelo"):
        st.dataframe(input_df, use_container_width=True)


def render_model_explanation() -> None:
    with st.expander("📌 Como o modelo funciona"):
        st.write(
            "O app carrega o modelo final salvo no notebook. As quatro medidas digitadas "
            "são organizadas na mesma ordem usada durante o treinamento."
        )
        st.write(
            "Depois disso, o modelo faz a previsão e o app mostra o nome da espécie classificada."
        )



def main() -> None:
    load_css()
    render_header()
    render_sidebar()

    model, classes = load_model()

    submitted, values = render_form()

    if submitted:
        species, input_df = predict_species(model, classes, values)
        render_result(species, input_df)
    else:
        st.info("Preencha as medidas e clique em classificar flor para ver o resultado.")

    render_model_explanation()


if __name__ == "__main__":
    main()