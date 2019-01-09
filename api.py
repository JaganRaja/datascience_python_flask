print("Jakkamma")

import flask

app = flask.Flask(__name__)
#Creates the Flask application object, which contains data about the application and 
#also methods (object functions) that tell the application to do certain actions
app.config["DEBUG"] = True 
#Starts the debugger. With this line, if your code is malformed, you’ll see an error when you visit your app. 
#Otherwise you’ll only see a generic message such as Bad Gateway in the browser when there’s a problem with 
#your code.


@app.route('/', methods=['GET'])
def home():
    return "<h1>Distant Reading Archive</h1><p>This site is a prototype API for distant reading of science fiction novels</p>"

app.run()
#A method that runs the application server.