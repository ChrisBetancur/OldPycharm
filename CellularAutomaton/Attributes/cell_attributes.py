
def validate_position(row, col, world):
    if world.rows > row >= 0 and world.columns > col >= 0:
        return True
    return False
