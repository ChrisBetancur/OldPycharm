from Util.CellularState import State

GRAVITY = 9.8


def apply_gravity(cell, world):
    below = get_below(cell, world)
    # print("Below:", below)

    '''if below.state == State.EMPTY:
        cell.state = State.EMPTY
        below.state = State.ACTIVE
        return True'''
    return False


def get_below(cell, world):
    cell_radius = cell.determine_radius(world)
    print(cell_radius)

    cell_below = []

    for curr_cell in cell_radius:
        if curr_cell.matrix_row > cell.matrix_row and curr_cell.matrix_col == cell.matrix_col:
            return curr_cell

