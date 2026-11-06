
import os
import datetime
import streamlit as st
import pandas as pd
from PIL import Image

# PAGE CONFIGURATION
st.set_page_config(
    page_title="AgriSmart AI",
    page_icon="🌱",
    layout="wide"
)

MODEL_ID = "neghani/plantvillage-mobilenetv2"
HISTORY_FILE = "data/history.csv"

# DISEASE INFORMATION
DISEASE_INFO = {
    "healthy": {
        "title": "Healthy Leaf",
        "symptoms": "No disease pattern identified.",
        "action": "Continue regular monitoring and balanced irrigation."
    },
    "early_blight": {
        "title": "Early Blight",
        "symptoms": "Brown spots with concentric rings.",
        "action": "Remove affected leaves, improve airflow and avoid overhead watering."
    },
    "late_blight": {
        "title": "Late Blight",
        "symptoms": "Dark, water-soaked lesions.",
        "action": "Remove infected material safely and seek agricultural advice."
    },
    "leaf_mold": {
        "title": "Leaf Mold",
        "symptoms": "Yellow patches and olive-gray growth.",
        "action": "Improve ventilation and avoid leaf wetness."
    },
    "bacterial": {
        "title": "Possible Bacterial Disease",
        "symptoms": "Dark spots and yellow halos.",
        "action": "Sanitize tools and seek expert diagnosis."
    },
    "rust": {
        "title": "Rust",
        "symptoms": "Orange or reddish powdery spots.",
        "action": "Remove heavily infected leaves and improve airflow."
    },
    "mildew": {
        "title": "Mildew",
        "symptoms": "Powdery or downy growth.",
        "action": "Improve spacing and airflow."
    },
    "spot": {
        "title": "Leaf Spot",
        "symptoms": "Brown, black or tan lesions.",
        "action": "Remove infected debris and avoid overhead irrigation."
    }
}


# NAVIGATION CALLBACK
def go_to_detection():
    st.session_state["Navigation"] = "Disease Detection"


# FORMAT LABEL
def friendly_label(label):
    return label.replace("___", " - ").replace("_", " ").title()


# CLASSIFY DISEASE CATEGORY
def classify_bucket(label):
    x = label.lower()

    if "healthy" in x:
        return "healthy"
    elif "early blight" in x or "early_blight" in x:
        return "early_blight"
    elif "late blight" in x or "late_blight" in x:
        return "late_blight"
    elif "leaf mold" in x or "leaf_mold" in x:
        return "leaf_mold"
    elif "bacterial" in x:
        return "bacterial"
    elif "rust" in x:
        return "rust"
    elif "mildew" in x:
        return "mildew"
    else:
        return "spot"


# LOAD PRETRAINED AI MODEL
@st.cache_resource
def load_model():
    from transformers import pipeline

    classifier = pipeline(
        "image-classification",
        model=MODEL_ID,
        revision="v1.0"
    )

    return classifier


# SAVE DETECTION HISTORY
def save_history(label, score):
    os.makedirs("data", exist_ok=True)

    record = pd.DataFrame([{
        "date_time": datetime.datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        ),
        "crop_disease": label,
        "confidence_percent": round(score * 100, 2)
    }])

    if os.path.exists(HISTORY_FILE):
        record.to_csv(
            HISTORY_FILE,
            mode="a",
            header=False,
            index=False
        )
    else:
        record.to_csv(HISTORY_FILE, index=False)


# SIDEBAR
st.sidebar.title("🌱 AgriSmart AI")

page = st.sidebar.radio(
    "Navigation",
    [
        "Home",
        "Disease Detection",
        "AI Farming Assistant",
        "Detection History",
        "About Project"
    ],
    key="Navigation"
)

st.sidebar.caption("AI Powered Agriculture Platform")
st.sidebar.info(
    "Upload a clear photograph of a single plant leaf."
)


# ==========================================
# HOME PAGE
# ==========================================

if page == "Home":

    st.title("🌱 AgriSmart AI")
    st.subheader("Smart Agriculture Assistant")

    st.write(
        "AI-powered plant disease screening "
        "and farmer guidance platform."
    )

    c1, c2, c3 = st.columns(3)

    c1.metric("AI Model", "MobileNetV2")
    c2.metric("Supported Classes", "38")
    c3.metric("Platform", "Web Application")

    st.markdown("---")

    st.header("What Can This Application Do?")

    st.markdown("""
    - 🌿 Plant Disease Detection
    - 🔬 AI Image Classification
    - 💡 Treatment Recommendations
    - 🤖 AI Farming Assistant
    - 📊 Detection History
    - 📈 Agriculture Analytics
    """)

    st.warning(
        "This application provides educational screening. "
        "AI predictions are not confirmed diagnoses."
    )

    st.button(
        "Go to Disease Detection",
        type="primary",
        on_click=go_to_detection
    )


# ==========================================
# DISEASE DETECTION
# ==========================================

elif page == "Disease Detection":

    st.title("🔬 Plant Disease Detection")

    st.write(
        "Upload a plant leaf image to identify "
        "possible crop diseases."
    )

    uploaded = st.file_uploader(
        "Upload Leaf Image",
        type=["jpg", "jpeg", "png"]
    )

    if uploaded is not None:

        try:
            image = Image.open(uploaded).convert("RGB")

            st.image(
                image,
                caption="Uploaded Plant Image",
                width=380
            )

            if st.button("Analyze Image", type="primary"):

                try:
                    classifier = load_model()

                    with st.spinner(
                        "AI is analyzing your plant image..."
                    ):
                        predictions = classifier(
                            image,
                            top_k=3
                        )

                    top = predictions[0]

                    label = top["label"]
                    score = float(top["score"])

                    save_history(label, score)

                    st.success("AI Analysis Completed!")

                    st.metric(
                        "Predicted Disease",
                        friendly_label(label),
                        f"{score * 100:.2f}% Confidence"
                    )

                    if score < 0.50:
                        st.warning(
                            "Low confidence. Upload a clearer image "
                            "and seek expert confirmation."
                        )
                    else:
                        st.info(
                            "Likely classification identified. "
                            "This is not a confirmed diagnosis."
                        )

                    bucket = classify_bucket(label)
                    info = DISEASE_INFO[bucket]

                    st.markdown("---")

                    st.header(info["title"])

                    st.write(
                        "**Possible Symptoms:**",
                        info["symptoms"]
                    )

                    st.write(
                        "**Recommended Next Steps:**",
                        info["action"]
                    )

                    st.markdown("---")
                    st.subheader("Top 3 AI Predictions")

                    for prediction in predictions:

                        st.write(
                            f"**{friendly_label(prediction['label'])}**"
                        )

                        st.progress(
                            float(prediction["score"])
                        )

                        st.write(
                            f"{prediction['score'] * 100:.2f}%"
                        )

                except Exception as error:

                    st.error(
                        "AI model could not load. "
                        "Check internet and installed packages."
                    )

                    st.exception(error)

        except Exception as error:

            st.error("Invalid image file.")
            st.exception(error)

    else:

        st.info(
            "Please upload a clear JPG or PNG plant leaf image."
        )


# ==========================================
# AI FARMING ASSISTANT
# ==========================================

elif page == "AI Farming Assistant":

    st.title("🤖 AI Farming Assistant")

    st.write(
        "Ask questions about irrigation, crop diseases, "
        "plant health and farming."
    )

    question = st.text_area(
        "Enter Your Question",
        placeholder="How can I protect tomato plants from fungal disease?"
    )

    if st.button("Get Guidance", type="primary"):

        if not question.strip():

            st.warning("Please enter a question.")

        else:

            q = question.lower()
            answers = []

            if any(w in q for w in [
                "water", "irrigation", "pani", "watering"
            ]):

                answers.append(
                    "Water near the soil rather than over leaves. "
                    "Avoid waterlogging."
                )

            if any(w in q for w in [
                "fung", "mold", "mildew", "blight"
            ]):

                answers.append(
                    "Improve plant spacing and airflow. "
                    "Avoid prolonged leaf wetness."
                )

            if any(w in q for w in [
                "yellow", "yellowing"
            ]):

                answers.append(
                    "Yellow leaves may indicate nutrient deficiency, "
                    "watering problems, pests or disease."
                )

            if any(w in q for w in [
                "pest", "insect"
            ]):

                answers.append(
                    "Inspect both sides of leaves and identify "
                    "the pest before selecting a control method."
                )

            if any(w in q for w in [
                "tomato"
            ]):

                answers.append(
                    "For tomato crops, maintain proper spacing, "
                    "remove diseased debris and avoid wetting foliage."
                )

            if any(w in q for w in [
                "fertilizer", "fertil", "nutrient"
            ]):

                answers.append(
                    "Use soil testing and crop requirements "
                    "to guide fertilizer application."
                )

            if not answers:

                answers.append(
                    "Please identify the crop, its growth stage, "
                    "visible symptoms and watering conditions. "
                    "You can also upload a leaf image for AI screening."
                )

            st.subheader("Assistant Response")

            st.success(" ".join(answers))

    st.info(
        "This version uses a built-in agriculture knowledge base "
        "for question answering. The plant disease classifier "
        "uses a pretrained deep-learning model."
    )


# ==========================================
# DETECTION HISTORY
# ==========================================

elif page == "Detection History":

    st.title("📊 Detection History")

    if os.path.exists(HISTORY_FILE):

        df = pd.read_csv(HISTORY_FILE)

        st.dataframe(
            df,
            use_container_width=True
        )

        st.metric(
            "Total Scans",
            len(df)
        )

        if st.button("Clear History"):

            os.remove(HISTORY_FILE)

            st.success("History cleared successfully.")

            st.rerun()

    else:

        st.info(
            "No detection records found. "
            "Analyze a leaf image first."
        )


# ==========================================
# ABOUT PROJECT
# ==========================================

elif page == "About Project":

    st.title("About AgriSmart AI")

    st.markdown("""
    ### Project Overview

    AgriSmart AI is an AI-powered Smart Agriculture Assistant.

    ### Problem Statement

    Plant diseases can reduce agricultural production.
    Early identification can help farmers seek advice sooner.

    ### Proposed Solution

    A web application that analyzes plant leaf images
    using a pretrained deep-learning model.

    ### AI Technology

    - MobileNetV2
    - Deep Learning
    - Computer Vision
    - PlantVillage Dataset

    ### Technology Stack

    - Python
    - Streamlit
    - PyTorch
    - Hugging Face Transformers
    - Pandas
    - Pillow

    ### Future Scope

    - Hindi Voice Assistant
    - Weather Integration
    - Soil Analysis
    - Regional Crop Recommendations
    - Generative AI Integration
    """)

    st.markdown("---")

    st.write("**Developer:** Anash Rahman")
    st.write("**College:** Jamia Hamdard University, New Delhi")
    st.write("**Department:** Computer Science & Engineering")
