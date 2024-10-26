
# Bitcoin Price Prediction

This project is a Bitcoin price prediction model built using an LSTM neural network, with a web interface powered by Flask for real-time predictions.

## Table of Contents
- [Overview](#overview)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Technologies](#technologies)

## Overview

The Bitcoin Price Prediction project leverages machine learning to forecast Bitcoin prices based on historical data. The model uses an LSTM (Long Short-Term Memory) network due to its effectiveness with time series data. The project also includes a web interface to view predictions in real-time, hosted locally through Flask.

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/malayashekhar/Bitcoin-Price-Prediction.git
   cd Bitcoin-Price-Prediction
   ```

2. **Install dependencies:**
   Ensure you have Python installed, then install all dependencies from `requirements.txt`.
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Run the Notebook:**
   Open and execute all cells in the `.ipynb` notebook to train and test the model.
   ```bash
   jupyter notebook Bitcoin_Price_Prediction.ipynb
   ```

2. **Start the Flask App:**
   After training the model, start the Flask server to access the web interface:
   ```bash
   python app.py
   ```

3. **View the Web Interface:**
   Open your browser and navigate to `http://localhost:5000` to view real-time predictions.

## Project Structure

- `Bitcoin_Price_Prediction.ipynb` - Jupyter notebook containing the LSTM model training code.
- `app.py` - Flask application file for hosting the web interface.
- `requirements.txt` - List of project dependencies.

## Technologies

- Python
- Flask
- Jupyter Notebook
- LSTM Neural Network
