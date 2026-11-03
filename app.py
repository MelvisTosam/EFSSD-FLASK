# this code imports the flask library and some functions from it.
from flask import Flask, render_template

#create a flask application instance
app = Flask(__name__)

# Routes 
# They define which template is loaded, or action taken, depending on the URL requested
#===========
# Home page
@app.route("/")
def index():
    # It defines a variable "studentname" that will be passed to the output html
    studentName = "Melvis"
    # Render HTML with the name in H1 tag
    return f"<h1>Hello, {studentName}!</h1>"

# Run application
#==================
# This code executes when the script is run directly
if __name__ == "__main__":
    print("Starting Flask application..")
    print("Open Your Application in Your Browser: http://localhost:81")
    # The app will run on port 81, accessible from any local IP address
    app.run(host='0.0.0.0', port=81, debug=True)

# About Page
@app.route('/about <name>')
def aboutName(name):
    # Render HTML with the name in a H1 tag
    return render_template("index.html",greeting="Welcome", username=studentName)
