import streamlit as st
import random

# Setting the title of the app
st.title('Number Guessing Game')

# Generating a random number between 1 and 100
target_number = random.randint(1, 100)
attempts = 0

# Session state to keep track of the number across reruns
if 'number' not in st.session_state:
    st.session_state.number = target_number

# Session state to keep track of attempts
if 'attempts' not in st.session_state:
    st.session_state.attempts = attempts

# Asking user for a number input
guess = st.number_input('Guess a number between 1 and 100', min_value=1, max_value=100, step=1)

# Button to check the guess
if st.button('Check Guess'):
    st.session_state.attempts += 1
    if guess < st.session_state.number:
        st.warning('Too low! Try again.')
    elif guess > st.session_state.number:
        st.error('Too high! Try again.')
    else:
        st.success(f'Congratulations! You guessed the number in {st.session_state.attempts} attempts.')
        st.session_state.number = random.randint(1, 100)  # Resetting the number
        st.session_state.attempts = 0  # Resetting the attempts

# Button to give up and show the correct number
if st.button('Give Up'):
    st.info(f'The correct number was {st.session_state.number}')
    st.session_state.number = random.randint(1, 100)  # Resetting the number for a new game
    st.session_state.attempts = 0  # Resetting the attempts
