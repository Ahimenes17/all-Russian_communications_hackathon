from post import address_search
from post import postal_office_find
from pprint import pprint
ToPrint = address_search("c395e711c83187c5602bb1e3db09e07df00eb681", 48.460365, 135.08556, 1000)
pprint(ToPrint)
addresses = postal_office_find("c395e711c83187c5602bb1e3db09e07df00eb681", ToPrint)
pprint(addresses)
