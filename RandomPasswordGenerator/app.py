from flask import Flask, render_template, request

app = Flask(__name__)

# Function to generate a random password
import random
import string

def generate_Random_Password(PassLength, uppercase, lowercase, numbers, symbols):
    Pass = " ";
    
    # Add character sets based on user selection
    if uppercase:
        Pass += string.ascii_uppercase
    if lowercase:
        Pass += string.ascii_lowercase
    if numbers:
        Pass += string.digits
    if symbols:
        Pass += string.punctuation
    
    # If no character sets are selected, return an empty string
    if not Pass:
        return " "
    
    # Generate a random password
    PasswordGen = ''.join(random.choice(Pass) for _ in range(PassLength))
    
    return PasswordGen

# Route to serve the HTML page and handle form submission
@app.route('/', methods=['GET', 'POST'])
def index():
    Password = " ";
    if request.method == 'POST':
        # Get form data
        PassLength = int(request.form['length'])
        uppercase = 'uppercase' in request.form
        lowercase = 'lowercase' in request.form
        numbers = 'numbers' in request.form
        symbols = 'symbols' in request.form

        # Generate the password
        Password = generate_Random_Password(PassLength, uppercase, lowercase, numbers, symbols)

    return render_template('index.html', Password=Password);

if __name__ == '__main__':
    app.run(debug=True)