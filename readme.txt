This is a super hero search application.

execute this code to start the app: python app.py

execute this code to install the requirement: pip install -r requirements.txt

web: gunicorn app:app 

first app is the name of the file. For example file name is app.py
second app is the name of the application from Flask(we start the application with this line app = Flask(__name__))