from flask import Flask, render_template

# ADJUSTMENT: import the library that will let us read environment variables
import os

app = Flask('MyHerokuApp')

mailgun_secret_key_value = None

# ADJUSTMENT: This is needed for Heroku configuration as in Heroku our
# app will porbably not run on port 5000 as Heroku will automatically
# assign a port for our application.
port = int(os.environ.get("PORT", 5000))

@app.route('/')
def index():
   
   return render_template("index.html", value=mailgun_secret_key_value)

# ADJUSTMENT: Setup our application to run with the needed port.
app.run(host='0.0.0.0', port=port, debug=True)