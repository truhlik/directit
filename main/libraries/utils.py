import logging
from typing import Tuple, Dict
from urllib.parse import unquote

from ares_util.ares import call_ares
from ares_util.validators import czech_company_id_numeric_validator

logger = logging.getLogger(__name__)


def parse_street_and_number(street_and_number: str) -> Tuple[str, str]:
    """
    Vezme jeden string (ulice a ČP dohromady) a snaží se to parsovat na dva.
    """
    for i, c in enumerate(street_and_number):
        # najdi prvni cislici v ulice_cislo
        # přeskočím první 3 písmena, abych nechytal čísla jako 1. pluku apod.
        if c.isdigit() and i not in [1, 2, 3]:
            return street_and_number[:i - 1], street_and_number[i:]

    # pokud nic nenajdu tak vrátím v ulici všechno a do ČP nic
    return street_and_number, ''


def parse_first_and_last_name(first_and_last_name: str) -> Tuple[str, str]:
    """
    Vezme jeden string (jméno a příjmení dohromady) a snaží se to parsovat na dva.
    """
    # todo fixnout problém s titulem za jménem
    try:
        return ' '.join(first_and_last_name.split()[:-1]), first_and_last_name.split()[-1]
    except IndexError:
        return first_and_last_name, ''


def get_info_from_ares(reg_number: str) -> Dict:

    if not isinstance(reg_number, str):
        try:
            reg_number = str(reg_number)
        except (ValueError, TypeError):
            return {}

    try:
        json_data = call_ares(reg_number)
    except Exception:
        return {}

    if not json_data:
        return {}

    city2_name = json_data['address']['city']
    zip = json_data['address']['zip_code']

    street2_name, number2_name = parse_street_and_number(json_data['address']['street'])

    dic = json_data['legal']['company_vat_id']
    first_name, last_name = parse_first_and_last_name(json_data['legal']['company_name'])
    full_name = json_data['legal']['company_name']

    return {
        'city': city2_name,
        'street': street2_name,
        'street_number': number2_name,
        'zip': zip,
        'vat_number': dic,
        'first_name': first_name,
        'last_name': last_name,
        'name': full_name,
    }


def validate_reg_number(reg_number: str):
    czech_company_id_numeric_validator(reg_number)


def get_location_format(number=None, street=None, zip_code=None, city=None):
    adrress = ""

    if street:
        adrress += street
        if not number and city:
            adrress += ","
        adrress += " "

    if number:
        if street:
            adrress += number
            if city:
                adrress += ", "
    if city:
        adrress += city
        # for villages without street put number after city name
        if not street and number:
            adrress += " "
            adrress += number
        if zip_code:
            adrress += " "
    if zip_code:
        adrress += zip_code
    return adrress


def decode_url(url: str):
    return unquote(url)
