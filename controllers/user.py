from flask import Blueprint, request
from flask_cors import cross_origin, CORS
from service.users import getUsers
from utils.filterer import Filterer

router = Blueprint('UserController', __name__, url_prefix="/users")

@router.get("/one")
@cross_origin()
def _getUser():
    params = request.args
    return Filterer.filter(params, True)


@router.get("/")
@cross_origin()
def _getUsers():
    params = request.args
    return Filterer.filter(params)
