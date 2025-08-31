from flask import Flask
from app.database import init_db, db
from app.views.routes import routes
from app.seed import seed_data  # <-- novo import

app = Flask(__name__)
init_db(app)
app.register_blueprint(routes)

with app.app_context():
    db.create_all()
    seed_data()  # <-- insere filmes iniciais

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
