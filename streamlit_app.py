
import streamlit as st
from google_auth_oauthlib.flow import Flow
import base64
import os

st.set_page_config(page_title="TriMail", page_icon="✉️", layout="centered")

st.title("📬 TriMail")
st.subheader("Connectez-vous à votre compte Gmail pour trier automatiquement vos e-mails")

st.info("Cette démo est en construction. La connexion Gmail sera activée dès déploiement complet.")

st.markdown("---")
st.markdown("**Fonctionnement prévu :**")
st.markdown("- Connexion OAuth sécurisée à Gmail")
st.markdown("- Lecture seule des 30 derniers e-mails")
st.markdown("- Classement automatique : **Important / Publicité / Autres**")
st.markdown("- Aucune donnée stockée, tout se fait en mémoire")
st.markdown("---")
st.markdown("Déploiement à venir...")
