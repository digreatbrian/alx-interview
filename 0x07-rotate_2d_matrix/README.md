### Rotate 2D Matrix

This task involves rotating a 2D matrix by 90 degrees clockwise in-place, i.e., without creating a new matrix.

### Strategy:
1. **Diagonal Reflection**: First, reflect the matrix along the leading diagonal (negative slope diagonal).
2. **Middle Rotation**: Rotate the resulting matrix along the middle vertical axis.

By following these steps, the matrix is effectively rotated 90 degrees clockwise without the need for additional space.

### Example:
```python
Original Matrix:
1 2 3
4 5 6
7 8 9

After Diagonal Reflection:
1 4 7
2 5 8
3 6 9

After Middle Rotation:
7 4 1
8 5 2
9 6 3
```

This approach ensures an efficient in-place rotation of the matrix.
