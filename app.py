import os
import gradio as gr

# Get route from environment variable, with fallback
route = os.environ.get("ROUTE", "/text-processor")

def process_text(text, operation):
    """Process text based on the selected operation"""
    if operation == "Uppercase":
        return text.upper()
    elif operation == "Lowercase":
        return text.lower()
    elif operation == "Title Case":
        return text.title()
    elif operation == "Reverse":
        return text[::-1]
    elif operation == "Word Count":
        return f"Word count: {len(text.split())}"
    elif operation == "Character Count":
        return f"Character count: {len(text)}"
    else:
        return text

with gr.Blocks() as demo:
    gr.Markdown("# Simple Text Processor")
    gr.Markdown("Enter some text and select an operation to transform it!")
    
    with gr.Row():
        with gr.Column():
            text_input = gr.Textbox(
                label="Enter your text",
                placeholder="Type something here...",
                lines=5
            )
            operation = gr.Radio(
                ["Uppercase", "Lowercase", "Title Case", "Reverse", "Word Count", "Character Count"],
                label="Select operation",
                value="Uppercase"
            )
            process_button = gr.Button("Process Text", variant="primary")
        
        with gr.Column():
            text_output = gr.Textbox(
                label="Result",
                lines=5,
                interactive=False
            )
    
    with gr.Accordion("Examples", open=True):
        gr.Examples(
            examples=[
                ["Hello World! This is a Gradio app.", "Uppercase"],
                ["CONVERT THIS TO LOWERCASE", "Lowercase"],
                ["reverse this text", "Reverse"],
                ["Count the words in this sentence", "Word Count"]
            ],
            inputs=[text_input, operation],
            outputs=text_output,
            fn=process_text
        )
    
    process_button.click(
        process_text,
        inputs=[text_input, operation],
        outputs=text_output
    )

demo.launch(root_path=route, share=True, server_port=8050, server_name="0.0.0.0")
