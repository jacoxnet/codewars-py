def adjacent(loc, ship):
    for point in ship:
        if (point[0] == loc[0] and abs(point[1] - loc[1]) == 1) or (point[1] == loc[1] and abs(point[0] - loc[0]) == 1):
            # point adjacent - return 1
            return 1
        elif abs(point[0]-loc[0]) == 1 and abs(point[1] - loc[1]) == 1:
            # diag adjacent - can't have that
            return -1
    # no points adjacent
    return 0

def add_ship(all_ships, loc):
    for ship in all_ships.copy():
        if loc in ship:
            # part of existing ship
            return all_ships
        elif adjacent(loc, ship) == 1:
            # adjacent to existing ship - add to that one
            ship.append(loc)
            return all_ships
        elif adjacent(loc, ship) == -1:
            # can't have adjacent diag - return None
            return []
        else:
            pass
    # new ship
    all_ships.append([loc])
    return all_ships

def validate_battlefield(field):
    all_ships = []
    # assign adjacent points to ships
    for r in range(10):
        for c in range(10):
            if field[r][c] == 1:
                all_ships = add_ship(all_ships, (r, c))
    # check length of various ships
    # print(all_ships)
    if len(all_ships) == 10:
        if len([ship for ship in all_ships if len(ship) == 4]) == 1:
            if len([ship for ship in all_ships if len(ship) == 3]) == 2:
                if len([ship for ship in all_ships if len(ship) == 2]) == 3:
                    if len([ship for ship in all_ships if len(ship) == 1]) == 4:
                        return True
    return False
