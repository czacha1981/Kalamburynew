import streamlit as st
import random

# Tytuł gry
st.title("🇵🇱 POLSKA MENTALNOŚĆ 🇵🇱")
st.subheader("Wybierz swoją reakcję na codzienność!")

# Lista kategorii i obrazków (przykładowe opisy, można dodać obrazy)
kategorie = {
    "Człowiek w garniturze": "👨‍💼",
    "Sąsiad zagląda przez okno": "👀",
    "Korek na drodze": "🚗🚕🚙",
    "Polityk w TV": "📺🗣️",
    "Lekarz w szpitalu": "🏥👨‍⚕️",
    "Szef w pracy": "💼",
    "Gołąb na balkonie": "🕊️",
    "Janusz na wakacjach": "🌴🍺",
    "Nowe BMW pod blokiem": "🚘"
}

# Lista polskich reakcji
reakcje = [
    "🤬 Nienawidzę!", 
    "🍾 Napiłbym się wódki!", 
    "🤨 Sąsiad to złodziej!", 
    "☝️ Jego wina!", 
    "🤕 Niech mu się noga złamie!", 
    "🕊️ Niech go gołąb osra!"
]

# Wybór losowej kategorii
obrazek, emoji = random.choice(list(kategorie.items()))

st.markdown(f"### {emoji} {obrazek}")

# Przyciski do wyboru reakcji
wybrana_reakcja = st.radio("Jak zareagujesz?", reakcje)

# Po wybraniu reakcji wyświetlamy humorystyczny komunikat
if st.button("Zatwierdź wybór"):
    st.success(f"Twoja reakcja: {wybrana_reakcja} - typowo po polsku! 🇵🇱😂")

