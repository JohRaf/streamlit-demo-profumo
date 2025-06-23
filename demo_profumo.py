import streamlit as st
import pandas as pd

# Carica dati demo da CSV
df = pd.read_csv("prezzi_profumi.csv")

st.title("🔍 Trova il miglior prezzo per il tuo profumo")
prodotto = st.text_input("Digita il nome del profumo:")

if prodotto:
    risultati = df[df["nome_prodotto"].str.lower().str.contains(prodotto.lower())]
    if risultati.empty:
        st.warning("❌ Prodotto non trovato nei dati demo.")
    else:
        miglior_offerta = risultati.sort_values("prezzo").iloc[0]
        st.success(f"💰 Prezzo migliore: {miglior_offerta['prezzo']}€ su {miglior_offerta['negozio']}")
        st.markdown(f"[🔗 Vai al negozio]({miglior_offerta['url']})")
