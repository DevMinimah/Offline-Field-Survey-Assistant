# Offline-Field-Survey-Assistant
A 100% local-first, offline AI application for analyzing environmental field images without cloud dependency. Built for data sovereignty in zero-connectivity environments.



# 🌿 Offline Field Survey Assistant (EcoSurvey AI)

A 100% local-first, offline AI application that analyzes environmental field images — flora, soil, vegetation health — and generates structured field reports with **zero cloud dependency** Built for data sovereignty in zero-connectivity environments.

## 🎯 Project Overview
Designed for remote and zero-connectivity environments (e.g., Niger Delta field stations), this tool lets field researchers analyze sensitive ecological imagery without internet access, cloud APIs, or subscription costs. All inference runs on the local device, ensuring complete data sovereignty.

## 🧠 How It Works: Multi-Pass Inference Pipeline
Lightweight edge vision models struggle with complex multi-part prompts. Instead of one large instruction, this app issues **three single-intent queries** to the local model (subject identification → condition assessment → action recommendation), then programmatically assembles the structured Markdown report client-side. This design maximizes output quality on sub-2GB edge models.

## 🛠 Tech Stack
- **Frontend:** Streamlit (Python)
- **Local Vision Engine:** Ollama running `moondream` (lightweight edge vision model)
- **Architecture:** Localhost HTTP API — fully air-gapped

## 🚀 How to Run Locally
1. Install [Ollama](https://ollama.com) and pull the model: `ollama pull moondream`
2. Install dependencies: `python -m pip install streamlit requests pillow`
3. Run the app: `python -m streamlit run field_survey_app.py`
4. **Air-gap verification:** Disconnect Wi-Fi — the app still functions fully offline.

## 🎯 Design Philosophy & Honest Scoping
Positioned as a **rapid field-triage tool**, not a replacement for laboratory taxonomic verification. Deliberately optimized for 4GB RAM hardware so that privacy-preserving AI is accessible to researchers in resource-constrained regions, regardless of hardware budget.

## 🔮 Planned Improvements
- EXIF/GPS metadata extraction for geo-tagged reports
- Burn-severity scoring module for post-fire assessment
- Offline species reference database for identification validation
- Support for larger vision models on higher-spec hardware

## 🎓 Academic & Professional Context
This project builds on my experience developing **Niger Delta Sentinel** (deforestation tracking) and **EnvoShield** (secure GIS whistleblower portal), and applies concepts from my **IBM SkillsBuild** and **TS Academy Cybersecurity** training. It forms a foundational prototype for my planned **Digital Forensics for Environmental Crimes** toolkit, supporting my objectives of protecting the environmentent (Nature, Society and Environmental Governance)**.
