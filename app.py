# Gradio UI
iface = gr.Interface(
    fn=predict_news,
    inputs=gr.Textbox(lines=10, placeholder="Paste a news article here..."),
    outputs="text",
    title="📰 Fake News Detector",
    description="Enter news text to detect if it's Real or Fake.",
)

iface.launch(share=True)
