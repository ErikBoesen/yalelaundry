import yalelaundry
import os

# 'api' name can be whatever is most convenient for your program
api = yalelaundry.YaleLaundry(os.environ['YALE_API_KEY'])

# You can get anything directly by ID/key
rooms = api.rooms()
room = rooms[11]
print(room.name)
print(room)
availability = api.availability(room.id)
total = api.totals(room.id)
appliances = api.appliances(room.id)
status = api.status(appliances[0].key)
for appliance in appliances:
    print(appliance.time_remaining_raw)

# Or you can use a more intuitive syntax
room = api.room('Trumbull College')
availability = room.availability
totals = room.totals
# You can also use the special use method to get around requesting both availability and totals
use = room.use
print('There are %d/%d dryers available at %s.' % (use.availability.dryer, use.totals.dryer, room.name))
