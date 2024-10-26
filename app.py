# import modules
from imports import *

# Load trained model (Pickle)
data = pickle.load(open('data.pkl', 'rb'))
training_data_len = pickle.load(open('training_data_len.pkl', 'rb'))
scaler = pickle.load(open('scaler.pkl', 'rb'))
scaled_data = pickle.load(open('scaled_data.pkl', 'rb'))
model_1 = pickle.load(open('model_1.pkl', 'rb'))
predictions_1 = pickle.load(open('predictions_1.pkl', 'rb'))

app = Flask(__name__)

# Route for homepage
@app.route('/')
def home():
    start_index = len(data) - 60
    input_sequence = scaled_data[start_index:].tolist()
    future_days = 5
    future_predictions = []

    for _ in range(future_days):
        pred = model_1.predict(np.array(input_sequence[-60:]).reshape(1, 60, 1))
        future_predictions.append(pred[0, 0])
        input_sequence.append(pred[0])

    future_predictions = scaler.inverse_transform(np.array(future_predictions).reshape(-1, 1))

    future_dates = pd.date_range(data.index[-1], periods=future_days + 1)[1:]
    future_data = list(zip(future_dates.strftime('%Y-%m-%d'), future_predictions.flatten()))

    # Pass future_data to the template
    return render_template('index.html', future_predictions=future_data)

# Route for homepage
@app.route('/plot')
def plot():
    train = data[:training_data_len]
    valid_1 = data[training_data_len:]
    valid_1['Predictions'] = predictions_1

    # Compute future predictions
    start_index = len(data) - 60
    input_sequence = scaled_data[start_index:].tolist()
    future_days = 5
    future_predictions = []

    for _ in range(future_days):
        pred = model_1.predict(np.array(input_sequence[-60:]).reshape(1, 60, 1))
        future_predictions.append(pred[0, 0])
        input_sequence.append(pred[0])

    future_predictions = scaler.inverse_transform(np.array(future_predictions).reshape(-1, 1))
    future_dates = pd.date_range(data.index[-1], periods=future_days + 1)[1:]
    future_df = pd.DataFrame(future_predictions, index=future_dates, columns=['Predictions'])

    # Plot
    plt.figure(figsize=(14, 10))
    plt.title('Bitcoin Price Prediction')
    plt.xlabel('Date', fontsize=18)
    plt.ylabel('Close Price USD', fontsize=18)
    plt.plot(train['Close'], label='Train')
    plt.plot(valid_1[['Close', 'Predictions']], label='Validation')
    plt.plot(future_df['Predictions'], linestyle='--', label='Future Predictions')
    plt.legend(['Train', 'Validation', 'Predictions', 'Future Predictions'], loc='upper left')

    # Return plot as an image
    img = BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    return send_file(img, mimetype='image/png')


if __name__ == "__main__":
    app.run(debug=True)
