from flask import Flask, request, jsonify
from transformers import AutoProcessor, AutoModelForCausalLM
import torch
from scipy.io.wavfile import write

app = Flask(__name__)

# Load the processor and model
processor = AutoProcessor.from_pretrained("facebook/musicgen-small")
model = AutoModelForCausalLM.from_pretrained("facebook/musicgen-small")
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)

@app.route('/generate_audio', methods=['POST'])
def generate_audio():
    # Get input text from the frontend
    input_text = request.json['text']
    
    # Process input text
    inputs = processor(
        text=[input_text],
        padding=True,
        return_tensors="pt",
    )

    # Generate audio
    audio_values = model.generate(**inputs.to(device), do_sample=True, guidance_scale=3, max_new_tokens=1024)
    
    # Save the generated audio
    audio_path = "generated_audio.wav"
    write(audio_path, 22050, audio_values[0].cpu().numpy())

    # Return the path to the generated audio
    return jsonify({'audio_path': audio_path})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000,debug=True)
