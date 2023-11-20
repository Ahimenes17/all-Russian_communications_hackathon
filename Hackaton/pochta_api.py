from dadata import Dadata
import requests
from pprint import pprint
import json


def pocha_get(val_radius, val_dolgota, val_shirota):
    token = "c395e711c83187c5602bb1e3db09e07df00eb681"
    secret = "5a1d03971d7cd51a0361af059f5094822e0724d3"
    dadata = Dadata(token, secret)

    responce = dadata.geolocate(
        name="address", lat=val_shirota, lon=val_dolgota, radius_meters=val_radius
    )

    address_data = responce
    if address_data:
        # Обрабатываем полученные данные
        if address_data:
            postals = {}

            # pprint(address_data)
            for suggestion in address_data:
                address = suggestion.get("value")
                index = suggestion.get("data", {}).get("postal_code")
                print("Адрес:", address)
                print("Индекс:", index)
                print()
                if postals.get(suggestion["data"]["postal_code"]):
                    postals[suggestion["data"]["postal_code"]].append(suggestion)
                else:
                    postals[suggestion["data"]["postal_code"]] = [suggestion]
            
    def postal_office(index):
        url = "https://address_data.dadata.ru/address_data/api/"
