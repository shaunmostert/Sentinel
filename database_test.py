import modules.database as database


events = database.get_events()

for event in events:
    print(event)