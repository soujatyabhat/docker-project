import random

from flask import Flask, jsonify

#Global Decleartion
alpha = [d for d in "abcdefghijklmnopqrstuvwxyz"]
non_alpha = [d for d in "!#$%&'()*+,-./:;<=>?@[\]^_`{|}~"]

#Random Password Generator
def password_gen(char_range,nonChar_range,digit_range):
    password = ''
    
    for i in range(0,char_range):
        pick = random.randrange(1,nonChar_range)
        password = password  + ''.join(str(alpha[pick]))
    for i in range(0,nonChar_range):
        pick = random.randrange(0,len(non_alpha))
        password = password  + ''.join(non_alpha[pick])
    digit = random.randrange(1,digit_range)
    password = password + str(digit)

    return password

# Create an instance of the Flask class
app = Flask(__name__)

# Define a route and its corresponding request handler
@app.route("/")
def home():
    return "True"

@app.route("/passtype/<string:tye>")
def output(tye):
    data = ""
    if tye == "easy":
        data= password_gen(3,5,7000)
    elif tye == "medium":
        data= password_gen(5,7,9000)
    elif tye == "hard":
        data = password_gen(7,9,11000)
    return jsonify({
        "passType": tye,
        "value": data})

# Run the application
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
