import os
from flask import Flask
from flask_migrate import Migrate
from src.config import configs
from src.utils import db
from src.Album.resources import bp

app = Flask(__name__)
config = os.environ.get('PYTH_SRVR', 'default')
config = configs.get(config)
app.config.from_object(config)
app.register_blueprint(bp)
migrate = Migrate(app, db)
db.init_app(app)

if __name__ == "__main__":
    app.run(debug=True)
