// Example using fetch API in JavaScript
const inputText = "authentic set of Indian Garba beats that capture the essence of traditional folk percussion, incorporating rhythmic patterns like the Dandiya Raas, to evoke the lively energy and festive atmosphere of Navratri celebrations";

fetch('/generate_audio', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json'
  },
  body: JSON.stringify({ text: inputText })
})
.then(response => response.json())
.then(data => {
  const audioPath = data.audio_path;
  // Use audioPath to play or display the generated audio in the frontend
});
