def traverse_labyrinth(labyrinth, start, end):
    # Dimensions of the labyrinth
    rows = len(labyrinth)
    columns = len(labyrinth[0])
    orientation = True

    # List of directions to move in the labyrinth (up, down, left, right)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # Auxiliary function to calculate the heuristic distance (Manhattan distance)
    def heuristic_distance(current_pos):
        return abs(current_pos[0] - end[0]) + abs(current_pos[1] - end[1])

    def can_rotate(row, column):
        if (row - 1 >= 0 and row + 1 < rows and column - 1 >= 0 and column + 1 < columns):
            return (labyrinth[row][column] == '.' and labyrinth[row - 1][column] == '.' and labyrinth[row + 1][column] == '.' and
                    labyrinth[row][column - 1] == '.' and labyrinth[row][column + 1] == '.' and
                    labyrinth[row - 1][column - 1] == '.' and labyrinth[row - 1][column + 1] == '.' and
                    labyrinth[row + 1][column - 1] == '.' and labyrinth[row + 1][column + 1] == '.')

        return False 

    def is_valid(row, column):
        return row >= 0 and row < rows and column >= 0 and column < columns and labyrinth[row][column] == '.'

    def has_passable_path(row, column, orientation):
        if orientation:
            return is_valid(row, column - 1) and is_valid(row, column + 1) and column - 1 >= 0

        return is_valid(row - 1, column) and is_valid(row + 1, column) and row - 1 >= 0

    def reconstruct_path(parents, current):
        path = []
        visited = set()  # Conjunto para realizar un seguimiento de los nodos visitados
        while current in parents:
            if current in visited:
                break  # Se ha encontrado un ciclo, salir del bucle
            visited.add(current)
            path.append(current)
            current = parents[current]
        return list(reversed(path))

    # Initialization
    g_scores = {start: 0}
    f_scores = {start: heuristic_distance(start)}
    parents = {}
    open_set = [(f_scores[start], start)]

    while open_set:
        _, current = min(open_set)

        if current == end:
            # Path has been found
            path = reconstruct_path(parents, current)
            total_steps = g_scores[current]
            return path, total_steps

        to_remove = (f_scores[current], current)
        if to_remove in open_set:
            open_set.remove(to_remove)
        else:
            return [], -1


        for direction in directions:
            new_row = current[0] + direction[0]
            new_column = current[1] + direction[1]
            new_pos = (new_row, new_column)

            if is_valid(new_row, new_column) and has_passable_path(new_row, new_column, orientation):
                g_score_new_pos = g_scores[current] + 1

                if new_pos not in g_scores or g_score_new_pos < g_scores[new_pos]:
                    parents[new_pos] = current
                    g_scores[new_pos] = g_score_new_pos
                    f_scores[new_pos] = g_score_new_pos + heuristic_distance(new_pos)

                    if (f_scores[new_pos], new_pos) not in open_set:
                        open_set.append((f_scores[new_pos], new_pos))

        if orientation and can_rotate(current[0], current[1]):
            orientation = False
            if can_rotate(current[0], current[1]):
                g_score_rotate = g_scores[current] + 1
                rotate_pos = (current[0], current[1])
                parents[rotate_pos] = current
                g_scores[rotate_pos] = g_score_rotate
                f_scores[rotate_pos] = g_score_rotate + heuristic_distance(rotate_pos)
                if (f_scores[rotate_pos], rotate_pos) not in open_set:
                    open_set.append((f_scores[rotate_pos], rotate_pos))

    # No path has been found
    return [], -1

print()
print("Labyrinth 1 ")
# Example usage
labyrinth = [
    ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['#', '.', '.', '.', '#', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '#', '.', '.', '.', '.'],
    ['.', '#', '.', '.', '.', '.', '.', '#', '.'],
    ['.', '#', '.', '.', '.', '.', '.', '#', '.']
]

start = (0,0)
end = (3, 8)

path, total_steps = traverse_labyrinth(labyrinth, start, end)
print(path)
if path:
    print(total_steps)
else:
    print(-1)


print()
print("Labyrinth 2 ")
# Example usage
labyrinth2 = [
    ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['#', '.', '.', '.', '#', '.', '.', '#', '.'],
    ['.', '.', '.', '.', '#', '.', '.', '.', '.'],
    ['.', '#', '.', '.', '.', '.', '.', '#', '.'],
    ['.', '#', '.', '.', '.', '.', '.', '#', '.']
]

start2 = (0,0)
end2 = (3, 8)

path2, total_steps2 = traverse_labyrinth(labyrinth2, start2, end2)

if path2:
    print(total_steps2)
else:
    print(-1)



print()
print("Labyrinth 3 ")
# Third labyrinth
labyrinth3 = [
    ['.', '.', '.'],
    ['.', '.', '.'],
    ['.', '.', '.'],
]

start3 = (0, 1)
end3 = (1,2)

path3, total_steps3 = traverse_labyrinth(labyrinth3, start3, end3)
print(path3)
if path3:
    print(total_steps3)
else:
    print(-1)


print()
print("Labyrinth 4 ")
# Fourth labyrinth
labyrinth4 = [
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '#', '.', '.', '.', '.', '#', '.', '.', '.'],
    ['.', '#', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '#', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '#', '.', '.', '.', '#', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '#', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.']
]

start4 = (0, 1)
end4 = (8, 9)

path4, total_steps4 = traverse_labyrinth(labyrinth4, start4, end4)
print(path4)
if path4:
    print(total_steps4)
else:
    print(-1)


