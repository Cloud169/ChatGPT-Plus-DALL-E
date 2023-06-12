import streamlit as st
import openai

openai.api_key=st.secrets["api_key"]

st.title("Cloud 169")
st.subheader("맑은하늘 형성되는 구름의 이미지를 만나볼까요?")
with st.form("form"):
    
    user_input = st.text_input("prompt를 입력해주세요.")
    size = st.selectbox("Size",["1024x1024","512x512","256x256"])
    submit = st.form_submit_button("실행")

if submit and user_input:
    gpt_prompt=[{
        "role":"system",
        "content":"Imagine the detail appeareance of input.Response it shortly around 20 words."
    }]
    gpt_prompt.append({
        "role":"user",
        "content": user_input
    })

    with st.spinner("Waiting for ChatGPT...새로운 prompt를 생성 중 입니다."):

        gpt_response=openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=gpt_prompt
        )
    prompt=gpt_response["choices"][0]["message"]["content"]
    st.write(prompt)

    with st.spinner("Waiting for DALL-E...이미지 생성 중 입니다. "):
        dalle_response=openai.Image.create(
            prompt=prompt,
            size=size
        )

    st.image(dalle_response["data"][0]["url"])

