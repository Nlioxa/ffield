from ffield import FField

f = FField(p = 67, w = 13)

b = f.num(53)
c = f.num(35)

print(f"task 1: {b + c = }")
print(f"task 2: {b - c = }")
print("task 3: J_b = {0}, J_c = {1}".format(f.find(b), f.find(c)))
print(f"task 4: {b * c = }")
print(f"task 5: {b / c = }")
print(f"task 6: {b ** c = }")


# task 1: b + c = 21
# task 2: b - c = 18
# task 3: J_b = 3, J_c = 2
# task 4: b * c = 46
# task 5: b / c = 13
# task 6: b ** c = 5
