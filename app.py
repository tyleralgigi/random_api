from flask import Flask, jsonify
from random import choice, randint
import os
import json

# Initialize the Flask app
app = Flask(__name__)

# Sample prompts for crimes and work (replace with your full dataset)
prompts_file = os.path.abspath(os.path.dirname(__file__)) + '/data/simulation_crime_prompts.json'
f = open(prompts_file)
# returns JSON object as a dictionary
crime_prompts = json.load(f)
f.close()

prompts_file = os.path.abspath(os.path.dirname(__file__)) + '/data/simulation_work_prompts.json'
f = open(prompts_file)
# returns JSON object as a dictionary
work_prompts = json.load(f)
f.close()


# Route for getting a random crime prompt
@app.route('/random_crime', methods=['GET'])
def get_random_crime():
    random_crime_prompt = choice(crime_prompts)
    coins = randint(-1000, 1000)
    return jsonify(
        {
            "prompt": random_crime_prompt,
            "coins": coins
        }   
    )

# Route for getting a random work prompt
@app.route('/random_work', methods=['GET'])
def get_random_work():
    random_work_prompt = choice(work_prompts)
    coins = randint(1, 1000)
    return jsonify(
        {
            "prompt": random_work_prompt,
            "coins": coins
        }   
    )

# Start the Flask app
if __name__ == '__main__':
    app.run(debug=True)
