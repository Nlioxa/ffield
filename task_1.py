from ffield import FField

f = FField(p = 20, w = 8)

b = f.num(53)
c = f.num(35)

print("task 1: {0}".format(b + c))
print("task 2: {0}".format(b - c))
print("task 3: b = {0}\tc = {1}".format(f.find(b), f.find(c)))
print("task 4: {0}".format(b * c))
print("task 5: {0}".format(b / c))
print("task 6: {0}".format(b ** c))

# task 1: 21
# task 2: 18
# task 3: b = 3 c = 2
# task 4: 46
# task 5: 13
# task 6: 5
