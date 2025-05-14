import streamlit as st
from google_auth_oauthlib.flow import Flow
from googleapiclient.discovery import build
import base64

st.set_page_config(page_title="TriMail", layout="centered")
st.title("📬 TriMail - Lecture et tri automatique de vos mails Gmail")

# État initial
if "credentials" not in st.session_state:
    st.session_state["credentials"] = None
if "messages_scanned" not in st.session_state:
    st.session_state["messages_scanned"] = 0

CLIENT_SECRET_JSON = "client_secret.json"
SCOPES = ['https://www.googleapis.com/auth/gmail.modify']

# Étape 1 : Connexion OAuth
if st.session_state["credentials"] is None:
    flow = Flow.from_client_secrets_file(
        CLIENT_SECRET_JSON,
        scopes=SCOPES,
        redirect_uri='urn:ietf:wg:oauth:2.0:oob'
    )
    auth_url, _ = flow.authorization_url(prompt='consent')
    st.markdown(f"[1. Clique ici pour te connecter à Gmail]({auth_url})")
    code = st.text_input("2. Colle ici le code d'autorisation Google")

    if code:
        flow.fetch_token(code=code)
        st.session_state["credentials"] = flow.credentials
        st.success("Connexion réussie ! Recharge la page.")
        st.stop()

else:
    creds = st.session_state["credentials"]
    service = build('gmail', 'v1', credentials=creds)

    st.markdown("### Étape 2 : Lecture de 100 mails")
    response = service.users().messages().list(userId='me', maxResults=100).execute()
    messages = response.get('messages', [])

    if messages:
        for msg in messages:
            full_msg = service.users().messages().get(userId='me', id=msg['id']).execute()
            headers = full_msg['payload'].get('headers', [])
            subject = next((h['value'] for h in headers if h['name'] == 'Subject'), "(Sans objet)")
            st.write(f"**Objet :** {subject}")
            st.session_state["messages_scanned"] += 1

        st.success(f"{st.session_state['messages_scanned']} mails analysés.")
    else:
        st.info("Aucun nouveau mail trouvé.")
