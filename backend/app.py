from flask import Flask, request, jsonify

from src.database.models import User
from src.database.controller import add_user, get_user_by_user_id
from src.database.database import get_db


app = Flask(__name__)


@app.route("/api/user/register", methods=["POST"])
def register_user():
    user = request.get_json()
    db = get_db()

    # python의 dictionary앞에 붙는 **은 편리해요. **이 뭘까요?
    user_model = User(**user)
    add_user(db=db, user=user_model) # 이렇게 하면 데이터베이스에 저장이 되요.
    db.close()
    return jsonify({"message": "success"})

@app.route("/api/user/login", methods=["POST"])
def login_user():
    user_input = request.get_json()
    db = get_db()

    user_db = get_user_by_user_id(db=db, user_id=user_input["user_id"])
    if user_db is None:
        return jsonify({"message": "fail"})
    
    if user_db.user_password != user_input["user_password"]:
        return jsonify({"message": "fail"})
    
    return jsonify({"message": "success"})

if __name__ == "__main__":
    app.run("0.0.0.0", debug=True, port=8080)