from ffield import FField

f = FField(p = 83, w = 19)

Xa = 15
Xb = 112

Ya = f.mod(Xa)
Yb = f.mod(Xb)

K = Ya ** Xb

print(f"{Ya = }, {Yb = }, {K = }")

# Ya = 76, Yb = 49, K = 48
