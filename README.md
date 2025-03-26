# Regression Model API - README

## 📌 Project Overview
This project provides a publicly available API endpoint that returns predictions based on given input values. The API is built using FastAPI and is accessible via a deployed web service, which can be tested using Swagger UI.

## 🌐 Public API Endpoint
You can access the API documentation and test the endpoint using Swagger UI here:
[Regression Model API Docs](https://regression-summative.onrender.com/docs)

## 🎥 Demo Video
Watch the quick demo (max 2 minutes) on YouTube:
[Demo Video Link] https://drive.google.com/file/d/1du1V5CY67rZ9qk4_ADu6sOsemkoacxCH/view?usp=sharing

## Running the Mobile App
Follow these steps to run the mobile app and interact with the API:

1. Clone the Repository:
   ```sh
   git clone <repository-url>
   cd <project-folder>
   ```

2. Install Dependencies:
   If using Flutter:
   ```sh
   flutter pub get
   ```
   If using React Native:
   ```sh
   npm install
   ```

3. Set API Endpoint:
   - Locate the API configuration file (e.g., `config.dart` in Flutter or `.env` in React Native).
   - Update the API URL:
     ```sh
     API_BASE_URL=https://regression-summative.onrender.com/docs
     ```

4. **Run the App:**
   - For Flutter:
     ```sh
     flutter run
     ```
   - For React Native:
     ```sh
     npx react-native run-android  # Android
     npx react-native run-ios  # iOS
     ```

## Features
- Predictive modeling via FastAPI.
- Publicly accessible endpoint for real-time inference.
- Mobile app integration for seamless predictions.



