# Weather-App

# Weather Checker

Welcome to the **Weather Checker** project! This sample application demonstrates how to build a simple frontend user interface (UI) and a backend microservice to retrieve current weather information from an external weather API (in this case, [Open-Meteo](https://open-meteo.com/)).

## Table of Contents

1. [Overview](#overview)  
2. [Features](#features)  
3. [Project Structure](#project-structure)  
4. [Setup and Installation](#setup-and-installation)  
5. [Running the Application](#running-the-application)  
6. [Best Practices Highlighted](#best-practices-highlighted)  
7. [How It Works (Simple Explanation)](#how-it-works-simple-explanation)  

---

## Overview

- **Frontend (UI)**: A basic HTML and JavaScript page that allows users to enter a ZIP code and see the current weather.
- **Backend (Microservice)**: A Python Flask app that receives the ZIP code, calls a weather API to retrieve current conditions, and sends the results back to the frontend.

This project demonstrates how to structure a small production-ready application, including **error handling**, **logging**, and **validation**.

---

## Features

1. **Enter ZIP Code**: A text box where the user can enter a ZIP code (e.g., 12345).
2. **Get Weather**: A button that, when clicked, sends the ZIP code to the microservice.
3. **Weather Response**: Displays the current temperature, basic condition (e.g., sunny, cloudy), and wind speed.
4. **Error Handling**: If something goes wrong (invalid ZIP code, server error, etc.), the app displays a friendly message.
5. **Logging**: The microservice logs important events and errors for easier troubleshooting.

---

## Project Structure

    weather-checker/
    ├── frontend/
    │   ├── index.html
    │   └── app.js
    └── backend/
        ├── app.py
        └── requirements.txt

- **frontend/**  
  - **index.html**: The main UI with an input field and button.  
  - **app.js**: The JavaScript logic to handle button clicks, make requests to the backend, and display results.

- **backend/**  
  - **app.py**: The Flask microservice that fetches weather data from an external API.  
  - **requirements.txt**: A list of Python dependencies (Flask, requests, etc.).

Feel free to structure the project however you prefer. You can rename folders or combine files as needed.

---

## Setup and Installation

1. **Clone This Repository** or download it as a ZIP.
2. **Install Python** (3.7+ recommended).

### Python Libraries

From within the `backend/` directory (or the project root if you have a consolidated `requirements.txt`), run:

```bash
pip install -r requirements.txt
```

This will install:
- **Flask** (a Python web framework)  
- **requests** (for making HTTP requests)

---

## Running the Application

1. **Start the Backend Microservice**  
   Navigate to the `backend/` folder in your terminal:

   ```bash
   python app.py
   ```
   By default, it will run on `http://localhost:3000`.

2. **Open the Frontend**  
   - Navigate to the `frontend/` folder.  
   - Open **index.html** in your web browser (e.g., double-click or open with your browser).  

3. **Use the Application**  
   - Enter a ZIP code (e.g., `12345`) into the text box.  
   - Click **Get Weather**.  
   - The current weather information is displayed below the button.

---

## Best Practices Highlighted

1. **Error Handling**:  
   - The frontend checks if the user typed a ZIP code.  
   - The backend wraps calls in a `try/except` block to catch unexpected issues.  

2. **Logging**:  
   - Flask’s built-in logging (`app.logger`) is used to record important events and errors.

3. **Response Codes**:  
   - **`400 Bad Request`** if the ZIP code is missing or invalid.  
   - **`500 Internal Server Error`** if there’s an exception on the server.

4. **Separation of Concerns**:  
   - The frontend only handles user interaction.  
   - The backend microservice handles all communication with the external weather API.

5. **Production-Ready Extras** (not fully shown, but recommended):  
   - Use **HTTPS** in real-world deployments.  
   - **Validate** ZIP codes on the server side.  
   - Use **caching** to improve performance.  
   - Use a proper **geocoding service** to convert ZIP codes to latitude/longitude.

---

## How It Works (Simple Explanation)

1. **User Interface**: You type your ZIP code into a box and click “Get Weather.”  
2. **Microservice Request**: The webpage sends your ZIP code to our Python server (the microservice).  
3. **Weather API Call**: The microservice uses the ZIP code to find the location’s latitude/longitude (for example, via a geocoding service or a basic lookup).  
4. **Current Weather**: The microservice contacts the **Open-Meteo** API to get the latest weather.  
5. **Response**: The Python server sends back the weather info (temperature, condition, etc.) as simple text.  
6. **Display**: The webpage shows you the result (e.g., “It’s 72°F and Partly Cloudy!”).

---

**Thank you for checking out this project!** Feel free to customize, improve, or extend it for your own needs. If you have any questions or run into issues, please reach out or open an issue on the repository. Enjoy your Weather Checker!