from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
	return "Hello World!"

@app.route("/devops")
def devops():
	return "Hello, DevOps"

if __name__ == "__main__":
	app.run(debug=True,host="0.0.0.0",port=5000)
