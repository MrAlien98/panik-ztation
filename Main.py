from flask import Flask, redirect, url_for, render_template, request, flash

app=Flask(__name__)


@app.route("/")
def home():
	return "First commit"

if __name__ == "__main__":
	app.run(debug=True)