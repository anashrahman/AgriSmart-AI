# AgriSmart AI – Smart Agriculture Assistant

A college-level web application for plant-leaf disease screening and general crop-care guidance.

## Features
- Image-based plant disease classification using a pretrained MobileNetV2 model.
- Top-3 predictions and confidence scores.
- General disease information and prevention suggestions.
- Built-in agriculture Q&A assistant.
- Local CSV detection history and dashboard.
- About page describing architecture and limitations.

## Requirements
- Windows 10/11, macOS, or Linux
- Python 3.10 or 3.11 recommended
- Internet connection on first run (to download the pretrained model)
- 4 GB RAM minimum; 8 GB recommended

## Run on Windows
1. Extract the ZIP.
2. Open the extracted folder in VS Code.
3. Open Terminal in that folder.
4. Run:

```bash
py -3.11 -m venv .venv
.venv\Scripts\activate
python -m pip install --upgrade pip
pip install -r requirements.txt
streamlit run app.py
```

If `py -3.11` is unavailable, use `python -m venv .venv`.

The browser should open at `http://localhost:8501`.

## AI model
The app uses `neghani/plantvillage-mobilenetv2` from Hugging Face, a MobileNetV2 image-classification model with 38 PlantVillage crop-condition classes. It is loaded automatically the first time a scan is run.

Model page: https://huggingface.co/neghani/plantvillage-mobilenetv2

## Important limitations
PlantVillage images were collected in controlled conditions. Real farm photos can have different lighting, backgrounds, multiple leaves, and symptoms. Confidence is not a guarantee of correctness. The system is an educational screening aid, not a substitute for a plant pathologist or local agricultural extension officer. Do not apply pesticides or other treatments solely based on this output.

## Troubleshooting
- **Model download fails:** check internet access and retry.
- **Torch installation issue:** use Python 3.10/3.11 64-bit and install requirements again.
- **Slow first scan:** expected; model files are downloaded and cached on first use.
- **Port in use:** run `streamlit run app.py --server.port 8502`.

## Project structure
```text
Smart_Agriculture_AI/
├── app.py
├── requirements.txt
├── README.md
├── PROJECT_REPORT.md
├── PPT_CONTENT.md
└── data/
```
