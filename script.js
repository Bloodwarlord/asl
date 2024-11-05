// script.js
const video = document.getElementById("video");
const prediction = document.getElementById("prediction");
const confidence = document.getElementById("confidence");

// Access the device camera and stream to the video element
navigator.mediaDevices
  .getUserMedia({ video: true })
  .then((stream) => (video.srcObject = stream))
  .catch((error) => console.error("Error accessing the webcam", error));

// Capture the current video frame and send it to the backend
function captureImage() {
  const canvas = document.createElement("canvas");
  canvas.width = video.width;
  canvas.height = video.height;
  canvas.getContext("2d").drawImage(video, 0, 0, canvas.width, canvas.height);
  canvas.toBlob((blob) => {
    const formData = new FormData();
    formData.append("image", blob, "frame.jpg");

    fetch("/predict", {
      method: "POST",
      body: formData,
    })
      .then((response) => response.json())
      .then((data) => {
        prediction.innerText = `Prediction: ${data.prediction}`;
        confidence.innerText = `Confidence: ${data.confidence.toFixed(2)}`;
      })
      .catch((error) => console.log("Error:", error));
  });
}
