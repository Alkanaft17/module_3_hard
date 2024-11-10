def calculate_structure_sum(data_structure):
    a = 0
    if isinstance(data_structure, int) or isinstance(data_structure, float):
        return data_structure
    elif isinstance(data_structure, str):
        return len(data_structure)
    elif isinstance(data_structure, list):
        for item in data_structure:
            a += calculate_structure_sum(item)
        return a
    elif isinstance(data_structure, tuple):
        for item in data_structure:
            a += calculate_structure_sum(item)
        return a
    elif isinstance(data_structure, set):
        for item in data_structure:
            a += calculate_structure_sum(item)
        return a
    elif isinstance(data_structure, dict):
        for key in data_structure.items():
            a += calculate_structure_sum(key)

        return a
    else:
        return 0
data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)

