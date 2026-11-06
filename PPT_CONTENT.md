# AgriSmart AI – PPT Slide Content

## Slide 1 – Title
AgriSmart AI: Smart Agriculture Assistant  
Presented by: __________ | Department: CSE

## Slide 2 – Introduction
- Plant diseases can reduce crop quality and yield.
- Early screening can help users seek advice sooner.
- AI computer vision can classify leaf images.

## Slide 3 – Problem Statement
- Disease identification may require experience.
- Expert help may not always be immediately available.
- Users need an accessible preliminary screening tool.

## Slide 4 – Objectives
- Upload and analyze leaf images.
- Predict likely crop-condition classes.
- Display confidence and general guidance.
- Provide farming Q&A and scan history.

## Slide 5 – Proposed System
- Streamlit web application.
- Pretrained MobileNetV2 classifier.
- 38 PlantVillage crop-condition classes.
- General guidance and history modules.

## Slide 6 – System Architecture
User → Streamlit UI → Image preprocessing → MobileNetV2 model → Top predictions → Guidance + History

## Slide 7 – Technology Stack
Python, Streamlit, PyTorch, Hugging Face Transformers, Pillow, Pandas, CSV.

## Slide 8 – Modules
Home, Disease Detection, AI Farming Assistant, Detection History, About Project.

## Slide 9 – Workflow
1. Upload leaf image.
2. Convert image to RGB.
3. Run image classifier.
4. Display top-3 classes and scores.
5. Show general prevention suggestions.
6. Save scan record.

## Slide 10 – Output
Insert screenshots of:
- Home page
- Uploaded leaf image
- Prediction result
- Farming Assistant
- Detection History

## Slide 11 – Advantages and Limitations
Advantages: easy interface, pretrained AI, top-3 results, history.  
Limitations: fixed classes, field-image domain gap, expert confirmation required.

## Slide 12 – Future Scope
Hindi voice assistant, live generative AI, weather integration, soil data, regional recommendations.

## Slide 13 – Conclusion
AgriSmart AI demonstrates an end-to-end AI-enabled web prototype for preliminary crop disease screening.

## Slide 14 – References
PlantVillage, Hugging Face model card, Streamlit docs, PyTorch docs.
