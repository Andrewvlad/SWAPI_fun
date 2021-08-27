# Using data provided from the
#       Star Wars API (https://swapi.dev/)

# produce a
#       list

# of all possible
#       species

# for a given
#       planet

# Planet Name --> Planet URL

import json
from urllib.request import urlopen

api_key = ''  # No authentication is required to query and get data from SW-API.
planet_url = 'https://swapi.dev/api/planets/'


def api_call(url: str) -> dict:
    json_url = urlopen(url)
    return json.loads(json_url.read())  # converts json to dict


def convert_to_people(resident_list: list) -> list:
    species_set = set()
    for resident in resident_list:
        species_set |= {*api_call(url=resident).get('species')}
    return [api_call(url=species).get('name') for species in species_set]


def read_planet(planet_name: str, request_url: str = planet_url) -> dict:
    planets_dict = api_call(url=request_url)
    for planet in planets_dict.get("results"):
        if planet.get("name") == planet_name:  # if you find the planet
            return planet
    # otherwise, cycle to the next page
    return read_planet(planet_name=planet_name, request_url=next_page) if (next_page := planets_dict.get('next')) else next_page


def main(user_input: str) -> list:
    if planet_dict := read_planet(planet_name=user_input):  # check if planet exists
        return convert_to_people(resident_list=planet_dict.get('residents'))  # check if planet exists
    return ["Planet not found"]


def tester():
    # duplicate species - Tatooine
    assert main("Tatooine") == ['Droid'], "Should be {'Droid'}"
    # no species - Tholoth
    assert main("Tholoth") == [], "Should be {''}"
    # fake planet - Zatooine
    assert main("Zatooine") == ["Planet not found"], "Should be \"Planet not found\""


if __name__ == '__main__':
    tester()
    print("Everything passed")
