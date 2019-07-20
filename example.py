import yalelaundry
import os

# 'laundry' name can be whatever is most convenient for your program
laundry = yalelaundry.YaleLaundry(os.environ['YALE_API_KEY'])

# You can get anything directly by ID/key
rooms = laundry.rooms()
room = rooms[11]
print(room.name)
print(room)
available = laundry.available(room.id)
total = laundry.total(room.id)
appliances = laundry.appliances(room.id)
status = laundry.status(appliances[0].key)
for appliance in appliances:
    print(appliance.time_remaining_raw)

# Or you can use a more intuitive syntax
room = laundry.room('Trumbull College')
available = room.available
total = room.total
# You can also use the special use method to get around requesting both availability and totals
use = room.use
print('There are %d/%d dryers available at %s.' % (use.available.dryers, use.total.dryers, room.name))

# Putting it all together into one intuitive line, we get the number of available dryers in Branford:
laundry.room('Branford College').available.dryers
