import gradio as gr
from ultralytics import YOLO
import cv2

# Load your trained YOLOv8 model
model = YOLO("best.pt")  # replace with correct path if needed

def predict(image):
    # Run YOLO prediction
    results = model(image)
    
    # Annotated image with bounding boxes
    annotated_frame = results[0].plot()
    return annotated_frame

# Gradio interface
demo = gr.Interface(
    fn=predict,
    inputs=gr.Image(type="numpy", label="Upload an image"),
    outputs=gr.Image(type="numpy", label="Detection Result"),
    title="🍓🍋 Strawberry vs Lemon Detector",
    description="Upload an image and the YOLOv8 model will detect strawberries and lemons."
)

if __name__ == "__main__":
    demo.launch()
