from flask import Flask
from flask_cors import CORS

from controllers.user import router as usersRouter
from controllers.nationalities import router as nationalitiesRouter

app = Flask(__name__)

CORS(app)

app.register_blueprint(usersRouter)
app.register_blueprint(nationalitiesRouter)


@app.get("/")
def get():
    return {
        "documentation": "",
        "endpoints": {
            "users": "/users"
        }
    }

if __name__ == '__main__':
    app.run()