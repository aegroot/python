tabel = [[0, 156, 0, 0], [34, 0, 0, 0], [23, 123, 23, 0]]
pixel = 0
for rij in tabel:
    for i in rij:
        if i > 1:
            pixel += 1
print(pixel)
