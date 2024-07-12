"""
    Web Application Development with Flask
    https://flask.palletsprojects.com/en/3.0.x/

    1. Install Flask in Virtual Env
       pip install Flask

    2. Create Object of Flask

    3. Create a Function, with route as /

    4. In main function run the Flas App using run()

    5. Return the HTML webapge as a template from function
"""

from flask import *
import datetime
import hashlib

# Create the Object of Flask
# Which represents a Web Application
web_app = Flask("Doctors App")

@web_app.route("/") # Decorator
def index():
    # message = "Welcome to Patient Management System. Its {}".format(datetime.datetime.now())

    # message copied form index.html
    # can return plain text or can return HTML
    message = """
<html>
    <head>
        <title>Doctors App</title>
    </head>
    <body>
        <center>
            <h3>Doctors App</h3>
        </center>
    </body>
</html>"""
    # return message
    
    # render_template is used to return web pages(html)
    return render_template("index.html")

@web_app.route("/register")
def register():
    return render_template("register.html")

@web_app.route("/add-user", methods=["POST"])
def add_user_in_db():
    # Create a dictionary with data from HTML register form

    
    user_data = {
        "name": request.form["name"],
        "email": request.form["email"],
        "password": hashlib.sha256(request.form["password"].encode('utf-8')).hexdigest(),
        "created_on": datetime.datetime.now()
    }

    # Save data in MongoDB

    message = "Welcome to Home Page. Data is: {name}, {email}, {password}, {created_on}".format_map(user_data)
    return message
def main():
    # Run the app infinitely, till the user quits
    web_app.run()
    # web_app.run(port=5001) # Optionally you can give the port number


if __name__ == "__main__":
    main()