import streamlit as st
from pathlib import Path

st.title("Cadastro de clientes")

nome = st.text_input("Digite o nome do cliente")
endereco = st.text_input("Digite o endereço")
dt_nasc = st.date_input("Escolha a data de nascimento")
tipo_cliente = st.selectbox("Tipo de cliente",
                            ["Pessoa física", "Pessoa jurídica"])

cadastrar = st.button("Cadastrar cliente")

if cadastrar:
    if not nome.strip():
        st.error("Por favor, preencha o nome do cliente.")
    else:
        # garante que o arquivo será criado na mesma pasta do app.py
        file_path = Path(__file__).parent / "clientes.csv"
        with open(file_path, "a", encoding="utf-8", newline="") as arquivo:
            arquivo.write(f"{nome},{endereco},{dt_nasc.isoformat()},{tipo_cliente}\n")
        st.success("Cliente cadastrado com sucesso!")
        st.info(f"Arquivo salvo em: {file_path}")