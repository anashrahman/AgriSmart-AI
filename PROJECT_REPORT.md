# AgriSmart AI – Smart Agriculture Assistant
## Project Report (editable draft)

**Submitted by:** ____________________  
**Roll Number:** ____________________  
**Department:** Computer Science & Engineering  
**College:** ____________________  
**Academic Year:** ____________________

## Abstract
AgriSmart AI is a web-based smart agriculture assistant designed to support preliminary plant disease screening. A user uploads a photograph of a plant leaf, and a pretrained MobileNetV2 image-classification model predicts the most likely crop-condition class. The application displays the top predictions, confidence scores, general symptom information, and preventive guidance. It also provides a basic agriculture question-answer assistant and stores previous scans locally. The system is intended as an educational decision-support prototype and does not replace professional diagnosis.

## 1. Introduction
Agriculture is affected by plant diseases that can reduce crop quality and yield. Visual identification may be difficult without experience. Computer vision can help screen leaf images and provide preliminary information. AgriSmart AI combines image classification with a simple web interface to make this process accessible.

## 2. Problem Statement
Farmers and students may not have immediate access to expert plant-disease identification. A simple digital tool that screens leaf images and presents general guidance can help users understand possible crop-health issues earlier.

## 3. Objectives
- Build a user-friendly web application for leaf-image analysis.
- Integrate a pretrained deep-learning image classifier.
- Display top-3 predictions and confidence values.
- Present general disease information and preventive guidance.
- Provide an agriculture Q&A interface.
- Maintain a local history of previous scans.

## 4. Existing System
Traditional identification relies on visual inspection and expert consultation. It can be time-consuming and may not be immediately available. Generic online information may also be difficult to connect to a specific leaf image.

## 5. Proposed System
The proposed application accepts an image, preprocesses it through the model pipeline, and returns likely crop-condition classes. A guidance layer maps common disease terms to general prevention suggestions. Streamlit provides the user interface, while CSV storage records scan history.

## 6. System Architecture
1. User opens the Streamlit application.
2. User uploads a leaf image.
3. Image is converted to RGB.
4. Pretrained MobileNetV2 classifier predicts the top classes.
5. Application displays class labels and confidence scores.
6. Guidance module displays general information.
7. Scan details are saved to local CSV history.

## 7. Technology Stack
- Programming Language: Python
- UI: Streamlit
- Deep Learning: MobileNetV2
- Model Runtime: PyTorch and Hugging Face Transformers
- Image Processing: Pillow
- Data Handling: Pandas and CSV
- Dataset: PlantVillage

## 8. AI / Machine Learning Methodology
The application uses transfer learning through a pretrained MobileNetV2 image-classification model fine-tuned for 38 PlantVillage crop-condition classes. The model is downloaded from Hugging Face on first use. The image-classification pipeline preprocesses the input and returns ranked labels with scores. The application presents the scores as model confidence, not as a calibrated probability of field accuracy.

## 9. Modules
### 9.1 Home
Introduces the application and its features.
### 9.2 Disease Detection
Accepts a leaf image and displays top-3 predictions.
### 9.3 Farming Assistant
Answers common crop-care questions using a built-in knowledge base.
### 9.4 Detection History
Displays previous scans saved in CSV format.
### 9.5 About Project
Explains the purpose, technology, and limitations.

## 10. Hardware and Software Requirements
**Hardware:** 4 GB RAM minimum (8 GB recommended), dual-core processor, internet for first model download.  
**Software:** Windows/Linux/macOS, Python 3.10 or 3.11, VS Code or any Python IDE, modern web browser.

## 11. Testing
| Test case | Expected result |
|---|---|
| Open home page | Home dashboard loads |
| Upload JPG/PNG leaf image | Image preview appears |
| Run analysis with internet | Top predictions appear |
| Prediction confidence below 50% | Uncertainty warning appears |
| Open history after scan | Scan record is displayed |
| Enter farming question | General guidance is displayed |

## 12. Advantages
- Simple browser-based interface.
- Uses an actual pretrained image-classification model.
- No model training required during project setup.
- Top-3 predictions support uncertainty awareness.
- Includes guidance and scan history.

## 13. Limitations
- The model is trained on PlantVillage-style images; real-world field images may perform differently.
- The classifier supports a fixed set of 38 classes.
- The built-in assistant is a limited knowledge-base Q&A, not a general-purpose generative chatbot.
- Internet is needed for the initial model download.
- Predictions require expert confirmation before treatment decisions.

## 14. Future Scope
- Add a live generative-AI assistant with an API key.
- Add Hindi voice input and output.
- Add weather and soil data integration.
- Add region-specific crop advisory.
- Expand training data with real field images.
- Add user accounts and cloud database.

## 15. Conclusion
AgriSmart AI demonstrates how deep-learning image classification can be integrated into a practical web application for preliminary plant disease screening. The project combines computer vision, a user interface, guidance content, and scan history. It provides a foundation for future smart-agriculture systems while clearly communicating the limitations of model predictions.

## References
1. PlantVillage Dataset: https://plantvillage.psu.edu/
2. Hugging Face model: https://huggingface.co/neghani/plantvillage-mobilenetv2
3. Streamlit documentation: https://docs.streamlit.io/
4. Hugging Face Transformers documentation: https://huggingface.co/docs/transformers/
5. PyTorch documentation: https://pytorch.org/docs/
