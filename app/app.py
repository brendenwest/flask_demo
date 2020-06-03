from flask import Flask, request
app = Flask(__name__)

@app.route('/')
def hello_world():
   return 'Ahoy there matey'

@app.route('/predict', methods=['POST'])
def make_prediction():
   data = request.get_json()
   return "you posted {0}".format(data['message'])

if __name__ == '__main__':
   app.run(host='0.0.0.0')
