from flask import Flask

app = Flask(__name__)  #Instance of the Flask application
                        #Flask uses this locate resources and tempaltes.
                        

@app.route("/")
def home():
    return "Hello from Flask!!"  #This says whenevr you put up the URL "/", we have to call the function home()


if __name__ == "__main__":
    app.run(debug=True) #Run the Flask server
    
