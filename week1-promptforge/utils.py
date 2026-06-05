from personas import PERSONAS


from personas import PERSONAS

def build_messages(mode, user_message, history=None):

    persona = PERSONAS[mode]

    messages = []

    # System Prompt
    messages.append(
        {
            "role": "system",
            "content": persona["system_prompt"]
        }
    )

    # Few-shot examples
    for example in persona["few_shot_examples"]:

        messages.append(
            {
                "role": "user",
                "content": example["user"]
            }
        )

        messages.append(
            {
                "role": "assistant",
                "content": example["assistant"]
            }
        )

    # Previous conversation
    if history:

        for msg in history:

            messages.append(
                {
                    "role": msg["role"],
                    "content": msg["content"]
                }
            )

    # Current message
    messages.append(
        {
            "role": "user",
            "content": user_message
        }
    )

    return messages