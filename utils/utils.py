import random

from faker import Faker

from data.users import *


def getStuff():
    return {
        "italian": {
            "names": italian_names,
            "surnames": italian_surnames,
            "phone_numbers": italian_phone_numbers
        },
        "russian": {
            "names": russian_names,
            "surnames": russian_surnames,
            "phone_numbers": russian_phone_numbers
        },
        "french": {
            "names": french_names,
            "surnames": french_surnames,
            "phone_numbers": french_phone_numbers
        },
        "german": {
            "names": german_names,
            "surnames": german_surnames,
            "phone_numbers": german_phone_numbers
        },
        "american": {
            "names": american_names,
            "surnames": american_surnames,
            "phone_numbers": american_phone_numbers
        },
        "african": {
            "names": african_names,
            "surnames": african_surnames,
            "phone_numbers": african_phone_numbers
        },
        "chinese": {
            "names": chinese_names,
            "surnames": chinese_surnames,
            "phone_numbers": chinese_phone_numbers
        },
        "japanese": {
            "names": japanese_names,
            "surnames": japanese_surnames,
            "phone_numbers": japanese_phone_numbers
        },
        "indian": {
            "names": indian_names,
            "surnames": indian_surnames,
            "phone_numbers": indian_phone_numbers
        },
        "brazilian": {
            "names": brazilian_names,
            "surnames": brazilian_surnames,
            "phone_numbers": brazilian_phone_numbers
        },
        "algerian": {
            "names": algerian_names,
            "surnames": algerian_surnames,
            "phone_numbers": algerian_phone_numbers
        },
        "canadian": {
            "names": canadian_names,
            "surnames": canadian_surnames,
            "phone_numbers": canadian_phone_numbers
        },
        "australian": {
            "names": australian_names,
            "surnames": australian_surnames,
            "phone_numbers": australian_phone_numbers
        },
        "spanish": {
            "names": spanish_names,
            "surnames": spanish_surnames,
            "phone_numbers": spanish_phone_numbers
        },
        "ukrainian": {
            "names": ukrainian_names,
            "surnames": ukrainian_surnames,
            "phone_numbers": ukrainian_phone_numbers
        },
        "polish": {
            "names": polish_names,
            "surnames": polish_surnames,
            "phone_numbers": polish_phone_numbers
        },
        "english": {
            "names": english_names,
            "surnames": english_surnames,
            "phone_numbers": english_phone_numbers
        }
    }


def getAvailableCountries():
    return [
        "italian", "russian", "french", "german", "american", "african",
        "chinese", "japanese", "indian", "brazilian", "algerian",
        "canadian", "australian", "spanish", "ukrainian", "polish", "english"
    ]

def getCountryDetails(nationality):
    return {
        "italian": {"country": "Italy", "country_code": "IT", "c": "it_IT"},
        "russian": {"country": "Russia", "country_code": "RU", "c": "ru_RU"},
        "french": {"country": "France", "country_code": "FR", "c": "fr_FR"},
        "german": {"country": "Germany", "country_code": "DE", "c": "de_DE"},
        "american": {"country": "United States", "country_code": "US", "c": "en_US"},
        "african": {"country": "Africa", "country_code": "AF", "c": "en_US"},
        "chinese": {"country": "China", "country_code": "CN", "c": "zh_CN"},
        "japanese": {"country": "Japan", "country_code": "JP", "c": "ja_JP"},
        "indian": {"country": "India", "country_code": "IN", "c": "hi_IN"},
        "brazilian": {"country": "Brazil", "country_code": "BR", "c": "pt_BR"},
        "algerian": {"country": "Algeria", "country_code": "DZ", "c": "ar_JO"},
        "canadian": {"country": "Canada", "country_code": "CA", "c": "en_CA"},
        "australian": {"country": "Australia", "country_code": "AU", "c": "en_AU"},
        "spanish": {"country": "Spain", "country_code": "ES", "c": "es_ES"},
        "ukrainian": {"country": "Ukraine", "country_code": "UA", "c": "uk_UA"},
        "polish": {"country": "Poland", "country_code": "PL", "c": "pl_PL"},
        "english": {"country": "United Kingdom", "country_code": "GB", "c": "en_GB"}
    }.get(nationality)

def getAvailableProfessions():
    return [
        "doctor", "engineer", "teacher", "lawyer", "chef", "artist",
        "programmer", "scientist", "writer", "athlete", "architect",
        "musician", "actor", "nurse", "police officer", "firefighter",
        "entrepreneur", "designer", "pilot", "journalist", "psychologist",
        "veterinarian", "electrician", "plumber", "mechanic", "pharmacist",
        "dentist", "accountant", "astronaut", "graphic designer",
        "real estate agent", "fashion designer", "photographer", "paramedic",
        "chemist", "biologist", "geologist", "librarian", "social worker",
        "mathematician", "economist", "physicist", "chemist", "astronomer",
        "marine biologist", "speech therapist", "occupational therapist",
        "physical therapist", "radiologist", "dietitian", "IT consultant",
        "cybersecurity analyst", "data scientist", "network administrator",
        "human resources manager", "marketing manager", "sales representative",
        "event planner", "public relations specialist", "financial analyst",
        "investment banker", "actuary", "web developer", "UX designer",
        "civil engineer", "mechanical engineer", "electrical engineer",
        "chemical engineer", "environmental scientist", "forensic scientist",
        "historian", "archaeologist", "linguist", "translator", "paramedic",
        "veterinary technician", "phlebotomist", "radiation therapist",
        "ultrasound technician", "acupuncturist", "paramedic", "optometrist",
        "paralegal", "court reporter", "event coordinator", "florist",
        "landscaper", "travel agent", "air traffic controller",
        "flight attendant", "event coordinator", "wedding planner",
        "biomedical engineer", "biotechnologist", "geneticist", "zoologist",
        "airline pilot", "fire inspector", "forester", "surveyor",
        "taxi driver", "airline pilot", "bus driver", "train conductor",
        "construction worker", "welder", "plasterer", "bricklayer"
    ]

def getRandomStreet(nationality):
    fake = Faker(getCountryDetails(nationality).get("c"))
    return fake.street_address()