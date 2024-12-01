
import streamlit as st


def streaming_interface():
    st.set_page_config(
        page_title=f"Curriculumly WhatsApp GPT",
        page_icon="📝🔍",
        layout="wide"
    )
    st.title(f"Curriculumly WhatsApp GPT")

    # Display all previous messages
    for message in st.session_state.questions.history.logs:
        if message["role"] == "system":
            continue
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    user_prompt = st.chat_input()  # Input box for the user

    if user_prompt is not None:
        st.session_state.questions.listen(user_prompt)
        with st.chat_message("user"):
            st.markdown(user_prompt)

        # Placeholder for the assistant's reply
        assistant_message_placeholder = st.chat_message("assistant")
        assistant_text = assistant_message_placeholder.empty()

        # Stream response
        with st.spinner("Loading..."):
            answer = st.session_state.questions.respond()
            assistant_text.markdown(answer)
