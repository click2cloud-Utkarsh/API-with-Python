from asyncio.windows_events import NULL
from flask import Flask, escape, render_template, url_for

app = Flask(__name__)

# @app.route("/hello/<name>", methods=['POST'])
# def hello(name=None):
#     return render_template('home.html', name=name)

# @app.route("/number/<int:n>")
# def hello_world(n):
#     return f"You entered, {escape(n)} !"


@app.route("/")
def home():
    return render_template('home.html')

@app.route("/about")
def about():
    return render_template('about.html')
  
@app.route("/contact")
def contact():
    return render_template('contact.html')



if __name__== "__main__":
  app.run(debug=True)

# with app.test_request_context():
#   print(url_for('hello',name='Utkarsh Nigam'))
#   print(url_for('hello',name='Nigam'))
#   print(url_for('hello',name='XYZ'))
#   print(url_for('hello_world',n=123))