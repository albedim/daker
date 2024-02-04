from flask import Blueprint, request
from flask_cors import cross_origin, CORS
from service.users import getUsers
from utils.filterer import Filterer
from utils.utils import getAvailableCountries

router = Blueprint('NationalityController', __name__, url_prefix="/nationalities")

@router.get("/")
@cross_origin()
def getNationalities():
    return getAvailableCountries()
