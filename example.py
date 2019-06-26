import yalelaundry
import os
from pprint import pprint

# "api" name can be whatever is most convenient for your program
api = yalelaundry.YaleLaundry(os.environ['YALE_API_KEY'])

pprint(api.get_rooms())
#pprint(api.get_availabilities())
