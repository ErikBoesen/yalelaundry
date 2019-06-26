import yalelaundry
import os
from pprint import pprint

# "api" name can be whatever is most convenient for your program
api = yalelaundry.YaleLaundry(os.environ['YALE_API_KEY'])

rooms = api.get_rooms()
availability = api.get_availability(rooms[1].id)
pprint(availability)
