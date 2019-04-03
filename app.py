import os
from flask import Flask
from .views import main

app = Flask(__name__)

app.register_blueprint(main)

#current = int(os.environ.get('PORT', 5000))

if __name__ == '__main__':
    app.run()
    #  app.run(host='0.0.0.0', port=current)
