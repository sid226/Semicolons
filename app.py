from flask import Flask  
from Routes.slides import app_routes
  
app = Flask(__name__) #creating the Flask class object   
app.register_blueprint(app_routes)


if __name__ =='__main__':  
    app.run(debug = True)  