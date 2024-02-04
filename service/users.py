import random
from datetime import datetime, timedelta

from pip._internal.utils.misc import enum

from data.users import *
from utils.consts import *
from utils.utils import getAvailableCountries, getStuff, getCountryDetails, getRandomStreet, \
    getAvailableProfessions


class User:
    sex: str = None
    age: int = None
    nationality: str = None

    def __init__(self, age, nationality, sex, min_age=10, max_age=99):
        self.sex = sex if sex != "all" else ["male", "female"][random.randint(0,1)]
        if age != "all":
            self.age = int(age)
        else:
            self.age = random.randint(int(min_age), int(max_age))
        self.nationality = nationality if nationality != "all" else getAvailableCountries()[random.randint(0, len(getAvailableCountries()) - 1)]

    def generateRandomName(self):
            names = getStuff().get(self.nationality).get("names")
            if self.sex != "all":
                rn = random.randint(0, len(names) - 1)
                name = names[rn]
                while name['sex'] != "unspecified" and name['sex'] != self.sex:
                    rn = random.randint(0, len(names) - 1)
                    name = names[rn]
                return name['name']
            else:
                rn = random.randint(0, len(names) - 1)
                return names[rn]['name']

    def generateRandomBirthDate(self):
        current_year = datetime.now().year
        random_year = current_year - self.age
        random_month = random.randint(1, 12)
        random_day = random.randint(1, 28)  # Assuming a maximum of 28 days in a month for simplicity
        random_date = datetime(random_year, random_month, random_day)
        return random_date.strftime("%Y-%m-%d")

    def generateRandomSurname(self):
        surnames = getStuff().get(self.nationality).get("surnames")
        rn = random.randint(0, len(surnames) - 1)
        return surnames[rn]

    def generateRandomProfession(self):
        if self.age < 22:
            return "Student"
        rn = random.randint(0, len(getAvailableProfessions()) - 1)
        return getAvailableProfessions()[rn]

    def generateRandomPhoneNumber(self):
        phone_numbers = getStuff().get(self.nationality).get("phone_numbers")
        rn = random.randint(0, len(phone_numbers) - 1)
        return phone_numbers[rn]

    def generateRandomPhoto(self):
        clothing_color_value = hairstyle_values[random.randint(0, len(clothing_color_values) - 1)]
        hairstyle_value = hairstyle_values[random.randint(0, len(hairstyle_values) - 1)]
        hair_color_value = hair_color_values[random.randint(0, len(hair_color_values) - 1)]
        mouth_value = mouth_values[random.randint(0, len(mouth_values) - 1)]
        skin_color_value = skin_color_values[random.randint(0, len(skin_color_values) - 1)]
        glasses_value = glasses_values[random.randint(0, len(glasses_values) - 1)]
        facial_hair_value = facial_hair_values[random.randint(0, len(facial_hair_values) - 1)]
        clothing_value = clothing_values[random.randint(0, len(clothing_values) - 1)]

        if self.sex == "male":
            while "Long" in hairstyle_value:
                rn = random.randint(0, len(hairstyle_values) - 1)
                hairstyle_value = hairstyle_values[rn]
            if self.age < 20:
                facial_hair_value = "Blank"
        else:
            while "Short" in hairstyle_value:
                rn = random.randint(0, len(hairstyle_values) - 1)
                hairstyle_value = hairstyle_values[rn]
            facial_hair_value = "Blank"

        return "https://avataaars.io/?avatarStyle=Circle&topType="+hairstyle_value+"&accessoriesType="+glasses_value+"&hairColor="+hair_color_value+"&facialHairType="+facial_hair_value+"&facialHairColor="+hair_color_value+"&clotheType="+clothing_value+"&clotheColor="+clothing_color_value+"&graphicType=Cumbia&eyeType=Default&eyebrowType=Default&mouthType="+mouth_value+"&skinColor=" + skin_color_value

def getUser(sex, age, max_age, min_age, nationality):

    if min_age != "all":
        if max_age != "all":
            user = User(age, nationality, sex, min_age, max_age)
        else:
            user = User(age, nationality, sex, min_age)
    else:
        user = User(age, nationality, sex)

    ranoomBirthDate = user.generateRandomBirthDate()
    userNationality = getCountryDetails(user.nationality)

    return {
        "name": user.generateRandomName(),
        "surname": user.generateRandomSurname(),
        "birth_date": ranoomBirthDate,
        "phone_number": user.generateRandomPhoneNumber(),
        "sex": user.sex.capitalize(),
        "image": user.generateRandomPhoto(),
        "nationality": user.nationality.capitalize(),
        "address": {
            "country": {
                "name": userNationality.get("country"),
                "code": userNationality.get("country_code")
            },
            "street": getRandomStreet(user.nationality)
        },
        "profession": user.generateRandomProfession().capitalize()
    }

def getUsers(sex, age, max_age, min_age, nationality):
    users = []
    for i in range(50):
        if min_age != "all":
            if max_age != "all":
                user = User(age, nationality, sex, min_age, max_age)
            else:
                user = User(age, nationality, sex, min_age)
        else:
            user = User(age, nationality, sex)

        ranoomBirthDate = user.generateRandomBirthDate()
        userNationality = getCountryDetails(user.nationality)
        users.append({
            "name": user.generateRandomName(),
            "surname": user.generateRandomSurname(),
            "birth_date": ranoomBirthDate,
            "phone_number": user.generateRandomPhoneNumber(),
            "sex": user.sex.capitalize(),
            "image": user.generateRandomPhoto(),
            "nationality": user.nationality.capitalize(),
            "address": {
                "country": {
                    "name": userNationality.get("country"),
                    "code": userNationality.get("country_code")
                },
                "street": getRandomStreet(user.nationality)
            },
            "profession": user.generateRandomProfession().capitalize()
        })
    return users