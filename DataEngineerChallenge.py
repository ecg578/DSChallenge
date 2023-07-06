def traverse_labyrinth(labyrinth, start, end):
    # Labyrinth dimensions
    rows = len(labyrinth)
    columns = len(labyrinth[0])
    horizontal = True

    # List of directions to move in the labyrinth (up, down, left, right)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # Helper function to calculate the heuristic distance (Manhattan distance)
    def heuristic_distance(current_pos):
        return abs(current_pos[0] - end[0]) + abs(current_pos[1] - end[1])

    def can_rotate(row, col,horizontal):
        if (row-1 and col == '.') and (row+1 and col == '.') and (row and col-1 == '.') and (row and col+1 == '.') and (row-1 and col-1=='.') and (row+1 and col+1=='.') and (row-1 and col+1=='.') and (row+1 and col-1=='.'):
            return not horizontal
        else: 
            return horizontal


    # Helper function to check if a position is within the labyrinth and is traversable
    def is_valid(row, col, horizontal):
        if (row >= 0 and row < rows and col >= 0 and col < columns and labyrinth[row][col] == '.' and horizontal):
            return (row-1 and col == '.') and (row+1 and col == '.')
        elif (row >= 0 and row < rows and col >= 0 and col < columns and labyrinth[row][col] == '.' and not horizontal):
            return (row and col-1 == '.') and (row and col+1 == '.')
        else:
            return False


    # Helper function to reconstruct the path from start to end
    def reconstruct_path(parents, current):
        path = []
        while current in parents:
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

        open_set.remove((f_scores[current], current))

        for direction in directions:
            new_row = current[0] + direction[0]
            new_col = current[1] + direction[1]
            new_pos = (new_row, new_col)

            if is_valid(new_row, new_col, horizontal):
                g_score_new_pos = g_scores[current] + 1
                #horizontal= can_rotate(new_row,new_col,horizontal)
                if new_pos not in g_scores or g_score_new_pos < g_scores[new_pos]:
                    # Found a shorter path to this position
                    parents[new_pos] = current
                    g_scores[new_pos] = g_score_new_pos
                    f_scores[new_pos] = g_score_new_pos + heuristic_distance(new_pos)
                    if (f_scores[new_pos], new_pos) not in open_set:
                        open_set.append((f_scores[new_pos], new_pos))

    # No valid path found
    return [], -1

# Example usage
labyrinth = [
    ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['#', '.', '.', '.', '#', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '#', '.', '.', '.', '.'],
    ['.', '#', '.', '.', '.', '.', '.', '#', '.'],
    ['.', '#', '.', '.', '.', '.', '.', '#', '.']
]

start = (0, 0)
end = (4, 8)

path, total_steps = traverse_labyrinth(labyrinth, start, end)

if total_steps == -1:
    print(-1)
else:
    for row, col in path:
        labyrinth[row][col] = 'O'
    for row in labyrinth:
        print(' '.join(row))
    print(total_steps)
