from api.AI import AIAPI
import streamlit as st


def main():
    text = None

    st.title("2023 HAI Web App Project")

    st.header("책 읽어주는 인공지능\n")
    image = st.file_uploader("책 이미지 입력\n")

    if 'button' not in st.session_state:
        st.session_state.button = False

    def click_button():
        st.session_state.button = not st.session_state.button

    st.button('입력', key=1, on_click=click_button)

    if st.session_state.button:
        with st.expander("입력된 이미지 보기"):
            st.image(image)
        with st.expander("OCR 결과"):
            text = AIAPI.query_image2text(image, image)
            st.write(text)
        with st.expander("요약 결과"):
            title, summary = AIAPI.query_text2text(text, text)
            st.subheader(title)
            st.write(summary)
        
        
if __name__ == '__main__':
    main()