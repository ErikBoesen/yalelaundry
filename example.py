import yalelaundry
import os

# "api" name can be whatever is most convenient for your program
api = yalelaundry.YaleLaundry(os.environ['YALE_API_KEY'])

# You can get anything directly by ID/key
rooms = api.rooms()
availability = api.availability(rooms[1].id)
total = api.totals(rooms[1].id)
appliances = api.appliances(rooms[1].id)
status = api.status(appliances[0].key)
print(appliances)

# Or you can use a more intuitive syntax
room = rooms[8]
availability = room.availability
totals = room.totals
print("There are %d/%d dryers available at %s." % (availability.dryer, totals.dryer, room.name))
