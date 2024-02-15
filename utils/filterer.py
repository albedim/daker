import random
from exceptions.InvalidParamException import InvalidParamException
from service.users import getUsers, getUser
from utils.consts import MAX_VALUES
from utils.utils import getAvailableCountries


class Filterer:

    @classmethod
    def filter(cls, params: dict, one=False):

        sex = "all"
        age = "all"
        max_age = "all"
        min_age = "all"
        n = 20
        nationality = "all"

        try:
            if "n" in params:
                if not str(params.get("n")).isnumeric():
                    raise InvalidParamException("n", "a number")
                if int(params.get("n")) > MAX_VALUES:
                    raise InvalidParamException("n", "less than <"+str(MAX_VALUES)+">")
                n = int(params.get("n"))
            if "nationality" in params:
                if str(params.get("nationality")) not in getAvailableCountries():
                    raise InvalidParamException("nationality", "one of these: " + str(getAvailableCountries()))
                nationality = str(params.get("nationality"))
            if "sex" in params:
                if str(params.get("sex")) != "male" and str(params.get("sex")) != "female":
                    raise InvalidParamException("sex", "equals to <male> or <female>")
                sex = str(params.get("sex"))
            if "age" in params:
                if not str(params.get("age")).isnumeric():
                    raise InvalidParamException("age", "a number")
                age = int(params.get("age"))
            else:
                if "min_age" in params:
                    if not str(params.get("min_age")).isnumeric():
                        raise InvalidParamException("min_age", "a number")
                    if int(params.get("min_age")) < 10:
                        raise InvalidParamException("min_age", "grater than <10>")
                    min_age = int(params.get("min_age"))
                    if "max_age" in params:
                        if not str(params.get("max_age")).isnumeric():
                            raise InvalidParamException("max_age", "a number")
                        if int(params.get("max_age")) > 99:
                            raise InvalidParamException("max_age", "less than <99>")
                        max_age = int(params.get("max_age"))
            if one:
                return getUser(sex, age, max_age, min_age, nationality)
            return getUsers(n, sex, age, max_age, min_age, nationality)

        except InvalidParamException as exc:
            return {
                "error": True,
                "code": exc.code,
                "message": exc.message
            }, exc.code