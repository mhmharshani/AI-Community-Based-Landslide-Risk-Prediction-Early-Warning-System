# AI+Community-Based-Landslide-Risk-Prediction-Early-Warning-System

AI-based landslide risk prediction system for Sri Lanka, starting as an MVP with environmental data and evolving into a full platform with community reporting, explainable AI, and offline support.

## Overview

The software solution is an intelligent landslide risk prediction system designed specifically for Sri Lanka. It combines geotechnical knowledge with machine learning to support early warning and decision-making in landslide-prone areas.

The project is developed in two stages:

* **MVP (Minimum Viable Product):** A simple system that predicts landslide risk based on environmental inputs.
* **Final System (Planned):** A full-featured platform integrating community reporting, explainable AI, and offline capabilities.

---

## MVP Features (Current)

* Landslide risk prediction using:

  * Rainfall
  * Slope
  * Soil type
* Machine Learning model (Random Forest)
* Simple web interface for input/output
* Risk levels: Low / Medium / High
* Basic explanation of key factors

---

## Planned Final Features

* Interactive map-based dashboard
* Community reporting (cracks, seepage, slope movement)
* Hybrid risk fusion (AI + community data)
* Explainable AI (feature importance)
* Actionable recommendations
* Offline mode (data caching + sync)
* Scalable backend with database

---

## Tech Stack

### MVP

* Frontend: React
* Backend: FastAPI
* ML: Scikit-learn

### Final System (Planned)

* Maps: Leaflet
* Explainability: SHAP
* Database: PostgreSQL
* Deployment: Vercel + Render

---

## System Architecture

### MVP Flow

User → Input Data → ML Model → Risk Output → Basic Explanation

### Final System Flow

Environmental Data + Community Reports → ML Model → Risk Fusion → Explainability → Dashboard + Alerts

---

## Project Motivation

This project was inspired by recent extreme weather events in Sri Lanka, including the impacts of the Ditwa cyclone, which resulted in landslides and the loss of valuable lives. These events highlight the urgent need for more accessible, intelligent, and localized early warning systems. Hence, There is a need for a user-centric landslide risk prediction and decision support platform.
Existing landslide warning systems in Sri Lanka are mostly centralized and lack user interaction, explainability, and community involvement. This project aims to bridge that gap by creating a user-centric, intelligent system for better situational awareness and safer decision-making. 

---

## Future Scope

* Integration with real-time weather APIs
* Mobile application development
* Continuous learning from user feedback
* Expansion to other natural hazards

---

## Author

Individual Software Engineering Project

---

## Disclaimer

This project is developed for academic and research purposes. It should not be used as the sole source for real-world disaster decisions without validation from official authorities.

---
