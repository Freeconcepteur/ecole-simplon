from flask import Flask, jsonify
import random
from time import sleep

app = Flask(__name__)

@app.route('/random_number', methods=['GET'])
def get_random_number():
    sleep(1)  # Attendez 30 secondes avant de générer un nouveau nombre
    number = random.randint(1, 6)
    return jsonify(number=number)

if __name__ == '__main__':
    app.run(debug=True)
