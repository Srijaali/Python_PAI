datatype = [('name', 'S20'), ('height', float), ('class', int)]

array = np.array([
    ('Ali', 5.5, '10'),
    ('Babar', 5.6, '10'),
    ('Charlie', 5.7, '10'),
    ('Daniyal', 5.9, '10'),
    ('Esha', 5.3, '10')
], dtype=datatype)
print(arr)

sorted_array = np.sort(array, order=['class', 'height'])
print(sorted_array)
