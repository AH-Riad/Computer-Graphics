import matplotlib.pyplot as plt

xc, yc = 0, 0   
r = 5           

x = 0
y = r

p = 3 - 2 * r   

x_points = []
y_points = []

def draw_circle(xc, yc, x, y):
    
    x_points.extend([xc+x, xc-x, xc+x, xc-x, xc+y, xc-y, xc+y, xc-y])
    y_points.extend([yc+y, yc+y, yc-y, yc-y, yc+x, yc+x, yc-x, yc-x])


print("Step\tX\tY\tp")

step = 0
while x <= y:
    print(step, "\t", x, "\t", y, "\t", p)

    draw_circle(xc, yc, x, y)

    if p < 0:
        p = p + 4 * x + 6
    else:
        p = p + 4 * (x - y) + 10
        y = y - 1

    x = x + 1
    step += 1


plt.scatter(x_points, y_points)
plt.gca().set_aspect('equal', adjustable='box')
plt.title("Bresenham Circle Drawing Algorithm")
plt.grid()
plt.show()