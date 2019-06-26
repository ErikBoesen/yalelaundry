import yalelaundry
import os

# "api" name can be whatever is most convenient for your program
api = yalelaundry.YaleLaundry(os.environ['YALE_API_KEY'])

rooms = api.get_rooms()
availability = api.get_availability(rooms[1].id)
total = api.get_total(rooms[1].id)
appliances = api.get_appliances(rooms[1].id)
print(appliances)
