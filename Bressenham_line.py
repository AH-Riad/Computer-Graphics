import matplotlib.pyplot as plt

x1, y1 = 2, 3
x2, y2 = 10, 8

x = x1
y = y1

dx = x2 - x1
dy = y2 - y1

p = 2 * dy - dx  

x_points = []
y_points = []

print("Step\tX\tY\tp")

for i in range(dx + 1):
    print(i, "\t", x, "\t", y, "\t", p)

    x_points.append(x)
    y_points.append(y)

    x = x + 1  

    if p < 0:
        p = p + 2 * dy
    else:
        y = y + 1
        p = p + 2 * dy - 2 * dx


plt.plot(x_points, y_points, marker='o')
plt.title("Bresenham Line Drawing Algorithm")
plt.grid()
plt.show()