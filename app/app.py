from flask import Flask, request, render_template, jsonify
app = Flask(__name__)

@app.route('/')
def index():
   greeting = 'Ahoy there matey'
   return render_template('home.html', greeting = greeting)

@app.route('/predict', methods=['POST'])
def make_prediction():
   # get JSON payload from client
   data = request.get_json()
   print("you posted {0}".format(data['entry']))

   # send a JSON response to the client
   return jsonify(response="I am sorry! I don't understand you")

if __name__ == '__main__':
   app.run(host='0.0.0.0')
