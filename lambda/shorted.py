point2D = [(1, 3), (-1, 1), (3, -2), (11, 2)]

point2D_shorted = sorted(point2D, key= lambda x: x[0] )  # 0 for x index and 1 for y index
point2D_shorted_sum = sorted(point2D, key= lambda x: x[0] + x[1] )  # 0 for x index and 1 for y index


print(point2D)
print(point2D_shorted)

print(point2D_shorted_sum)