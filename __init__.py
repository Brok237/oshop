from flask import Flask
from pages import bp  

app = Flask(__name__, template_folder="template")  


app.secret_key = 'acu'  


app.register_blueprint(bp)  

if __name__ == "__main__":
    app.run(debug=True)  
