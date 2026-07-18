from flask import Flask,request,jsonify,render_template
from chatbot import get_response

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat",methods=["POST"])
def chat():

    message = request.json["message"]

    answer = get_response(message)

    return jsonify({
        "response":answer
    })

if __name__=="__main__":
    app.run(debug=True)
    

'''from flask import Flask, request, jsonify, render_template
from openai import OpenAI
import os

app = Flask(__name__)

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():

    message = request.json["message"]

    response = client.responses.create(
        model="gpt-5.5",
        input=message
    )

    return jsonify({
        "response": response.output_text
    })

if __name__ == "__main__":
    app.run(debug=True)
'''