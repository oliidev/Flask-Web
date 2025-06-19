from flask import Flask, render_template
import random

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/home')
def homepage():
  return render_template("home.html")

@app.route('/menu')
def menu():
  return render_template("menu.html")

@app.route('/rewards')
def rewards():
  return render_template("rewards.html")

@app.route('/about')
def about():
  return render_template("about.html")

@app.route('/contact')
def contact():
  return render_template("contact.html")

@app.route('/order')
def order():
  return render_template("order.html")



if __name__ == '__main__':
  app.run()
