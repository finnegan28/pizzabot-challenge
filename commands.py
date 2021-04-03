#!/usr/bin/python


def valid_args(args):
    arg_count = len(args)
    # Validate amount of arguments
    if arg_count < 3:
        exit("Argument missing. Example format, 'pizzabot.py 5x5 (5,5)'")


def valid_grid(size):
    # Split grid on the x
    parsed_size = size.lower()
    grid_split = parsed_size.split("x")

    # Validate grid format
    if len(grid_split) != 2:
        exit(f"\n{size} is not valid. Please follow format for grid size. Example '5x5'")

    # Try to convert to int, will fail if empty or non-numeric
    try:
        grid_x = int(grid_split[0])
        grid_y = int(grid_split[1])
    except ValueError:
        exit(f"\n{size} is not valid. Grid cannot be empty or non-numeric. Example '5x5'")

    # Validate grid size is not 0 or negative
    if grid_x <= 0 or grid_y <= 0:
        exit(f"\n{size} is not valid. Grid size cannot be 0 or negative. Example '5x5'")


def valid_locations(size, locations):

    parsed_size = size.lower()
    grid_split = parsed_size.split("x")
    grid_x = int(grid_split[0])
    grid_y = int(grid_split[1])

    # Valid Delivery Locations
    for location in locations:
        if not (location[0] == "(" and location[len(location) - 1] == ")"):
            exit(f"\n{location} is not surrounded with brackets. Example '(5,5)'")

        try:
            # Split the delivery x y co-ords
            location_split = location.strip("()").split(",")
            # Check if enough co-ords provided
            if len(location_split) < 2:
                exit(f"\n{location} is not valid. Not enough co-ordinates provided. Example '(5,5)'")
            # Try to convert to int, will fail if empty or non-numeric
            current_x = int(location_split[0])
            current_y = int(location_split[1])
        except ValueError:
            exit(f"\n{location} is not valid. Co-ordinates cannot be empty or non-numeric. Example '(5,5)'")

        # Validate grid size is not negative
        if current_x < 0 or current_y < 0:
            exit(f"\n{location} is not valid. Delivery location cannot be negative. Example '(5,5)'")

        # Within Delivery Area check
        if current_x > grid_x or current_y > grid_y:
            exit(f"\n{location_split} is not in the specified delivery area")


def deliver_pizza(locations):
    delivery_list = [[0, 0]]
    delivery_coords = ""
    x = 0

    for location in locations:
        # Split the delivery x y co-ords
        location_split = location.strip("()").split(",")
        current_x = int(location_split[0])
        current_y = int(location_split[1])
        delivery_list.append([current_x, current_y])

    for delivery in (delivery_list[1::]):
        previous_coord = delivery_list[x]
        # Calculate X axis moves
        x_move = previous_coord[0] - delivery[0]
        while x_move < 0:
            delivery_coords = delivery_coords + "E"
            x_move += 1
        while x_move > 0:
            delivery_coords = delivery_coords + "W"
            x_move -= 1
        # Calculate Y axis moves
        y_move = previous_coord[1] - delivery[1]
        while y_move < 0:
            delivery_coords = delivery_coords + "N"
            y_move += 1
        while y_move > 0:
            delivery_coords = delivery_coords + "S"
            y_move -= 1
        if y_move == 0 and x_move == 0:
            delivery_coords = delivery_coords + "D"
        x = x+1

    return delivery_coords
