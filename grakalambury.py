import streamlit as st
import random
import os

HIGHSCORE_FILE = "highscore.txt"
MAX_HIGHSCORES = 5

# Lista zagadek
zagadki = [
    ("""
      (__)    
      (oo)    
 /------\/  
/ |    ||   
*  /---\   
   ~~   ~~  
    """, "Krowa", ["Pies", "Krowa", "Owca", "Koza"]),
    ("""
     (o.o)  
     <(   )>  
      (   )   
     """, "Sowa", ["Sowa", "Krowa", "Koń", "Kangur"]),
    ("""
     (\_/)
     (o.o)
     (> <)
    """, "Królik", ["Królik", "Mysz", "Chomik", "Żaba"]),
]

# Funkcja do wczytywania wyników
def load_highscores():
    if os.path.exists(HIGHSCORE_FILE):
        with open(HIGHSCORE_FILE, "r") as file:
            return [line.strip().split(" - ") for line in file.readlines()]
    return []

# Funkcja do zapisywania wyników
def save_highscores(highscores):
    with open(HIGHSCORE_FILE, "w") as file:
        for name, score in highscores[:MAX_HIGHSCORES]:
            file.write(f"{name} - {score}\n")

# Inicjalizacja sesji
if "score" not in st.session_state:
    st.session_state.score = 0
    st.session_state.lives = 3
    st.session_state.used_questions = set()
    st.session_state.current_question = None
    st.session_state.game_over = False
    st.session_state.show_highscores = False

# Nagłówek gry
st.title("🎮 Kalambury w ASCII")
st.write("by Adam Kami")

# Ekran Highscore
if st.session_state.show_highscores:
    st.subheader("🏆 Najlepsze Wyniki")
    highscores = load_highscores()
    for i, (name, highscore) in enumerate(highscores, 1):
        st.write(f"{i}. {name} - {highscore}")
    if st.button("🔙 Powrót do menu"):
        st.session_state.show_highscores = False
    st.stop()

# Menu główne
if st.session_state.current_question is None and not st.session_state.game_over:
    st.subheader("📜 Menu Główne")
    if st.button("🎮 Start Gry"):
        st.session_state.score = 0
        st.session_state.lives = 3
        st.session_state.used_questions = set()
        st.session_state.current_question = random.choice(zagadki)
    if st.button("🏆 Zobacz Highscore"):
        st.session_state.show_highscores = True
    if st.button("❌ Wyjdź"):
        st.stop()

# Logika gry
if st.session_state.current_question and not st.session_state.game_over:
    zagadka, poprawna, opcje = st.session_state.current_question

    st.subheader("🔍 Zgadnij co to jest:")
    st.text(zagadka)

    wybor = st.radio("Wybierz odpowiedź:", options=opcje)

    if st.button("✅ Sprawdź"):
        if wybor == poprawna:
            st.session_state.score += 10
            st.success(f"✅ DOBRZE! +10 pkt! ({st.session_state.score} pkt)")
        else:
            st.session_state.lives -= 1
            st.error(f"❌ ZŁA ODPOWIEDŹ! Poprawna: {poprawna}")
        
        # Sprawdź, czy gra się kończy
        if st.session_state.lives == 0:
            st.session_state.game_over = True
        else:
            # Wybierz nową zagadkę
            st.session_state.current_question = random.choice(zagadki)

# Ekran Game Over
if st.session_state.game_over:
    st.subheader("💀 GAME OVER 💀")
    st.write(f"Twój wynik: {st.session_state.score}")

    highscores = load_highscores()
    if len(highscores) < MAX_HIGHSCORES or st.session_state.score > int(highscores[-1][1]):
        name = st.text_input("📝 Wpisz swoje imię:")
        if st.button("📜 Zapisz wynik"):
            highscores.append((name, str(st.session_state.score)))
            highscores.sort(key=lambda x: int(x[1]), reverse=True)
            save_highscores(highscores)
            st.session_state.show_highscores = True
            st.session_state.game_over = False
            st.session_state.current_question = None
            st.rerun()
    
    if st.button("🔁 Powrót do menu"):
        st.session_state.game_over = False
        st.session_state.current_question = None
        st.rerun()
