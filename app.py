from flask import Flask, request, render_template
from textblob import TextBlob

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        review = request.form['review']
        analysis = TextBlob(review)
        sentiment = 'Positive' if analysis.sentiment.polarity > 0 else 'Negative'
        return render_template('pred.html', sentiment=sentiment, review=review)

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)