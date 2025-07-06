from flask import Flask, render_template, request
import joblib
import datetime

# Flask app
app = Flask(__name__)

# Load model from Desktop
model = joblib.load(r'C:\Users\prasa\OneDrive\Desktop\petrol_price_model.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        year = int(request.form['year'])
        current_year = datetime.datetime.now().year

        if year < 2000 or year > 2039:
            return render_template('index.html', prediction_text="⚠️ Please enter a year between 2000 and 2039.")
        
        prediction = model.predict([[year]])
        price = round(prediction[0], 2)
        return render_template('index.html', prediction_text=f"Predicted Petrol Price in {year} is ₹{price} per liter")

    except ValueError:
        return render_template('index.html', prediction_text="⚠️ Please enter a valid numeric year.")
    except Exception as e:
        return render_template('index.html', prediction_text=f"⚠️ Error: {str(e)}")

if __name__ == '__main__':
    app.run(debug=True)
