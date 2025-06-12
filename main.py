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

@app.route('/landingpage')
def landingpage():
  return render_template("landingpage.html")


if __name__ == '__main__':
  app.run()