import gradio as gr
from openai import OpenAI

client = OpenAI(api_key='place api key ')

def openai_chat(message, history):
    history = history or []
    response = client.chat.completions.create(
      model="gpt-4-1106-preview",
      messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": message}
      ]
    )
    history.append((message, response.choices[0].message.content))
    return history, history

iface = gr.Interface(
    fn=openai_chat,
    inputs=["text", "state"],
    outputs=["chatbot", "state"],
    allow_flagging="never",
)

iface.launch()