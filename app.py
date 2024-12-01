import streamlit as st

from questions import Questionaire
from streaming_interface import streaming_interface

if __name__ == "__main__":
    if 'questions' not in st.session_state:
        st.session_state.questions = Questionaire()
        st.session_state.questions.initiate()
    streaming_interface()