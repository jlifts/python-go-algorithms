# Traveling the states with Greedy first search
states_needed = set(["mt", "wa", "or", "id", "nv", "ut", "ca", "az"])
# Sets will eliminate duplicates
# Gas stations to visit

stations = {}
stations["kone"] = set(["id", "nv", "ut"])
stations["ktwo"] = set(["wa", "id", "mt"])
stations["kthree"] = set(["or", "nv", "ca"])
stations["kfour"] = set(["nv", "ut"])
stations["kfive"] = set(["ca", "az"])

final_station = set()

while states_needed:
    best_station = None
    states_covered = set()
    for station, states_for_station in stations.items():
        # This is a set intersection, it shows things that are similar to both sets.
        # A | is set union, which combines the sets.
        # - is a difference, it will remove subtract one set similar items from the other.
        covered = states_needed & states_for_station
        if len(covered) > len(states_covered):
            best_station = station
            states_covered = covered

    states_needed -= states_covered
    final_station.add(best_station)


print(final_station)
