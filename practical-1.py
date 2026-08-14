# PRACTICAL 1 - implement a simple refelx or goal based agent in toy environment# Goal Based AI Agent - Vacuum Cleaner

DIRTY = "🗑️"
CLEAN = "✨"
room = [DIRTY, CLEAN, DIRTY, DIRTY, CLEAN]
# Display room status
def show_room(room):
    for i in range(len(room)):
        print("Spot", i+1, ":", room[i])
print("Before Cleaning:")
show_room(room) 

def clean_spot(spot):
    if spot == DIRTY:
        return CLEAN
    return spot
    
cleaned = 0

for i in range(len(room)):
    if room[i] == DIRTY:
        cleaned += 1
    room[i] = clean_spot(room[i])
print("\nAfter Cleaning:")
show_room(room)

if DIRTY not in room:
    print("\n🎯 Goal Achieved!")
else:
    print("\n❌ Goal Not Achieved!")
print("🧹 Cleaned Spots:", cleaned)