import matplotlib.pyplot as plt

x1, y1 = 2, 3
x2, y2 = 10, 8

dx = x2 - x1
dy = y2 - y1

steps = max(abs(dx), abs(dy))

x_inc = dx / steps
y_inc = dy / steps

x = x1
y = y1

x_points = []
y_points = []

print("Step\tX\tY\tRounded X\tRounded Y")

for i in range(steps + 1):
    xr = round(x)
    yr = round(y)

    print(i, "\t", f"{x:.2f}", "\t", f"{y:.2f}", "\t", xr, "\t\t", yr)

    x_points.append(xr)
    y_points.append(yr)

    x = x + x_inc
    y = y + y_inc


plt.plot(x_points, y_points, marker='o')
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("DDA Line Drawing Algorithm")
plt.grid()
plt.show()