from flask import Flask
from src.Album.resources import bp

app = Flask(__name__)


app.register_blueprint(bp)
app.run(debug=True)
