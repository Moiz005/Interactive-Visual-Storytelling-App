# Interactive Visual Storytelling App

A multimodal AI app that generates images with Stable Diffusion, stories with GPT-4o-mini, and audio with Coqui-AI TTS from text prompts. Built in Colab with a Gradio interface for vivid visuals and immersive narratives.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/interactive-visual-storytelling-app.git
   cd interactive-visual-storytelling-app
   ```

2. Install required packages:
   ```bash
   pip install diffusers==0.31.0 Pillow==10.4.0 openai==1.50.2 TTS==0.22.0 torch==2.4.1 numpy==1.26.4 gradio==4.44.1
   ```

## Prerequisites

- **Google Colab**: Run the app in a Colab notebook with a GPU runtime for faster processing.
- **OpenAI API Key**: Set `OPENAI_API_KEY` in Colab's Secrets (left sidebar, key icon).
- **Hugging Face Token** (optional): Required for Stable Diffusion model access. Run:
  ```python
  from huggingface_hub import login
  login()  # Enter your Hugging Face token
  ```

## Usage

1. Open the Colab notebook (`main.ipynb`) or Python script (`generate_story.py`).
2. Run the script to launch the Gradio interface.
3. Enter a text prompt (e.g., "A lone explorer in a mystical desert at twilight").
4. View the generated image, story, and play the audio narration in the Gradio UI.

## Example Prompt

```
A lone explorer in a mystical desert at twilight, surrounded by glowing cacti and ancient ruins under a starry sky, with a soft purple and blue color palette, highly detailed, cinematic lighting
```

## Notes

- Use a GPU runtime in Colab (**Runtime > Change runtime type > Hardware accelerator > GPU**).
- If you encounter a `numpy.dtype size changed` error, reinstall packages with:
  ```bash
  pip install numpy==1.26.4 --force-reinstall --no-cache-dir