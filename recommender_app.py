import streamlit as st
from users import users
from recommend import Recommend


def Recommend_app():
    st.title("Sistema de Recomendação Colaborativo para disciplinas optativas")

    username = st.text_input("Digite o nome do usuário:")

    if st.button("Recomendar disciplinas"):
        if username in users:
            recommendations = Recommend(username, users)
            st.write(f"Recomendações para {username}:")
            for recommendation in recommendations:
                st.write(f"{recommendation[0]} - Pontuação: {recommendation[1]}")
        else:
            st.write(
                "O usuário não foi encontrado. Por favor, insira um usuário válido."
            )
