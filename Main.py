from flask import Flask, redirect, url_for, render_template, request, flash

app=Flask(__name__)


@app.route("/")
def home():
	return render_template('home.html')

@app.route("/order/")
def order():
	return render_template('order.html')

@app.route("/product_design/")
def product_design():
	return render_template('order.html')

if __name__ == "__main__":
	app.run(debug=True)