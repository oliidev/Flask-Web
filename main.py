from flask import Flask, render_template
import random

app = Flask(__name__)
app.config['DEBUG'] = True

# @app.route('/')
# def hello():
#   page = """
#     <h1>Here's a random number: {0}</h1>
#     <form>
#       <button>New Number</button>
#     </form>
#   """
#
#   num = random.randint(1, 25)  # Select a random integer from 1 - 25.
#   return page.format(num)
#
# @app.route('/goodbye')
# def goodbye():
#   message = "<h2>This is the second page!</h2>"
#   return message
#
# @app.route('/form')
# def form():
#   return render_template("index.html")
#
# @app.route('/another')
# def anotherone():
#   return render_template("another.html")
#
# @app.route('/thanks')
# def thanks():
#   person = "Bob"
#   action = "dancing"
#   return render_template("tynote.html", name=person, verb=action)

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