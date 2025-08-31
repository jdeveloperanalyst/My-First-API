from flask import Flask
from app.database import init_db, db
from app.views.routes import routes
from app.seed import seed_data
from flasgger import Swagger

app = Flask(__name__)
swagger = Swagger(app, template_file="swagger.yaml")
init_db(app)
app.register_blueprint(routes)

with app.app_context():
    db.create_all()
    seed_data()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
