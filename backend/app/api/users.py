from app.api import bp
from app.models import User, UserSchema
from flask import json, Response

user_schema = UserSchema()

@bp.route("/users", methods=["GET"])
def get_all():
    users = User.get_all_users()
    print(users)
    serialize_users = user_schema.dump(users, many=True).data
    return custom_response(serialize_users, 200)


def custom_response(res, status_code):
    return Response(mimetype="application/json", response=json.dumps(res), status=status_code)



