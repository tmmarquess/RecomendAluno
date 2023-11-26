import streamlit as st

from users import users
from recommend import Recommend
from add_user import add_user


def Recommend_app():
    st.title("Sistema de Recomendação Colaborativo para disciplinas optativas")

    username = st.text_input("Digite o nome do usuário:")

    if username not in users and username != "":
        st.sidebar.title("Inserir novo usuário")
        qnt_materias = st.sidebar.number_input(
            "quantidade de matérias que deseja avaliar", 1, 5
        )

        materias_avaliadas = []
        for i in range(qnt_materias):
            nome_materia = st.sidebar.text_input("Nome da matéria", key=f"{i}-1")
            avaliacao = st.sidebar.slider(
                "Nota da matéria", 0.0, 5.0, step=0.5, key=f"{i}-2"
            )
            materias_avaliadas.append((nome_materia, avaliacao))

        if st.sidebar.button("Adicionar"):
            add_user(username, materias_avaliadas, users)

    if st.button("Recomendar disciplinas"):
        if username in users:
            recommendations = Recommend(username, users)
            st.write(f"Recomendações para {username}:")
            for recommendation in recommendations:
                st.write(f"{recommendation[0]} - Pontuação: {recommendation[1]}")
        else:
            st.write("O usuário não foi encontrado. Você deseja inserí-lo no sistema?")
