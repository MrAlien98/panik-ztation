from flask import Flask, redirect, url_for, render_template, request, flash

app=Flask(__name__)


@app.route("/")
def home():
	return '<h1>First commit</h1>'

if __name__ == "__main__":
	app.run(debug=True)