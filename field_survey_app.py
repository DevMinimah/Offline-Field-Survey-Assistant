import streamlit as st
import requests
import base64
from PIL import Image
import io

# --- CONFIGURATION ---
OLLAMA_API_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "moondream"  # Lightweight vision model for 4GB RAM

st.set_page_config(page_title="EcoSurvey AI", page_icon="🌿", layout="wide")

st.title("🌿 Offline Field Survey Assistant")
st.markdown("""
**Purpose:** Analyze environmental field images (flora, soil degradation, burn severity)
entirely offline. No cloud API, no data leakage, zero subscription cost.
""")

st.sidebar.header("System Status")
st.sidebar.success("✅ Running 100% Locally")
st.sidebar.info("🔒 Data never leaves this device")
st.sidebar.warning("📡 Try disconnecting your Wi-Fi. The app will still work!")

def ask_local_vision(img_base64, question):
    """Sends ONE simple question per call - best practice for small edge models."""
    payload = {
        "model": MODEL_NAME,
        "prompt": question,
        "images": [img_base64],
        "stream": False,
        "options": {"temperature": 0.3, "num_predict": 300}
    }
    response = requests.post(OLLAMA_API_URL, json=payload)
    response.raise_for_status()
    return response.json()["response"].strip()

# --- MAIN APP LOGIC ---
uploaded_file = st.file_uploader("Upload a field image (JPG/PNG)", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Field Image")

    if st.button("🔍 Analyze Environment (Offline)", type="primary"):
        with st.spinner("Running 3-pass local analysis on your hardware..."):
            try:
                rgb_image = image.convert("RGB")
                buffered = io.BytesIO()
                rgb_image.save(buffered, format="JPEG")
                img_base64 = base64.b64encode(buffered.getvalue()).decode('utf-8')

                # MULTI-PASS INFERENCE: one simple question per call
                subject = ask_local_vision(img_base64,
                    "Describe in detail what is visible in this environmental field image. Identify the plant type, soil, and vegetation.")

                condition = ask_local_vision(img_base64,
                    "Assess the ecological condition and health of the vegetation in this image. Mention any signs of stress, degradation, or damage.")

                action = ask_local_vision(img_base64,
                    "As an environmental scientist, recommend one action for this site: conservation, remediation, or monitoring. Explain briefly why.")

                # The app assembles the structured report itself
                report = f"""### 📊 Field Report

**1. Observed Subject**
{subject}

**2. Ecological Condition**
{condition}

**3. Recommended Action**
{action}

---
*Generated 100% offline by EcoSurvey AI (local edge model: {MODEL_NAME}).*
"""

                st.success("Analysis Complete!")
                st.markdown(report)

                st.download_button(
                    label="📥 Download Report as Text",
                    data=report,
                    file_name="field_survey_report.md",
                    mime="text/markdown"
                )

            except requests.exceptions.ConnectionError:
                st.error("❌ Local AI engine not found. Please ensure Ollama is running.")
            except Exception as e:
                st.error(f"An error occurred: {e}")