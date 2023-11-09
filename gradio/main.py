import gradio as gr
import pyjokes


def get_joke():
    return pyjokes.get_joke()


def greet(first_name, last_name, is_mr, is_rain, make_joke):
    salutation = "Mr." if is_mr else "Ms."
    suffix = " and it's raining" if is_rain else ""

    if make_joke:
        joke = get_joke()
    return f"Hello {salutation} {first_name} {last_name}{suffix}!\n{joke}"


# message and history required parameters of gr.ChatInterface
def random_responses(message, history):
    # random functionality
    return get_joke()


# any component created inside this clause is automatically added to the app
# Components appear vertically in the app in the order they are created
with gr.Blocks() as demo:
    gr.Markdown("Introduce yourself and I will greet you or chat with me.")

    with gr.Tab("Introduce yourself"):
        first_name = gr.Textbox(
            label="first name", lines=2, placeholder="First Name Here..."
        )
        last_name = gr.Textbox(
            label="last name", lines=2, placeholder="Last Name Here..."
        )
        output = gr.Textbox(label="Output box")
        greet_button = gr.Button("Greet")
        greet_button.click(
            fn=greet,
            inputs=[
                first_name,
                last_name,
                gr.Checkbox(label="is mr"),
                gr.Checkbox(label="is rain"),
                gr.Checkbox(label="make joke"),
            ],
            outputs=output,
            api_name="greet",
        )

    with gr.Tab("Chat"):
        gr.ChatInterface(random_responses)


if __name__ == "__main__":
    demo.launch(show_api=True)
