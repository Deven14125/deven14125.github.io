from flask import Flask, render_template, request,jsonify
from datetime import datetime

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    bmi = ""
    category = ""
    
    if request.method == "POST":
        try:
            # Get the data from the form
            Weight = float(request.form.get("weight"))
            Height = float(request.form.get("height"))

            if Height <= 0 or Weight <= 0:
                bmi = "Height and Weight must be greater than zero."
            else:
                # Calculate BMI
                BMI = Weight / (Height * Height)
                bmi = f"Your BMI (Body Mass Index) is: {BMI:.2f} kg/m²"

                # Determine the BMI category
                if BMI < 18.5:
                    category = "You are Underweight."
                elif BMI < 24.9:
                    category = "You are Normal Weight."
                elif BMI < 29.9:
                    category = "You are Overweight."
                else:
                    category = "You are Obese."
        except ValueError:
            bmi = "Weight And Height Must Be Greater Than Zero."
                
    return render_template("index.html", bmi=bmi, category=category)

if __name__ == "__main__":
    app.run(debug=True);