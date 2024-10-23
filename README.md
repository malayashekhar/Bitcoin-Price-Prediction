# Bitcoin Price Prediction Model

## Overview
This project implements a machine learning model to predict Bitcoin prices using historical price data. The model utilizes time series analysis and LSTM (Long Short-Term Memory) neural networks to forecast future Bitcoin price movements.

## Features
- Historical Bitcoin price data analysis
- Time series preprocessing and feature engineering
- LSTM neural network implementation
- Price prediction visualization
- Model performance evaluation

## Dependencies
```
pandas
numpy
sklearn
tensorflow
matplotlib
seaborn
yfinance
```

## Installation
1. Clone the repository:
```bash
git clone https://github.com/malayashekhar/Bitcoin-Price-Prediction.git
cd Bitcoin-Price-Prediction
```

2. Install required packages:
```bash
pip install -r requirements.txt
```

## Usage
1. Open the Jupyter notebook:
```bash
jupyter notebook "BitCoin Prediction.ipynb"
```

2. Run all cells in sequence to:
   - Load and preprocess historical Bitcoin price data
   - Train the LSTM model
   - Generate price predictions
   - Visualize results

## Model Architecture
- Input layer with time series data
- LSTM layers for sequence learning
- Dense layers for final prediction
- Optimization using Adam optimizer
- Mean Squared Error (MSE) as loss function

## Results
The model provides predictions for Bitcoin price movements based on historical patterns. Visualization includes:
- Actual vs Predicted price comparisons
- Price trend analysis
- Model performance metrics

## Limitations
- Market volatility and external factors may affect prediction accuracy
- Past performance doesn't guarantee future results
- Model requires regular retraining with new data

## Contributing
Feel free to fork the repository and submit pull requests. For major changes:
1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Open a pull request

## License
MIT License

## Contact
- GitHub: [@malayashekhar](https://github.com/malayashekhar)
