from flask import Flask

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
	return ("Flask is complete!!!! Yay!")

if __name__ == '__main__':
	app.run(debug=True, port=3000)