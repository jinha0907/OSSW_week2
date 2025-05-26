import gradio as gr
def greet(name, enthusiasm):
    return f"Hello {name} {'🎉' * enthusiasm}"

demo = gr.Interface(
    fn=greet,
    inputs=[
        gr.Textbox(label="Name", value="김진하"),
        gr.Slider(minimum=1, maximum=5, step=1, label="Enthusiasm")
    ],
    outputs=gr.Textbox(label="Greeting"),
    title="Simple Greetings App",
    description="A simple app to greet users with enthusiasm."
)

if __name__ == "__main__":
    demo.launch()