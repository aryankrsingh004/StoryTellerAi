import time
from google import genai
import streamlit as st

api_key = st.secrets["api"]["key"]
prompt = "You are a creative and imaginative AI storyteller. The user will provide the beginning of a story, and your task is to continue it in a compelling and engaging way, maintaining coherence, style, and tone. Your response should build on the provided introduction, adding depth to characters, developing the plot, and ensuring a satisfying flow. Keep the story immersive and unpredictable while staying true to the user’s input.The output should not contain any thing else. The Lenght of the story should be around 300 words. The user input is: "


def generate_response(user_input):
    
    client = genai.Client(api_key = api_key)
    response = client.models.generate_content_stream(
        model="gemini-2.0-flash", contents = prompt + user_input
    )
    # response = client.models.generate_content(
    #     model="gemini-2.0-flash", contents = prompt + user_input
    # )
    # return response
    full_text = ""
    for chunk in response:
        full_text += chunk.text
        output.write(full_text)
        time.sleep(0.3)
        # st.write(chunk.text, end="")
        # print(chunk.text, end="")

st.title("AI Storyteller")
st.write("Give me the beginning of a story, and I will continue it in a compelling and engaging way!")

if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
# for message in st.session_state.messages:
#     with st.chat_message(message["role"]):
#         st.write(message["content"])

user_input = st.chat_input("Type your message here...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.write(user_input)
    
    output = st.empty()
    generate_response(user_input)
    # response = generate_response(user_input)
    # st.session_state.messages.append({"role": "assistant", "content": response})
    # with st.chat_message("assistant"):
    #     st.write(response.text)