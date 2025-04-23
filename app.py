import streamlit as st
import random

#Initialize session stand for storing the random number 
if 'number' not in st.session_state:
    st.session_state.number = random.randint(1, 10)

#Initialize session stand for storing the number of attempts
if 'attempts' not in st.session_state:
    st.session_state.attempts = 0
    st.set_page_config(page_title="🎲Guess the Number ", page_icon=":guardsman:", layout="centered") # type: ignore
    
 #Game header
st.markdown("<h1 style='text-align: center;'>🎲Guess the Number Game🎯 </h1>", unsafe_allow_html=True)

st.markdown("<h4 style='text-align: center;'>I have chosen a number between 1 and 10. Can you guess it?</h4>", unsafe_allow_html=True)

#Get user's guess'
guess = st.number_input("Enter your guess:", min_value=1, max_value=10, step=1)

#Check button
if st.button("Check guess"):
    st.session_state.attempts += 1
    if guess == st.session_state.number:
        st.success(f"🎉Congratulations! You guessed the correct number in {st.session_state.number} in {st.session_state.attempts} attempts.")
        st.session_state.number = random.randint(1, 10)        
        st.session_state.attempts = 0

    else:
        st.error("Incorrect guess. Plaese try again")
        
        #Reset the button

        if st.button ("Reset Game"):
            st.session_state.number = random.randint(1, 10)
            st.session_state.attempts = 0
            st.rerun()

            st.markdown("---")
st.markdown("<p style='text-align: center; color: red;'>Made with ☕ and ❤️ by Ufaq Fatima</p>", unsafe_allow_html=True)
