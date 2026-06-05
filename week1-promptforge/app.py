import gradio as gr
from personas import PERSONAS
from utils import build_messages
from llm import stream_llm_response
from formatter import format_code_review

def chat_function(message, history, mode, temperature,current_chat,chat_store):

    if history is None:
        history = []

    user_history = history + [
        {
            "role": "user",
            "content": message
        }
    ]

    assistant_message = ""

    for chunk in stream_llm_response(
            build_messages(
                mode,
                message,
                history
            ),
            temperature
    ):

        assistant_message = chunk

        yield (
            "",
            user_history + [
                {
                    "role": "assistant",
                    "content": assistant_message
                }
            ],
            chat_store
        )

    # Streaming complete hone ke baad
    final_response = assistant_message

    if mode == "Code Reviewer":

        final_response = format_code_review(
            assistant_message
        )

        yield (
            "",
            user_history + [
                {
                    "role": "assistant",
                    "content": final_response
                }
            ],
            chat_store
        )

    final_chat = (
            user_history +
            [
                {
                    "role": "assistant",
                    "content": final_response
                }
            ]
    )

    chat_store[current_chat] = final_chat

with gr.Blocks(title="PromptForge") as demo:
    gr.HTML("""
    <div style='text-align:center'>
        <h1>🚀 PromptForge</h1>
        <h3>Multi-Persona AI Assistant</h3>
    </div>
    """)

    gr.Markdown(
        "Multi-Persona AI Assistant"
    )

    with gr.Row():
        with gr.Column(scale=1):
            mode = gr.Dropdown(
                choices=list(PERSONAS.keys()),
                value="Technical Explainer",
                label="Select Mode"
            )

            temperature = gr.Slider(
                minimum=0,
                maximum=2,
                value=0.7,
                step=0.1,
                label="Temperature"
            )

            new_chat_btn = gr.Button("➕ New Chat")

            with gr.Accordion("Active System Prompt", open=False):
                system_prompt = gr.Textbox(
                    value=PERSONAS["Technical Explainer"]["system_prompt"],
                    lines=8,
                    interactive=False
                )


            def update_prompt(mode):
                return PERSONAS[mode]["system_prompt"]


            mode.change(
                fn=update_prompt,
                inputs=mode,
                outputs=system_prompt
            )

            clear_btn = gr.Button(
                "🗑️ Clear Chat"
            )

            chat_selector = gr.Radio(
                choices=["Chat 1"],
                value="Chat 1",
                label="Chat History"
            )

        with gr.Column(scale=3):
            chatbot = gr.Chatbot(
                height=600
            )

            msg = gr.Textbox(
                placeholder="Ask anything..."
            )

        chat_store = gr.State({
            "Chat 1": []
        })

        current_chat = gr.State("Chat 1")


        def create_new_chat(chat_store):
            chat_num = len(chat_store) + 1

            chat_name = f"Chat {chat_num}"

            chat_store[chat_name] = []

            return (
                chat_store,
                gr.update(
                    choices=list(chat_store.keys()),
                    value=chat_name
                ),
                chat_name,
                [],
                ""
            )


        new_chat_btn.click(
            fn=create_new_chat,
            inputs=[chat_store],
            outputs=[
                chat_store,
                chat_selector,
                current_chat,
                chatbot,
                msg
            ]
        )


        def load_chat(chat_name, chat_store):
            return (
                chat_name,
                chat_store.get(chat_name, [])
            )


        chat_selector.change(
            fn=load_chat,
            inputs=[
                chat_selector,
                chat_store
            ],
            outputs=[
                current_chat,
                chatbot
            ]
        )

    msg.submit(
        fn=chat_function,
        inputs=[
            msg,
            chatbot,
            mode,
            temperature,
            current_chat,
            chat_store
        ]
        ,
        outputs=[
            msg,
            chatbot,
            chat_store
        ]
    )





demo.launch()