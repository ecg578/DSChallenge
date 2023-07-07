# Data Engineer Challenge

This challenge is part of the evaluation process for the Data Engineer position at Damavis. The goal of the challenge is to solve a labyrinth puzzle by finding the minimal number of moves required to carry a rod from the top left corner to the bottom right corner of the labyrinth.

## Challenge Description

The labyrinth is represented as a rectangular matrix, where each cell can be either empty (represented by '.') or blocked (represented by '#'). The rod, which needs to be moved through the labyrinth, is represented as a 1 × 3 rectangle. The rod cannot collide with blocked cells or the walls of the labyrinth.

The participant can perform five types of moves: move the rod one cell down, move the rod one cell up, move the rod one cell to the right, move the rod one cell to the left, or rotate the rod's orientation from horizontal to vertical or vice versa. Rotations can only be performed if the 3 × 3 area surrounding the rod is clear from obstacles or walls.

The initial position of the rod is horizontally oriented, with its left cell at [0, 0]. The goal is to move the rod into a position where one of its cells is in the bottom right cell of the labyrinth.

If it is impossible to reach the goal, the output should be -1.

## Input

- `labyrinth`: A rectangular array of characters representing the labyrinth. Each element `labyrinth[i][j]` can be either '.' if the corresponding cell is empty or '#' if the corresponding cell is blocked.

## Output

- `result`: An integer representing the number of moves required to carry the rod to the end of the labyrinth. If it is impossible to reach the goal, the output should be -1.

## Constraints

- 3 ≤ labyrinth.length ≤ 1000
- 3 ≤ labyrinth[i].length ≤ 1000

## Example

```python
labyrinth = [
    [".", ".", ".", ".", ".", ".", ".", ".", "."],
    ["#", ".", ".", ".", "#", ".", ".", ".", "."],
    [".", ".", ".", ".", "#", ".", ".", ".", "."],
    [".", "#", ".", ".", ".", ".", ".", "#", "."],
    [".", "#", ".", ".", ".", ".", ".", "#", "."]
]
result = solution(labyrinth)
print(result)  # Output: 11
```

## Acceptance Tests

The following are some acceptance tests that the solution should pass:

### Test 1:

```python
labyrinth = [
    [".", ".", ".", ".", ".", ".", ".", ".", "."],
    ["#", ".", ".", ".", "#", ".", ".", ".", "."],
    [".", ".", ".", ".", "#", ".", ".", ".", "."],
    [".", "#", ".", ".", ".", ".", ".", "#", "."],
    [".", "#", ".", ".", ".", ".", ".", "#", "."]
]
result = solution(labyrinth)
print(result)  # Output: 11
```

### Test 2:

```python
labyrinth = [
    [".", ".", ".", ".", ".", ".", ".", ".", "."],
    ["#", ".", ".", ".", "#", ".", ".", "#", "."],
    [".", ".", ".", ".", "#", ".", ".", ".", "."],
    [".", "#", ".", ".", ".", ".", ".", "#", "."],
    [".", "#", ".", ".", ".", ".", ".", "#", "."]
]
result = solution(labyrinth)
print(result)  # Output: -1
```

### Test 3:

```python
labyrinth = [
    [".", ".", "."],
    [".", ".", "."],
    [".", ".", "."]
]
result = solution(labyrinth)
print(result)  # Output: 2
```

### Test 4:

```python
labyrinth = [
    [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", "#", ".", ".", ".", ".", "#", ".", ".", "."],
    [".", "#", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", "#", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", "#", ".", ".", ".", "#", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", "#", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", ".", "."]
]
result = solution(labyrinth)
print(result)  # Output: 16
```

Good luck with the challenge! Feel free to reach out if you have any questions.
