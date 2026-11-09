# 1
def run(h, steps):
    x = 0.0
    for step in range(steps):
        gradient = 2 * (x - 3)
        x = x - h * gradient
    return x

def until_close(h):
    x = 0.0
    n = 0
    while abs(x - 3) > 0.0001:
        gradient = 2 * (x - 3)
        x = x - h * gradient
        n += 1
    return n, x

for h in (0.1, 0.5, 0.01):
    print(h, run(h, 20), until_close(h))

# 2
история = [120, 135, 128, 150, 145, 160]
прогноз = sum(история[-3:]) / 3
print(прогноз)

for i in range(3, len(история)):
    прогноз_дня = sum(история[i - 3:i]) / 3
    факт = история[i]
    print(прогноз_дня, факт, abs(прогноз_дня - факт))
