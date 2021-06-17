"""An example of getting data through a URL request"""
import requests


# This is a twitter user example pulling info about Elon Musk
r = requests.get("https://lambda-ds-twit-assist.herokuapp.com/user/elonmusk")
print("The request was made with status code: {}".format(r.status_code))


# This turns the json file into a python dict
elonmusk_dict = r.json()
print(elonmusk_dict["tweets"][0]["full_text"])


# This is an example with the poke api
poke_r = requests.get("https://pokeapi.co/api/v2/pokemon/squirtle")
print("The request was made with status code: {}".format(poke_r.status_code))
squirtle_dict = poke_r.json()
print(squirtle_dict["name"])
