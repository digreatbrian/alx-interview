# Island Perimeter
## Description
The `island_perimeter` function calculates the perimeter of an island in a given grid. The grid is a list of lists of integers, where:
- `0` represents water
- `1` represents land

Each cell in the grid is a square with a side length of 1. Cells are connected horizontally or vertically (not diagonally). The grid is completely surrounded by water and contains only one island (or none). The island does not contain any lakes (water inside that isn't connected to the water surrounding the island).

## Features
- **Simple and Efficient**: Calculate the perimeter of an island in a grid with a straightforward algorithm.
- **No External Dependencies**: The function does not require any external modules or libraries.

## Requirements
- Python 3.x

## Function Signature
```python
def island_perimeter(grid: list[list[int]]) -> int:
    """
    Calculate the perimeter of an island in a given grid.

    Args:
        grid (list[list[int]]): A 2D grid representing the map.

    Returns:
        int: The perimeter of the island.
    """
```

## Example
```python
# Example Usage
grid = [
    [0, 1, 0, 0],
    [1, 1, 1, 0],
    [0, 1, 0, 0],
    [1, 1, 0, 0]
]

print(island_perimeter(grid))  # Output: 16
```

## Constraints
- The grid is rectangular with its width and height not exceeding 100.
- The grid is completely surrounded by water.
- There is only one island or nothing in the grid.
- The island does not have lakes.

## How It Works
The function iterates through each cell in the grid. When it encounters a land cell (`1`), it checks its four neighboring cells (up, down, left, right). If a neighboring cell is water (`0`) or out of bounds, it adds to the perimeter count.

## Testing
To run tests, create a separate test file and use the following structure:
```python
import unittest
from your_module import island_perimeter

class TestIslandPerimeter(unittest.TestCase):
    def test_example(self):
        grid = [
            [0, 1, 0, 0],
            [1, 1, 1, 0],
            [0, 1, 0, 0],
            [1, 1, 0, 0]
        ]
        self.assertEqual(island_perimeter(grid), 16)

if __name__ == '__main__':
    unittest.main()
```

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributions
Contributions are welcome! Please open an issue or submit a pull request.

## Contact
For any questions, feel free to open an issue or contact the repository owner.

---

Happy Coding!

---

![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

Feel free to replace the placeholder image links with actual images relevant to your project.
