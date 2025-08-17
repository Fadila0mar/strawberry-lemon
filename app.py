from flask import Flask, request, render_template, send_file
from ultralytics import YOLO
import cv2
import numpy as np
import io
from PIL import Image
import os

app = Flask(__name__)

# Load YOLO model
model = YOLO("yolov8n.pt")  # change to best.pt if that’s your trained weights

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        file = request.files["image"]
        img = Image.open(file.stream).convert("RGB")
        img = np.array(img)

        results = model(img)
        annotated = results[0].plot()

        # Encode image to return to browser
        _, img_encoded = cv2.imencode(".jpg", annotated)
        return send_file(
            io.BytesIO(img_encoded.tobytes()),
            mimetype="image/jpeg"
        )
    return render_template("index.html")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 7860))  # Hugging Face provides PORT
    app.run(host="0.0.0.0", port=port)
