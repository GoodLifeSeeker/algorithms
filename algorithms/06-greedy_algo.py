''' We have states which we want to cover with our radio station. We have
stations which cover some states. And we have to create the set of stations
whcih covers as much states as it can by using minumum stations.

States:
mt - Montana,
wa - Washington,
or - Oregon,
id - Idaho,
nv - Nevada,
ut - Utah,
ca - California,
az - Arizona.
'''
states_needed = set(['mt', 'wa', 'or', 'id', 'nv', 'ut', 'ca', 'az'])
stations = {}
stations['k1'] = {'id', 'nv', 'ut'}
stations['k2'] = {'wa', 'id', 'mt'}
stations['k3'] = {'or', 'nv', 'ca'}
stations['k4'] = {'nv', 'ut'}
stations['k5'] = {'ca', 'az'}

final_stations = set()

while states_needed:
    best_station = None
    states_covered = set()
    for station, states_for_station in stations.items():
        covered = states_needed & states_for_station
        if len(covered) > len(states_covered):
            best_station = station
            states_covered = covered
    states_needed -= states_covered
    final_stations.add(best_station)


print('Our final stations are:')
for station in final_stations:
    print(station) 
