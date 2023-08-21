
from canvas import Canvas


def main():
    c = Canvas(600,600)
    
    # p = point(50, 299, 0)
    # for min in range(60):
    #     m = dot(dot(rotation_y(2 * pi / min), dot(rotation_x(2 * pi / min), eye(4))), p)
    #     c[m.x, m.y] = color(255,255,255)        

    print(c.to_ppm())

if __name__ == '__main__':
    main()
