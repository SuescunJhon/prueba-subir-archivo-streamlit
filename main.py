import streamlit as st
from pathlib import Path

st.set_page_config(page_title="Subir archivo", page_icon=":material/description:")
st.title("Gestor archivos")

ruta = Path("data/files")
ruta.mkdir(parents=True, exist_ok=True)


file = st.file_uploader("Subir archivo")

if file:
    ruta_archivo = ruta / file.name
    with open(ruta_archivo, "wb") as f:
        f.write(file.getbuffer())
    st.success(f"Archivo {file.name} se guardo correctamente.")

see_docs = st.button("Ver documentos", type="primary")
if see_docs:
    files = [f for f in ruta.iterdir() if f.is_file()]
    
    st.subheader("Archivos guardados")
    if files:
        for f in files:
            st.write(f.name)
    else:
        st.info("No hay archivos guardados.")