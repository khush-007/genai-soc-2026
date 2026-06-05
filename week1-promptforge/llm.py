# llm.py

from groq import Groq

from config import (
    GROQ_API_KEY,
    MODEL_NAME,
    DEFAULT_TEMPERATURE
)

client = Groq(
    api_key=GROQ_API_KEY
)

def get_llm_response(
    messages,
    temperature=DEFAULT_TEMPERATURE
):

    try:

        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=messages,
            temperature=temperature
        )

        return response.choices[0].message.content

    except Exception as e:

        return f"Error: {str(e)}"

def stream_llm_response(
    messages,
    temperature=DEFAULT_TEMPERATURE
):

    try:

        stream = client.chat.completions.create(
            model=MODEL_NAME,
            messages=messages,
            temperature=temperature,
            stream=True
        )

        full_response = ""

        for chunk in stream:

            content = chunk.choices[0].delta.content

            if content:

                full_response += content

                yield full_response

    except Exception as e:

        yield f"Error: {str(e)}"