import matplotlib.pyplot as plt
from diffusers import DiffusionPipeline
import torch
from openai import OpenAI
from TTS.api import TTS
import gradio as gr
import base64
from PIL import Image

import os
os.environ["hf_token"] = "HF_TOKEN"
os.environ["OPENAI_API_KEY"] = "OPENAI_API_KEY"

device = "cuda" if torch.cuda.is_available() else "cpu"

img_pipe = DiffusionPipeline.from_pretrained(
    "stable-diffusion-v1-5/stable-diffusion-v1-5",
    torch_dtype=torch.float16
).to(device)

def encode_image(image_path):
  with open(image_path, "rb") as image_file:
      return base64.b64encode(image_file.read()).decode('utf-8')

def generate_story(img_prompt):
  image = img_pipe(img_prompt).images[0]
  img_path = "image.png"
  image.save(img_path)
  base64_image = encode_image("image.png")
  response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "Write an engaging story based on the provided image. The story should be vivid, immersive, and capture the atmosphere of the scene."
                },
                {
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:image/png;base64,{base64_image}"
                    }
                }
            ]
        }
    ],
    max_tokens=500
  )
  story = response.choices[0].message.content
  tts = TTS(model_name="tts_models/en/ljspeech/fast_pitch").to(device)
  audio_path = "story.wav"
  tts.tts_to_file(text=story, file_path=audio_path)
  return Image.open(img_path), story, audio_path

interface = gr.Interface(
    fn=generate_story,
    inputs=gr.Textbox(label="Image Prompt", placeholder="Astronaut in a jungle, cold color palette"),
    outputs=[
        gr.Image(label="Generated Image"),
        gr.Textbox(label="Generated Story"),
        gr.Audio(label="Story Audio", type="filepath")
    ],
    title="Interactive Visual Storytelling App",
    description="Enter a prompt to generate an image, story, and audio narration."
)

interface.launch()