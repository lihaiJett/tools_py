data = (
    (15, 10, 0, 10, -15, 10, 9, 25, 0, 25, -10, 25,),
    (16, 10, 0, 10, -18, 10, 10, 19, 0, 19, -3, 19,),
    (16, 10, 0, 10, -19, 10, 10, 21, 0, 21, -11, 21,),
    (14, 10, 0, 10, -15, 10, 9, 27, 0, 27, -11, 27,),
    (13, 10, 0, 10, -17, 10, 14, 21, 0, 21, -16, 27,),
    (16, 10, 0, 10, -21, 10, 7, 27, 0, 27, -20, 27,),
    (14, 10, 0, 10, -15, 10, 9, 26, 0, 26, -14, 26,),
    (17, 10, 0, 10, -20, 10, 7, 21, 0, 21, -12, 21,),
    (16, 10, 0, 10, -22, 10, 12, 25, 0, 25, -19, 25,),
)


def c_t(p1, p2, p3):
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3

    return abs((x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) * 0.5)


def c_t2(p1, p2, p3):
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3

    return abs(((x1 * y2 + x3 * y1 + x2 * y3) - (x3 * y2 + x2 * y1 + x1 * y3)) * 0.5)


def c_three(d):
    d1 = (d[0], d[1])
    d2 = (d[6], d[7])
    d3 = (d[2], d[3])
    d4 = (d[8], d[9])
    d5 = (d[4], d[5])
    d6 = (d[10], d[11])

    # a = c_t(d1, d2, d3)
    # b = c_t(d2, d3, d4)
    # c = c_t(d3, d4, d5)
    # d = c_t(d4, d5, d6)
    # print(str(a) + "," + str(b) + "," + str(c) + "," + str(d))

    a = c_t2(d1, d2, d3)
    b = c_t2(d2, d3, d4)
    c = c_t2(d3, d4, d5)
    d = c_t2(d4, d5, d6)
    # print(str(a) + "," + str(b) + "," + str(c) + "," + str(d))
    return a + b + c + d


# print(c_t2((2, 3), (-5, -5), (4, -9)))
# print(c_t((2, 3), (-5, -5), (4, -9)))

# print("!!!!!!!!!!!!!!")
# print(c_three(data[0]))
for d in data:
    print(c_three(d))
