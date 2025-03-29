import writer as wf
from writer.core import WriterState
import requests
from ollama import chat
from ollama import ChatResponse
from ollama import Client

client = Client(
    host="http://localhost:11434",
    headers={
        "Content-Type": "application/json",
    },
)

# EVENT HANDLERS


async def submit_question(state: WriterState):
    response: ChatResponse = client.chat(
        model="llama3.2",
        messages=[
            {
                "role": "user",
                "content": state["prompt"],
            },
        ],
    )
    content = response["message"]["content"]
    state["response"] = content


# STATE INIT

initial_state = wf.init_state(
    {
        "response": "",
        "prompt": "",
    }
)
