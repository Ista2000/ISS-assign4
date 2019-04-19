from flask import Flask
from .views import main
from .models import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.secret_key = 'vlabs-crypt0-exp-pkcs-1.5-iss-assign-2018-ug2k18-istasis-kishan'

app.register_blueprint(main)

db.init_app(app)

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
