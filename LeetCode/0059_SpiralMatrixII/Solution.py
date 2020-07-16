def generateMatrix(n):
    A, lo = [], n*n+1
    while lo > 1:
        print("lo:", lo, "len", len(A))
        lo, hi = lo - len(A), lo
        print("lo:", lo, " hi:", hi)
        A = [range(lo, hi)] + zip(*A[::-1])
        print(A)
    return A


if __name__ == '__main__':
    x = generateMatrix(3)
    print(x)

"""
('lo:', 10, 'len', 0)
('lo:', 10, ' hi:', 10)
[[]]
('lo:', 10, 'len', 1)
('lo:', 9, ' hi:', 10)
[[9]]
('lo:', 9, 'len', 1)
('lo:', 8, ' hi:', 9)
[[8], (9,)]
('lo:', 8, 'len', 2)
('lo:', 6, ' hi:', 8)
[[6, 7], (9, 8)]
('lo:', 6, 'len', 2)
('lo:', 4, ' hi:', 6)
[[4, 5], (9, 6), (8, 7)]
('lo:', 4, 'len', 3)
('lo:', 1, ' hi:', 4)
[[1, 2, 3], (8, 9, 4), (7, 6, 5)]
[[1, 2, 3], (8, 9, 4), (7, 6, 5)]
"""