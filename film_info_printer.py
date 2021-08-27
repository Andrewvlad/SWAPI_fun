import json
from urllib.request import urlopen
import requests


def print_dict(data: dict):
    for key, value in data.items():
        print(key + ': ')
        if type(value) is list:
            for sub_value in value:
                print('\t' + sub_value)
        else:
            print('\t' + str(value))
        print()


def get_dict(url: str) -> dict:
    json_payload = urlopen(url).read()
    return json.loads(json_payload)  # calls a URL and converts the json result to return a dict


def get_name(url: str) -> str:
    json_payload = requests.get(url).json()
    return json_payload["name"]


def filled_page(url: str):
    data = get_dict(url)
    for key, value in data.items():
        if type(value) is list:
            data[key] = [get_name(sub_value) for sub_value in value]
    print_dict(data)


def main():
    filled_page('http://swapi.dev/api/films/1/')


main()

