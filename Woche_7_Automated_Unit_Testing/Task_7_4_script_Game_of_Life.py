def evolve(world, steps):
    allowed = set("-" + "|" + "#" + " ")

    if len(world) == 0:
        raise Warning("Your World is empty")

    line_length = len(world[0])
    pure_world = []
    populated_cells = 0

    def cell_mutation(x_coord, y_coord):

        status = " "
        neighbors_alive = 0

        if pure_world[y_coord][x_coord] != "#" and pure_world[y_coord][x_coord] != " ":
            raise Warning("Invalid 'valid' char in line")

        for i in range(-1, 2):
            for j in range(-1, 2):
                if i == 0 and j == 0:  # not itself
                    continue
                elif y_coord + i >= 0 and x_coord + j >= 0:
                    try:
                        if pure_world[y_coord + i][x_coord + j] == "#":
                            neighbors_alive += 1
                    except:
                        pass

        if pure_world[y_coord][x_coord] == "#":
            if neighbors_alive == 2 or neighbors_alive == 3:
                status = "#"
        else:
            if neighbors_alive == 3:
                status = "#"

        return status

    if type(steps) is not int:
        raise Warning("step value is not an integer")

    if steps < 1:
        raise Warning("step value must be positive")

    if line_length < 3 or len(world) < 3:  # too little length or too little height
        raise Warning("world is too small")

    for index, line in enumerate(world):

        if type(line) is not str:
            raise Warning(f"line {line} isn't a string")

        if not set(line) <= allowed:
            raise Warning("invalid character in world")

        if len(line) != line_length:
            raise Warning("not every line has same length")

        if index != 0 and index != len(world) - 1:
            if line[-1] != "|" or line[0] != "|":
                raise Warning("invalid 'valid' char in border")

        pure_world.append(line[1:-1])

    pure_world = pure_world[1:-1]
    end_field = pure_world

    for i in range(steps):

        pure_world = end_field
        end_field = []
        populated_cells = 0

        for y_index, line in enumerate(pure_world):
            result_line = ""

            for x_index, cell in enumerate(line):
                cell = cell_mutation(x_index, y_index)
                result_line += cell
                if cell == "#":
                    populated_cells += 1

            end_field.append(result_line)

    for index, line in enumerate(end_field):
        end_field[index] = "|" + line + "|"

    end_field.insert(0, line_length * "-")
    end_field.insert(len(end_field), line_length * "-")

    end_field = tuple(end_field)

    return end_field, populated_cells


field = (
    "-----",
    "| ##|",
    "| # |",
    "|#  |",
    "-----"
)

# field = (
#             "--------------",
#             "|            |",
#             "|  ###       |",
#             "|  #         |",
#             "|   #        |",
#             "|            |",
#             "--------------"
#         )

steps = 1

result, alive_cells = evolve(field, steps)

print(f"Game of Life after {steps} moves:")
for row in result:
    print(row)
print(f"{alive_cells} are alive.")
