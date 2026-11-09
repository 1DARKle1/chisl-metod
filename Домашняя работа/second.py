import math

def relative_error(approx, exact):
    return abs(approx - exact) / abs(exact)

# 1
approx = 3.14
exact = math.pi
print(abs(approx - exact), relative_error(approx, exact))

# 2
approx = 0.1 + 0.2
exact = 0.3
print(approx, abs(approx - exact), relative_error(approx, exact))

# 3
approx = 0.0
for _ in range(1_000_000):
    approx += 0.1
exact = math.fsum([0.1] * 1_000_000)
print(approx, exact, abs(approx - exact), relative_error(approx, exact))

print("3.14 и pi: абсолютная 0.0016, относительная около 0.05%")
print("0.1+0.2: абсолютная около 5.6e-17, не ноль, относительная тоже мала")
print("миллион 0.1: абсолютная больше, чем у одного сложения, относительная меньше, сумма сама большая")
