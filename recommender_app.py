import streamlit as st
import pandas as pd

from users import users, subjects
from recommend import Recommend
from add_user import add_user


def Recommend_app():
    st.title("Sistema de Recomendação Colaborativo para disciplinas optativas")

    username = st.text_input("Digite o nome do usuário:")

    if username not in users and username != "":
        st.sidebar.title("Inserir novo usuário")
        qnt_materias = st.sidebar.number_input(
            "quantidade de matérias que deseja avaliar", 1, len(subjects)
        )

        materias_avaliadas = []
        for i in range(qnt_materias):
            nome_materia = st.sidebar.selectbox(
                "Nome da matéria", subjects, key=f"{i}-1"
            )
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

            recomend_dict = dict(subject=list(), score=list())
            for recomendation in recommendations:
                if recomendation[1] > 0:
                    recomend_dict["subject"].append(recomendation[0])
                    recomend_dict["score"].append(recomendation[1])

            st.dataframe(
                pd.DataFrame(recomend_dict),
                column_config={"subject": "Matéria", "score": "Pontuação"},
            )
        else:
            st.write("O usuário não foi encontrado. Você deseja inserí-lo no sistema?")
