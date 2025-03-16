import streamlit as st

# ---------- TÍTULO PRINCIPAL ----------
st.set_page_config(page_title="Generador de Analizadores Léxicos", layout="wide")
st.title("Generador de Analizadores Léxicos - YALex")
st.markdown("### Proyecto de Laboratorio - Previsualización de Interfaz Gráfica")

st.markdown("---")

# ---------- CARGA DEL ARCHIVO YALex ----------
st.header("📁 Cargar Especificación en YALex")

uploaded_file = st.file_uploader("Selecciona un archivo .yalex", type=["yalex"])

if uploaded_file is not None:
    content = uploaded_file.read().decode("utf-8")
    st.success("✅ Archivo cargado correctamente.")
    st.text_area("📄 Contenido del archivo YALex", content, height=300)
else:
    st.info("Aún no se ha cargado ningún archivo.")
