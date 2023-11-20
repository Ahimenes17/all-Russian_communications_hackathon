
def address_search(token, latitude, longitude, radius):
    from dadata import Dadata
    # token = "c395e711c83187c5602bb1e3db09e07df00eb681"
    dadata = Dadata(token)
    address_data = dadata.geolocate(name="address", lat=latitude, lon=longitude, radius_meters=radius)

    if address_data:
        postals = {}
        for suggestion in address_data:
            if postals.get(suggestion['data']['postal_code']):
                postals[suggestion['data']['postal_code']].append(suggestion)
            else:
                postals[suggestion['data']['postal_code']] = [suggestion]

    return postals


def postal_office_find(token, postals):
    from dadata import Dadata
    dadata = Dadata(token)
    office_info = []
    for index in postals.keys():
        office_info.append(dadata.find_by_id("postal_unit", index))
    return office_info


