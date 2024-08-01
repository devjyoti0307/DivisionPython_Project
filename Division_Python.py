import streamlit as st
import base64

book_data = {
    "Pride and Prejudice": {
        "image": "../diversion/images/pridePrejudice.png",
        "pdf": "../diversion/pdfs/pridePrejudice.pdf"
    },
    "Animal Farm": {
        "image": "",
        "pdf": ""
    },
    "The Alchemist": {
        "image": "",
        "pdf": ""
    },
    "The Theory of Everything": {
        "image": "",
        "pdf": ""
    }
}

def displayPDF(file):

    with open(file, "rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode('utf-8')


    pdf_display = f'<embed src="data:application/pdf;base64,{base64_pdf}" width="750" height="1000" type="application/pdf">'

    st.markdown(pdf_display, unsafe_allow_html=True)

def chat_page(book_title):
    st.image(book_data[book_title]["image"], use_column_width=True)
    st.title(f"{book_title} Chat")

    pdf_path = book_data[book_title]["pdf"]
    displayPDF(pdf_path)

    user_input = st.text_input("Your message:", key="user_input")

    if st.button("Send"):
        response = generate_response(user_input)
        chat_history = st.session_state.chat_output
        chat_history += f"\nYou: {user_input}\nBot: {response}"
        st.session_state.chat_output = chat_history

    st.text_area("Chat", "", height=400, max_chars=None, key="chat_output", disabled=True)

def generate_response(user_input):
    return f"You said: {user_input}"

def main():
    st.sidebar.title("Navigation")
    pages = ["Pride and Prejudice", "Animal Farm", "The Alchemist", "The Theory of Everything"]

    selected_page = st.sidebar.selectbox("Go to", pages)

    if selected_page == "Pride and Prejudice":
        chat_page("Pride and Prejudice")
    elif selected_page == "Animal Farm":
        chat_page("Animal Farm")
    elif selected_page == "The Alchemist":
        chat_page("The Alchemist")
    elif selected_page == "The Theory of Everything":
        chat_page("The Theory of Everything")

if __name__ == "__main__":
    main()