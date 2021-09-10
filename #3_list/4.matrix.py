
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
# Transform Matrix to List:

print([matrix[row][col] for row in range(len(matrix))
      for col in range(len(matrix))])

# Combine column with Zip and *
print([x for x in zip(*matrix)])
