input = """6 * ((4 * 8 + 4) + (3 * 5 + 3 + 3 * 7 * 5)) + 7 + (9 * (6 + 9 * 7 + 2 * 6 * 6)) + 2
6 + 6 * (8 + 9 * 6 * 7 + 4 * 8) * (3 * 2 + 8 * (5 * 8 + 6 * 3 * 7 + 4))
((2 + 5 * 5 + 8 + 3 + 4) + 8 * 7 * 6) * 9 * 8 + 2
(2 + 7 * (3 + 5 * 2 + 3 + 6) * (4 * 6 + 8 * 3 * 2 + 7)) + 3 * ((2 + 8 + 6) * 8 + 9 * 6 * 6) + 5 + 6 + 5
((5 * 8 * 4 + 6 * 9) + 2 * 7 + 2 + (6 * 7 + 6)) + 6 + 6 * 9 * (2 * 8 * (3 + 7) * 9) * 7
6 * 4 + 8 + (2 * (4 * 3 * 7 * 4) * 3)
6 + 8 + ((3 + 7 + 4 + 9 + 6) * 7 + 9 + 2 * 4 * 6) * (3 + 6 * 5 * 2 * 4) * 3 + 9
(5 * 5 * 5 * 7 + 9) * 7 * 5
9 + 5 + (2 + (2 * 3 + 5 * 9) * 6) * 2 * (2 * (4 + 5 + 2 + 9 + 3))
8 + 7 + (2 + 4 + 5 + 9) * (7 + 4) * 7
9 * (3 + 9 + 5 + 7) * 5 + 6
2 + 3 + 4
8 * 4
6 * 4 * (2 * 7 * 7 * 2) * 4
2 * (6 + 5) + 5
(5 + 6 * 2 * 3) * (3 + 8 + 4 + 2 + 6) * 8
((7 + 7 * 3 + 3 + 7) * 3 + 7 + 2 * (3 * 8 * 2 + 2 * 7 * 4) + 9) + 4 + 3 * 7
6 + 8 + ((4 + 9 + 5 + 9 + 5 + 6) * 6 * (3 * 5 + 2 * 8) * 9 * 5 + 9)
(4 * 2) + 7 + 9 + 8 + ((2 * 9 * 4 + 3 + 7 + 8) + 7 * 9)
2 * 3 + 3 * 8
9 * 6 * 3 * 8 * ((8 * 4 * 2 * 6) + 3 * 8)
7 * 8 + 5 * 8 * 9
7 * ((3 * 3 + 4 + 4) * 3) + 8 + 7 + 2 * 8
2 * (9 + 9 * (8 * 9))
(8 + 6 + 9 * (5 + 5 + 5) * 6 * 9) * ((2 + 7 * 6 + 2) + 4 * 9 * 8 * (5 * 2 + 5 + 2 + 5))
(6 * 9) + 5 * 8 * 8 + 8 * (7 + 4 + 6 * (9 * 9) + 8)
2 * 9 + 3 * ((3 * 7 * 4 * 3 + 3 * 8) * (8 + 6 + 3 * 8 + 6) + 5 + 3 + 7 + 5) + 9 * (3 + 3 + 6 + 4)
((9 + 2 * 7 * 8 + 7) + 3 * (6 + 9 * 3)) + 7
4 * (8 * (6 + 3 * 4))
4 + 3 + 7 + 4 + 2 * 7
7 * 8 * 5 + 7
(7 * 9) * (2 * 9 + 5 + (5 + 2)) + ((9 + 7 + 9 * 7 * 4 + 8) * (6 * 7 + 4) + 3 * 7 + 4 * 8)
(8 * 6 * 9 * 7 + 2 * 2) * 8 * 2 * 9 + (8 + 9 * 7 * 8 * 7) + (5 * 5)
9 * 4 + 8 + (8 * 6 * 4 + (5 * 6 * 3 * 6 + 3) + 5) * 9 + 4
7 * (7 * 8 * 9) * 2
(3 + 3 + (8 + 5 * 6) + 7 + (9 + 8 + 2 * 3 * 9 + 2)) + (3 + 4 + (9 * 5 * 2 + 2 + 8) + (4 * 3 + 4)) + 8 * 6 * ((9 + 8) + 9 * 3)
3 + 2 + 7
(6 + 6 + 6 * 3 + (5 + 5 * 4)) * (3 * (9 + 2 + 4 * 5 * 3 * 3)) + (3 + 6 + 6 + 5 + 6 * 8)
(9 + (9 * 7 + 7 * 4 + 2) + (8 * 8) + 5 + 9 * 2) * 5 * (5 * 9 * 5 + 8 * 6)
2 + 5 + (2 + 2 + (7 * 2 * 7)) * (2 * (6 * 5 + 9 * 4)) * 4
5 + 7
7 + 5 * 4 * ((8 + 6 + 9 * 7 * 7 + 6) + 3 + 3 + 5) * (8 + (4 * 2 * 9) * 5 * 6 + (2 * 8 + 2 * 7)) + 8
6 * 7 * (2 * 3) * 3 * 3
6 * 3 + 8 * (4 * 7 + 9) + 4 * 7
4 + 2 + ((3 + 7) + (4 + 9))
4 + 8 * 6 * 5 * 7 + (7 * (8 + 5 + 5 + 2 + 3 * 5) * (6 + 3) + (2 * 3 * 5 + 4))
4 + (7 * 7 * (5 * 4 + 8) * 2) + 8 * 3
(4 * 9 * 8 * 9 * (6 * 7 + 2 * 5 + 6)) * ((4 + 2 * 5 + 9 * 9) * 3 + 8 * 2) + 9 + 9 + 2
4 * 5 + 9 * (4 * (8 + 8 * 5))
7 + (7 * 5 * (5 * 6) + 2 * 2) + (6 * 3 * (7 * 9 + 2 * 6)) + 5 * 7 + ((7 * 4 * 4 + 8 * 8 * 6) * (8 * 8 * 7 + 9 * 3 + 2) * 2 * 5)
(8 + 3 * 6 * 6 * 2 + 4) + 4
9 * 8 * (9 + 8)
((9 * 4 + 5 + 5) + 2 + 8 * 6) * 6 * 5 * 9
(7 * 3) + 3 * 8 * 3 * 7 + 8
8 + (9 * 7 * (6 + 2)) * 9
((6 + 9 * 2 + 7 + 4) * 5) * 7 + (6 + 3 * 9 + 5 + 9 * 4) + (3 * 6 * 3 + 8) + ((4 * 3 + 2 + 2) + 9 * 5 + 5 * 5)
(8 * (8 * 6 + 2) * 4) * 4 * 6
2 + 9 + (3 * 9 * 4 + (7 * 7)) + 7
(2 * 3 + 2) + ((8 + 4 + 6 * 7 * 8 * 3) * 8 + (3 + 2 + 3 * 8 * 6 + 3) + 8)
2 * (9 * 7 * (4 + 5 + 8)) + (3 + (7 + 2 * 6 + 2) + 7 * 2 * 9 * 7) + 2 * 4 * 3
5 + ((9 * 6 * 6) + (6 * 6 + 5) * 2) * 9 + 7 * ((8 * 8 * 2 + 2) + (4 * 9)) + (7 + 2 * 4 + 7 + 6)
((7 * 9 + 8 * 6 * 4 + 8) + (9 + 9 + 6 * 4) + 6) * 3 * 8
2 * 5 + 6 + 7 * (6 * (7 * 5 + 2 * 2) + 7 * 8)
4 * (4 * 4 * 2 + 3 * 9 + 7) * 7 + 6
7 + 3 * 4 + 2 * 8
6 + 3 * 8
5 + ((6 + 2 * 3 + 4) + 8 + 4 + 5 * 6 * 6)
(2 + (6 + 3 + 4 + 9) * (7 + 3 + 2 + 7 * 9) + (2 * 2 * 7 + 9 * 7) + 4 + 4) + ((5 + 5) + 4 + 5 + 2 * 2) + 2 + 4 * 6
(5 * (4 + 4 * 5 * 7 + 9 + 6) * 9) * 6 + 2
(6 + 2 + (8 * 9 + 2) + 8 + 5 + (7 + 2)) * 6
(9 * 3 * (8 * 7 + 6 + 7 * 3)) + 3
(4 + 4 + 2 * 9 + (5 * 9 * 3 + 7) + 9) * 2 + 6
4 * ((9 * 3 + 9) + 4) * 9
(5 + 3 + 4) * ((5 + 4 + 3 * 6) * 7 * 2 * 6 * 8) + 3 * 9 + 7 + 5
(3 + 4 * 8 + 8 + 3) * 4 * 7 * ((7 + 8 * 3 + 7 * 7 * 8) + 2 + 4 + (7 + 6 * 4) + 2 * 6)
4 * (8 + 2 * 8) * 6 * 7 * 9 + 5
5 + 3 + 6 + 8 * (2 + (4 * 5 * 2 + 9 * 9))
(3 + 6 + 5) * 2 * 9 + 3
(7 * 5 * 2 * 2 + 5) * 6
7 * 8 * (3 * 5 + (4 * 7) + 6) + 6 + (5 * (7 * 3) * 3 * 5) * 6
(8 + (6 + 2 * 2 * 6) + 3 + 9 + 5) * 3 + 6 * 7 + 4
(5 * 8 + (8 + 6 * 7 * 7 * 3)) + (6 + 7 + (5 + 7 + 7 + 4 * 8) + 8 * 5 + 2) * (5 + (5 * 4 * 9 + 7 * 9 * 6))
9 * (9 * 2) * 2 * 5
2 + 3 * 8 * 6 + 7 * 2
4 + 2 * 6 * 5 * 6 + (4 + 7 * 6 * (2 * 7 + 5 + 6 * 7 + 6))
((4 * 6 + 5 + 5) * 5 * 4 + 8 * 8) * 3 + 5
8 * 5 * 5 * (3 * 8 + 3 + 5 + 9 * (5 + 4 * 5 + 3 * 2))
8 + 4 * 7 * 3 * 4
(9 + 4 * (5 * 7) + 6 * 8 * (8 + 7 + 9)) + (2 * (4 + 8 * 3)) * 7
((6 * 6 + 3 + 9 + 6) + 3) + ((9 + 2) + 6 + (2 + 7)) * 5 * ((3 + 2) + 9 * 2)
(6 * 7) + 8
(5 * 3 + 8 + (9 * 4 * 4 * 3 * 9 + 2) * 6) * 8 + 4
8 * 7 + (6 * 8 + (8 + 2 + 8 * 3 * 9))
8 * (3 + (8 * 6)) + (2 + 5 + 8 * 3 + 8 * 9)
((9 * 3 + 9) + 8 + 7 * 9) + 5 * (4 + (6 * 7 * 8) * 4 + (5 + 6 + 6 * 2) * 3 * 5) + 8 + 5
4 + (2 + 3 + 5 + (8 * 2 + 7) + 3) * 8 * 3 * 3 * 2
5 + 2 * 6 + (5 + (2 * 5 * 7 + 6) * 5 * 4 + 4) + (2 + 5 * 9 * (2 * 5 * 2 + 5 * 2)) * 6
9 + 5 + 5 + ((7 * 4) * 6) + 3
(2 * 4 + 6 + (6 * 5 * 6 + 5 * 3 * 5) + 4 * 4) * (3 + 5 + 8 + 3 + (5 * 8 * 4 + 4 * 6 + 5) * 8) * 4 + (3 + 6 + 9 + (4 + 6 * 7 * 2 + 5) + (3 + 2 + 8 * 9 * 9))
(2 + 9 * 7) + (2 * 4 * (7 + 3 * 2))
(8 * 4 + 3 * 3) * 9 * 8
(4 * 3) * 6 * 5 * 7 + (4 + 7 + 4 * 6 * 9 * 6)
(7 + 4 + 9 + 7) * 3 * (2 * (7 * 5 * 7) * 5 + 9 * 4 + 3)
2 * 4 * 9 * 7 + (3 * 6 * 5 * 7 + 4)
5 + 5 * 2 * 3
5 + 6 * (8 * 9 + (4 + 7 * 6 + 5 * 8 + 8) + 9 * (2 + 7 + 6 + 5)) + (4 * 4 + 7 * 3) + 6
5 * 8 + 6 + (9 + 3 + (5 + 3 + 2 + 9))
4 * (7 * 2 * 6 * 2 + 6 * (5 + 3)) * (2 + 5 * 5 * 3) + (7 * 7 + (7 + 6) * 5 * 6) * (4 + (3 + 4) + 4 * 5 * (5 + 4 * 9 * 7 * 9 * 6))
(5 * 8 + 3 * 3 + (3 + 8)) * 9 + 3 + 4 + 4
2 + 5 * 2 * 5 * 8 + 6
4 * 7 * 5 + ((2 + 3 + 9 * 4) + 4 * (4 * 2 * 4 + 9 * 7)) * 6
(4 * 5 * 3 * 5) * 3 + 8 * 4
7 + 4 + (6 * (4 * 4 + 7)) + 5 + 9 * 3
(3 * 8 * 7 * (2 + 6) + (8 * 9 + 8 + 3 * 2) + 6) * 2 + 3 * 8
(6 + 9 * 4 * 4 * 9 + (4 + 7 + 7 * 7)) + (4 * 3 * (6 * 7 + 4 + 5 + 8) * 7) * ((5 * 7 * 5 * 9) + 4 + 4 + 8) + 3
8 * 5 * (5 * 8) * 5 + 8 + 9
3 + 7 + (5 + 4) + ((9 * 8 * 4 + 7 + 7) + 6) * (8 + 8 + (4 * 4 + 8 + 4 + 8) * 8 + 2 + (4 * 7 * 4))
9 * 3 * 5 + (3 + 3 + (4 + 8 + 6 + 4 + 9 * 2) + 7 * 7)
((9 * 7 + 8 * 6) + 3 + 2 + 8 + (6 * 6 + 7 * 4) * 6) * 4 + ((8 + 6 * 4 * 7 + 3 + 6) * 6 + 3 * 6 * (5 + 8 + 8 * 6 + 2 + 3)) + 9 + 9 + 6
7 + 3 + 8 + (9 * 2 + (3 * 3 + 6 + 4)) + (6 + 7 * 3 * 2 * 9 + (4 + 5 + 6 + 9 + 2 + 4))
(7 + 5 + 6) * 2 * 7 * (3 * 5)
(6 * 5 * 9 * 4) * 9 * 2 + 3 * 7 * 5
8 * (2 + (4 + 8 * 5 * 7) * 3)
(6 + 2 + 8 * 3 * 8) + ((9 + 8 + 8 + 9 * 3) * (3 * 4) * 2 * 4 + 6 + 5) * 5 * 6 * 4 + 7
(2 * 6) + (7 + 8 + 3)
5 + 4 * 7 * 3 * (3 + 3 + (2 + 3 * 8 + 4) + 9 + 3 * 3) + 3
9 * ((8 * 5 * 8 + 7 + 2) * (6 + 2 * 9) + 2) * 7
(6 * 8 * 8 * (4 + 5 + 3 + 4)) * 9 + (2 + 4 + 2 + 8)
(8 + (2 + 3 * 7) * 5 * 6 * 3) * 5 * 7 + (7 + (7 * 8 * 4 * 5) * 5 * 3 * 4 * 8) + ((2 + 6 * 9 * 2 + 8) + 7 * (5 * 8 * 5 + 6 + 9)) * 2
4 * 6 + 3 + (5 + 5) + 2
5 + (7 + 2) + 7 * 7 + (2 + 5) * 3
(9 + 4 * 7 + (7 * 2 + 8 * 8 * 8)) + 2 * (7 * 9 + 7 + 6) + 5 + 5
9 * 9 + (8 + (8 + 7 + 8 + 2 + 8 + 5) + 6 * 2 * 5 * 6) + 3
6 + (9 + 5 * 3 + 6 + 8) + 3
2 * 4 * 2 + 9 + 3 * ((8 * 6 * 9 + 7 * 6) * 3 * 2 + 9 + 9)
6 * 3 + (4 + 8 + (3 + 5 + 5) * 6 * 2 * 3) + 6 * 5 + 9
(7 * 8 + 9) * 7 * (6 + 5) * (4 + 8 * 5 * 6 * 9) * 4
5 * (7 * 3 + 3 * 4 * (2 * 3 * 9))
6 + 6 * 3 + 7 * (4 + 4 * 5) * (6 + 2)
7 + 8 * 9 * 3 * 8 * 2
3 * 2
8 * ((3 * 4 * 3) * 9 + 9 + 9) * 2 * 4 + 6 * 4
3 + (4 + 5 + 5) + 4 + 6
(4 * 7 * 5 + 8 * 7) * 4 * (6 * 6 + 4) * 4 + (2 + 7 + 2 + 8 * 6)
(2 + 2 + 8 + 9 * 9) + (9 * 4 * 2 * 9) * 9
(8 * (2 * 7 + 9) * 4) * 4 * 5 + 2 * 8
((7 + 8 + 6) + (9 + 8 * 7) + 6 * (5 * 8)) * 4
4 + (3 + (5 + 2 * 3 * 3 * 3) * 2) * (7 + 2)
5 + (5 + 3 * 4 * 6 + 6)
(4 + 4) + 7 + 8 + 6 * 5
5 * (6 + (6 + 6 * 2 + 9) + 8 * (2 * 6)) * 6 * 9
(4 + 7 * 6 * 9) + 6 * (9 * 7) * 4 * ((6 + 7) + 5 + 9 * 5 * 5 + 2)
(4 + (6 + 8 + 4 * 9) * 8 + (5 + 3 + 7)) + 2 * 3 * 9 * 3
9 * 9 + 9 + (4 * 9 * 3 + 4) * 9 * 6
2 * (6 + (8 + 7 + 6) * 9 * 6 * (2 * 8 * 3)) * ((9 * 7 + 6 * 3) * 8 * 5 + 8 + (7 + 7 + 7 * 5) * 5) + 2
6 + (7 + 8 * (5 + 4 * 3 * 2 + 2)) + (4 + 8 + 5 + 7 + 7 * (7 * 6 + 2 * 8 * 6 + 4)) * (6 * 9) * 9 * 9
7 * (5 * 7 * 5 * (7 + 7 + 9 + 5 * 2) * 3 * 3) * (4 * 9)
7 + 2 * 9
(9 + (6 + 3)) * 3 + 9 + 3 * 9 * (8 * (4 + 3 * 9))
7 + 2 * 4 * 5 * (6 * 5 + 3 * 3 * (5 * 8 + 7 * 5) * 7)
6 * (6 * 6 + 5 * 2) + 8 * ((4 + 2 * 7 + 9 + 9) * 4 + 5 * 5 * 2) * 3
3 * ((7 * 2) * 2 + 5 + 3 * 2 + 5)
9 * (4 + 3 * 6 * 4 * 6 + 3) + 7
2 * 8 + (2 + 9) * 8 + (9 + (5 * 8) + 2) * 6
(4 + (2 * 7 * 8 * 5 * 9) + 6 + (8 + 2 * 9 + 6) * 5 + 8) + 7 + 7 + 7
8 + (3 + 7 + 5 * 8) + 2 * (4 * 3)
9 + (2 * 5 * 2) * (2 + 4 + (4 + 4 * 7 * 9) * 6 + (8 + 9 * 3)) + ((2 * 7 * 8 + 5 * 5 + 5) * 6 * 9 + 5 * 9) + 2
7 + (4 + (2 * 4 + 6 + 3 + 8 + 5) + 2 * 5 + 3)
(7 + 4 + 9 * 7 + 2 + (5 * 8 * 8 + 2)) + 2 + 7
8 * (8 + 4)
5 * (3 + 8 * 4)
8 + (5 * 4 + 3 + 5)
3 * 5 * 9 * 5 + 8 + 8
2 * 4 * ((3 * 3 * 7 * 2 + 7) + 9) * 4 + 3
9 + 8 + (4 + (6 * 4 * 3 * 8) * (8 + 6 * 3) + 7)
3 * (3 + 6 * 7 + 8 + 4 + (5 * 4 + 3 + 4 * 6)) * 4 + 3 + (5 * 3 + (8 * 8 + 6 * 3 + 6 * 9) + 2 + 9)
(5 + 5 * 7) + 3 * 2 + (8 * 4 + 3 + 4)
(7 * 8 * (2 + 6 + 8) + 6) * 5
7 * 8 + ((6 * 9) * 5 * 5 * 9 + 9) + (7 + 8 + 2)
8 * 4 * 4 * (7 + (5 * 4 * 4) + 3 * (4 + 8 * 7) * 2 * 9) * (4 + 5) * 6
(2 * 3 + (3 * 4 + 7 + 5 + 2 + 2) + 7) + 7
(6 * (8 + 6 * 3 + 7 * 4 + 7) + 2 + (5 + 2 + 2 + 5 + 4 * 7) * 6 + (2 + 4 * 7)) * 3 + 7
3 * (2 * 8 * 7 + 6) * 8 + 7 * ((7 + 2 + 3 + 2) * 8 + (3 * 2 + 7 * 7 + 8 + 3) * 8 + 3 + 9) * 2
(9 * 2 + 4) + 4 * (7 * 2 * 5 * 3 * 6)
(3 + 9 + 2 * 5) * (6 * 6) * 9 * (4 + 7) * 9 * 7
(5 + 8 * 6 * 5) + 6 + (3 + 9 * 8 * 2) * 7
6 + ((9 + 7 + 2 * 7 + 2 + 7) * (5 + 5 * 8 + 9 + 3 + 4) + (9 * 7 + 7 * 7 + 9) + 4 * 6 + 6) + 6 + 2 * 3
(4 + (4 + 4 + 7 + 5 + 8)) + (7 + (2 * 8 + 4 + 6)) + 8 + 8 + 2
7 * (4 * 8 * 5 * (4 * 3 * 4 + 2 + 7) + 6 * 6)
9 * 4 + 4 + ((9 + 3) * 5 + 5) + 6
(4 * 9 + 3 + (9 * 6 + 4 * 6 + 3) * 8) + 3 + 9 * 4 + 8 * 6
(3 + 3) + 8 * 4 * 6
8 + 7 * (4 + 4 * (6 + 3 + 3 + 4 + 7 + 4) * (2 + 8 + 9 * 4 * 7) * 4 * (7 + 2 * 6 + 8 * 2 + 5))
6 * (2 + (4 * 9 * 8) + 8 + (8 + 6 + 3 * 8 * 5 * 7) + 9) + 8 * 9
(8 + 5) + (4 * 5 * 2 * 2 + 4 + 6) + (8 + 7 * 2)
9 * (7 + 3) * 7 * (6 * 9 + 4) * 4
2 * 4 + (9 + 8 + 3 + 5 + 9 + (4 + 7 * 6 * 7 + 9)) * 9 * 3
9 * (7 * 3) + 4 * 7 + 2
7 + 9
2 * (7 + 7 + 4 + 9 * 5) * 8 + 3
3 + 9 * 7 * (7 * 8 * 5 * 3)
((4 + 6 + 6 * 9 * 9) + 2 + 8 + (5 + 8 + 2)) + 5 * 5 + 7
(9 + 9) * (6 + (5 + 7 + 3 * 4) * 7) + (4 * 7 + 2 + 9 + 9) * 9 + (8 * 4 * 2)
5 * (7 * 5) * 3 + 3 * 5 + 7
9 * ((9 * 4 + 2 + 6 * 2 * 5) * (8 + 7) * 7 * 7 * 8 + 9) + 7 * 9 + (8 * 8 + 4 * 4 * 4)
9 * 9 + (4 + 9) + 7 + (5 * (7 + 7 + 9 + 4 * 4) * (5 + 9 * 7 + 5 * 9 * 2) + 7 + 2)
7 + 8 + 4 + ((3 + 4) * 2 + 3 * 5 + 9 + 6) * 6 * (9 * 6 + 9 * 8 * 5 * 8)
4 + (4 + 7 * (5 * 6 * 3 * 9 + 8) * 4) + 6 + 6 * ((8 + 7 * 7 + 5 + 2) + 3 + (8 + 3 + 3 + 2 * 9 + 7) * (8 + 5 + 7 * 9 + 2) + 6 + 5)
8 * 8 * 9 + (3 * 4 * 4 * 7 * (8 * 2 * 3 + 3)) * 2
((4 * 5 * 4) + 3) + 6 * 6 * 4 * 5
3 * 3 + 5 + (7 + 3) * 9 * 6
((7 * 3 * 7 + 3 * 7) + 4) + 2 + 4 + 7 + 8
6 + (8 * 9 * 6 * 3 * (5 * 9 + 7 * 5)) * (6 * 6 + 7 * 7) + 2 + 4 * 3
(2 * (8 * 2 * 3 * 3) * 3) * (2 + 5 * 9) + ((9 * 6 + 6 + 8 + 3 + 6) + 3 * 5 + (3 * 8 + 8 * 2 + 9) + 3 + 6)
4 + 5
(7 * (6 * 9 + 5 * 6 + 3) * 3 * (3 * 7 * 2 * 3 + 7 * 9)) * 9
(8 + 2 + 9 * 6 * (9 + 5 + 4 + 2) * 5) * 9
(6 + 6) + (7 + 9 + 8) + (7 + 3 * (6 + 2 + 8 * 5 * 7) + 7 * 3 + 7) * 3 + 3 * 6
6 * 8 + ((6 + 4 * 3) + (3 * 2 + 4) + 9 * 7) * 4
(7 * (2 * 4 * 5 + 9)) + 9 + (8 * 2 + (2 * 4 + 9 * 2 * 5) + 3 + 6 + 8) * 9 * 8
8 * 7 * 8 * (4 + 4)
(4 + 8 + (8 + 7 * 3 + 4 * 2 * 7) * 5 * (9 * 9 * 7 + 3 + 9 + 5)) * 9 + 4 * 3 * (8 + 7 + (9 * 2)) * 3
6 * 5 * 8 + (2 + 3 * 7 * 4 * 2)
2 * (7 * 7) * (6 + 7 + 2 * 3 * 7) * 2 * 5 * 7
7 * 2 * (3 * (2 * 5 * 7 + 3 * 8)) + (9 * (6 * 6 * 7 * 3) + (4 + 3 + 2 + 9 * 8) + 5 * (7 * 2 * 3 * 8 + 5 * 7)) * 8
((2 * 7 + 5) + 3 * 2 * 7) + 4 * 8
4 * (4 + 6) + (4 * 2 * 8 + (3 * 8 + 4 * 8))
3 + 3 * 8 * 6 + (4 + (5 + 5 + 6 + 5 * 5) * 3 * 8 * 4) * 5
9 + 9 * (5 + 7 + 7) * 5
(5 * (7 + 6 * 9 + 6 * 9 + 5) + 3 + (4 * 8 + 5 * 8 * 3) * (9 * 9 + 2 * 2 + 2 * 8)) + 7
((6 * 8 + 5) * (6 + 6 * 4 * 7 + 5 * 5) * 7) * 5 * 8 + 2 * 6 * 8
(3 + 7 + 2 + 2 * 2 + 6) + 4 * 2 * 3
5 * 2 * (7 * 2 + 2 + 8 * 2) + 4 * 4
2 * 6 * 9 + (9 + 2 + 6)
7 * (4 + 7 + 4 * 4) + 8
6 * 8 + 9 * 7 + (2 * (6 + 8 * 5 * 9 * 3 * 6) + 7)
4 * 9 * (4 + 9 + 8 + 7) + 7 + 4 + 7
((8 * 8) * 6 + 6 * (7 + 8) + 3 + 9) + (2 * 9 + 2 * 3 * 7) + (7 + 2 + 5) * 5
9 + 9 + 5 * (8 * 7 * 4 + 8 + 8 * 4) + 4
(2 + (4 + 3 + 7) * 8 + 2) * (7 * 8 * 4 + 5)
7 * (7 * 5 * 8 * (5 + 8 + 6 + 9) * 6 * 6) * 3
(6 + 7 * (6 + 9) + 3 * (2 + 9 + 5) * 5) * 3 * (3 * (4 * 6 + 4 * 5 * 5))
8 + 7 + 4 + (5 + 7 + 9 + 8) + 4 * (4 + 2 + 7)
4 + 2 * 6 + (9 * (3 + 5) * (2 + 7 * 6 + 8 + 8) + 6 * 8 * 7) + 7
(2 * (9 * 2 + 8 * 3 + 2) + (7 * 3 * 5 * 6)) * 2 + 9 + 7 + (4 + 7 * 8 + 9 * 3) + 8
6 * (9 * 8 + (5 + 2 * 5 + 2 * 6 + 6) * 8 + 2)
8 * 2 + (7 * 7 * (9 * 6 + 3)) + 7 + 5 * 4
9 + 3 + 7 + 9 + (5 + (7 * 4 * 6 + 3 + 7 + 3) * 8 + (9 + 4 * 8 * 7 * 7) + 2)
((4 * 4 * 8) + 6 * 4 * 7 + 4 * 7) + 7 * 8 + 3 + 8 + 9
6 * (5 + 2 * (4 + 3 * 5 + 6 * 2 + 6) * 5 * 4 + 4) + 4 + (9 * (7 * 5 * 2 * 4 + 5) + 8) * (5 * (2 + 2) + 7 + (6 * 4 + 3 * 7 * 9))
2 * (7 + 9) * (2 * 2 + 4 * 7 * 6) * 5 + 5 * ((5 * 8 + 3 + 9 * 3) + 6 * 4 + 9)
(4 * 3 + 5 * 7 + 3 + 3) + (3 * 8 * 3 * 4 * 4) * 8 + 5 * 8
6 * 4 * (4 * (3 + 6) + 2)
9 * (7 + 8 + 5 + (9 * 9 * 8 * 6 * 5) * 9)
(6 * 7) * 5 + 5 + 7 + 3 + ((4 + 7 * 5 + 6 + 7) * 3 + 4 * 4 + 3 + (6 + 2 * 3 * 2 + 4 + 8))
3 + 4 * 2 + 2 * 7
(7 * 4 + 9) * 9 + 6
2 * (4 + 7 + 6 + 2 + 5 + 2) * 3 * (5 + (9 * 8) + 4 + 5)
2 * (6 + 5 + 8 * 5 * (7 * 3 * 7 * 7)) * 8 + 2 + (3 + 7)
((3 * 8 + 7 * 8) + 5 * 2 + (7 + 4 + 8 * 3 * 6)) + (5 * 2 * 3 + 2 * 2) + 2 + 5 + 3
3 * 5 * 9 + 4 * ((5 + 5 * 4 * 3) * 5 + 8 + 5)
9 + 7 + (8 + 2 + 4 * 8 + 8 * 3) * 5
(4 + 6 * 4 + 7 + 9 + 9) + 5 + 5 * 5 + (4 * 8 + 2) * 2
(9 + 2 * 8 * 8) + 6 + (6 + 5 + 3) + (8 + 8 + 4) * 7
2 * (9 * 9 + 9 + 7) * ((5 + 9 * 9 * 8 * 4 + 5) + 8 * (3 * 6) + (9 * 9 * 2)) + 6 + ((7 + 9 + 3 * 3) + 4 + (3 * 6 + 2 * 8))
((6 * 5 + 7 + 8 * 9 + 4) + 4) * 6 + 4 * (5 + (7 * 9 + 7 + 9) + 7)
(9 * 3) * (3 + 2) + ((7 * 5 + 8 * 7 + 5) * 2) + 4 + 8
(8 * (4 * 2 * 8 + 6 + 6) * 9 * (8 + 9 + 9 + 7 * 7 * 2) + 2 * 5) + (4 + 3 + 9) + 4 * 2 * 7 + 5
5 * 6 + 9 + 6 + (9 * 7)
(7 * 9 + 9 + 8 * 4) + 5 * (2 + (4 * 5 * 5 + 8) + 3 * 6 * 5) * 7
2 + (9 * 2 * 4 + (8 + 6 * 6 + 6 * 4)) * 7
4 * 5 + (2 * 4 + 6 + (8 * 2) * 9 * 2) + 9
6 * 2 * (7 + 5 + 4 * 3 * 2) * 8
(6 + (5 * 2 * 9 * 6 + 4) + 8) + 7 * 2 * 9 * 8
(8 * 8) * ((9 * 4 * 2 * 4) * (2 + 7) + 6 * 7 * 5) + (9 + 6) * 3 * 6 * ((5 * 5 * 3 + 6 * 5 + 4) + 5 + 5)
5 + 3 * 8 + 7 * 2 + (3 + 3 + 4)
2 * 2 * 3 + 4
(6 + 5 * 3 + (7 * 2 * 8) * 4 * 4) + 2
4 + (2 + (9 * 8) * 2) + (6 + (6 * 3 * 2 * 5 + 4 + 2) + 2 + 8 * 2)
((3 + 9 + 9) + 3) * (3 * 4 + (3 * 8 * 3) + 3 * 4 + 5) + 3 * 5 * 9 * 5
(9 * 7 * 4 * 5) * (9 + 6) + (5 * 4 + 7 * 6 + 9 * 4) * 5
8 + ((2 + 5 * 2 + 4 * 4 + 5) * (2 + 4 * 6 * 8) + 3 * 7 + 8) + 3 + 6
(4 * 6 + (2 + 9 + 5 + 4 * 7 * 2)) + 4 + 9
3 + 6 + 9 * (7 * 6 + 5) * (6 * 7 * 3)
(2 * 6 + (2 * 8 + 2 * 8)) + 4
6 * 4 + 3 * 7 * 9 * (9 * 2 + 6 + 2)
(8 + (8 * 6 + 5 * 3 + 9)) * 4 * 9 + 4 + 5
(8 * 9 * 8) + 7 * 4 * 3 + 5 * (3 + 8 * 2 * 9 * 7 * 8)
5 + 6 + 8 + (4 + 4 + 4 * 5 + (9 * 2 + 6) + 5)
2 * (8 * 5 + 7 + 7 + (3 + 2) * 4) * (9 * (2 + 8 * 7))
(2 * (4 + 7 + 9) * (2 * 3 + 5 * 9 * 5 + 4) * 6) + 2
2 * (5 * 2 + (9 + 8 + 9 + 9 + 6) * 5) * 9 * 8 + 3 * (2 * (3 * 9) * 7 * 4 * (5 * 7) * 6)
(5 + 3 * 4 + 9) + 2
((3 * 9) * (8 + 3 * 3 + 2 + 2) * 3) * 9 * 7 + 4 + (3 + 9 * 3 + (2 + 6 * 7 + 8 + 9) * (6 * 6 + 2 + 3 + 2)) * 8
8 * (3 + 9 + 5) * (5 * (3 * 4 * 7 * 3) * 2 * 8) * 7 + (6 + 6 + 5)
9 + (8 + 2 * 3 + 7 * 3) * 5 * 5 + 7 * 4
6 * 9 + (9 * 5 + 7 * (4 * 5) * 2) + 9 * 4 * 5
8 + 3 + (4 * 6 + (9 * 2 + 4 + 4 + 4 + 8) + 3)
(3 * 6) + 2 * 9
8 * 6 * (2 * 7 * 5 + (8 + 6 + 6) * 4 * (4 * 8)) * 7 + ((4 * 3 + 5 + 2) * 6 + (2 + 6 * 6 * 8 + 8) * 9) + 7
(9 * (7 * 9) * (9 * 8 + 5) + 8 + (2 + 8 * 6 * 9) * (3 * 5 * 7 * 6 + 2 + 4)) + (8 * 9 + 7 + (3 * 5 * 2 * 4 + 9 * 8)) + 6 * 5
(7 * 8 * 2 * 4) + 7 + 8 * 8 * 6 * (6 + 2 * (5 * 2) * 4)
8 * (5 * 4 + 4) * 3 + 4 * 4
7 + 8 + 5 + ((3 * 2 + 3 + 4 * 8) * 7 * 5)
((9 * 7 * 6) + 7) + 7 + 3 + (4 * (2 * 8 * 7 + 2 + 9) + (4 + 2 * 3) + 2 + 4)
(6 + 3 * 6) * 9 * 7 * (4 * 8 * 2 * (5 * 8 * 9 + 4 + 2)) + 3
3 * 7 * 7 + 9 * 9 + (7 + 6 + (3 + 6))
5 + 8 + ((8 * 8 * 4 + 5 * 3 * 5) * 4 + 4 + (5 * 5 * 2)) * 4 * 5
2 * (5 * 4 + (3 * 9 + 9 * 9) * 9) + 6 + (3 * 3) + 9 * 7
6 * 5 + (6 * (8 * 5) * (9 + 7 * 6 * 5) * 9 + 3 * (6 + 9)) + 8
4 + 9 + (5 * 9 + (7 * 6 * 3 * 8) + (8 + 2 + 7 * 5 + 3) + (4 + 7 * 7 + 7) + 9) + 7 + (7 + 2 + 8 + 4)
((6 + 4 * 4 + 5 + 7 + 7) * (8 * 2) * (6 + 3) + (9 + 3 * 4 * 7 + 4 + 9)) + 5
(6 * 2 * 3) + 8 + 9 + (3 * 3 * 2 + 8) * (3 * 9 * 7 + 5 * 5)
7 * 5 * (9 + 5 + 3 * 7 + 8 * 4) * 3 + 2 + 4
(8 + 9) + ((5 * 5 + 5 * 3) + 2 + 8 + 9) * 4 * 2 * 4 * (5 + 4 + 2 * 8 + 7 * 3)
9 * 3 * 6 + (2 * (3 + 8 * 7 * 4 + 6) + 5 + (4 * 7) + 2 * (3 * 9 * 8)) * 7
((6 + 3 + 8 * 6 * 8) * (8 * 6 + 4 + 9 + 4) * (4 + 9 + 2 * 2 + 3) + 7 + (3 + 9 + 3 + 7 + 9 * 6) * 4) + 8
5 * (3 * 4 * 4 + (5 + 7 * 3)) * 3 * 5 * 7
((5 * 5 * 7 + 7 + 4 * 9) + 3) + 4 + 5
(7 * 4 + 6) * 2
6 * 2 * 5 * (8 + 6 + 3 * 8 * 5) * (4 * 3 * 5 + 4 + 5 + 9) * ((4 * 6 + 3 + 9) + 5 + 4 + 2 + 6 + 2)
4 + (5 + 4 + 7 + (8 * 8 + 7 + 6) * 3 * 4) * (2 + 3 + 4 + 9) + 3 + 8
5 * 5 + (7 * 9) + 5
(2 + 3 + 3 + 5 * 6 * 2) * 7 + 8 * (2 + 5 * 8 + 2 + 3 + 5)
2 + 5 * (5 * 7 * 5 * 3) + 2 * (7 + 4 * (5 * 9 * 5) + 6)
5 * 7 + 7 * 4
2 + 8 + 3 + (3 * 8 * 9) + 5
3 + ((2 * 8 + 3) + 3) * 9 * 6 * 6
((7 + 6 * 3 + 6 + 7) * 4 * (9 + 6) + 6 + (5 + 8 + 4 * 7 + 9) * 7) + 9
6 + ((2 * 7 * 6 + 2) * 9) * (8 * 5 * 2 + (2 + 6)) * 4 * 6
(5 * 6 * 4 * 2 * 7) * 2 + 2 + (5 * 8 * (9 + 8 + 7 * 3 + 2 + 6) + 5) + (2 + (9 * 4 + 3) * 9 * 2 * 4 + 8) * 6
((7 * 8 + 2) * 8 * 6 * 5) + 4 + ((8 + 3 * 9 + 7) + 8 * 5) + (2 + 5 + 8) * 4
3 * (4 + (7 + 2 * 4) * 8 * 6)
9 * ((6 + 8 + 2 * 3) * 2 + 7 + 4 + 9 + 5) + 6 + 9
6 + 7 + (7 * 7) + (8 * 9 + (9 + 9) + (6 * 5 * 9 + 9 * 4)) * 3
(5 + (3 * 5) + 5) + (3 + 5 * (4 + 7 + 7 * 8) * 8 * 2) * 7
5 * 7 + ((9 + 3 * 8) + 3 * 3)
2 * (8 + 8) * (4 * 9 * 9 * (6 + 8 + 3)) * 7 * 7 + 8
9 + ((6 * 4 * 9 + 3 + 7) * 5 * 9 + 9 * (2 * 8 + 3 + 7 * 9 + 4)) + 8 + 6 * 8 * 9
(8 + 3 + 9 + 7 * 6) * 6 * 2 + 7
7 * (5 * 4 * 8 + (9 * 7) * 7) * 8 + 3
(5 + 5 + (3 * 9) * 3 * (6 + 2 * 5 * 4 * 5) * (8 * 7 * 9 + 9)) + 9 + ((6 * 2 + 9 + 5 + 6) + 4) * 3 * 8
4 + 4 + 7 + 2 + (4 * 5 + 2)
5 + 8 * (5 * (6 * 5 * 7))
((8 * 5 + 8 + 4 * 9 + 4) * 5 * 2 * 5) + 6 + 5
4 + ((2 + 6 * 3 + 5) + 9 * 3 * 6 + 4 * 7) * (7 * 6 * 4)
5 * (4 + 2 * 8 * 3 + 8 * 8)
5 + 2 + (2 * (2 + 4) * (3 * 3 * 7 * 6 + 5 * 7) * 8 + 4) * (8 * 9 * (5 + 3 + 8 + 4 * 9 * 7))
8 + ((5 + 4 + 9 + 3 + 8) + 9 * (3 * 2) + (6 + 5)) + ((8 + 7 * 2 * 4) * 5 + 4 + 5 + 2 * (2 * 3))
(8 + (7 + 6 + 9 + 2 * 6 + 4) * 2 + 5) * (3 + 6 * 9 + 6 + (8 + 9 + 4 * 4 + 2 * 7) * 6) + 4
8 + ((5 * 4) + 7) * 2 * 3 * 7
(3 + 4 + 2 + 8 + 2 + 4) + (2 + 6 + (7 * 8 * 4) + 3) + 3 + 2 * 9 + 5
6 * 8 * (8 * 9 + 5 + 8)
((8 + 2 + 5 * 8 * 9 + 4) * 8 + 9 * (9 + 2 * 6)) + 3 * 3 + 9 * (5 * 4)
((2 * 9) + 7 + 7 * (7 + 8 * 4 + 2)) * 6 + 6 + (4 * 2 * 7)
7 + ((2 + 8 + 7 + 4) * (4 + 2 + 9 + 2 * 9) + 2 + (6 * 8 + 5 * 2 * 3) + 5) + 7 * (6 + 8) * 5 + 2
8 * 5 + 3 + 7 * 7
(6 * 3 + 2 * 5 + 6) + 5 * (4 + 9 * 2 * 8 * (7 * 7)) * 7 + 9
2 * 7 * ((5 + 7 * 5) * 6 + 3 * (2 * 3 + 8) + 5 * (9 + 7 + 5 * 3 * 6)) + (7 * (8 * 5 + 7 * 4) * 9)
((6 * 9 + 8 * 8 + 2 * 8) + 8 + 5 + 4 * 7 * 4) + 7
5 * 6 * (3 * 3 * 6) * 6 * 7 * 9
2 + 3 + ((6 + 5) * 7 + (2 * 4) + 7) + 6
(7 + 8 + (2 + 4 * 9 * 8 * 5)) + (3 + 8 * 7)
9 + ((3 + 4 * 8 + 3 * 4) + 2 + 9 + (8 * 7 + 3 * 4 * 7 * 8) + 3) * 2 + 4 * 6
4 + ((2 + 9 + 4) * 3 + (7 + 3 + 2) * 5 * 3 + 2)
2 * 4 + 8 + 2 + 5 * (4 + 6)
(9 + 8 + 9 + 7) * 8 + 4 * 8 * (9 + 9 * 6) * 8
3 + 5 + (6 * 8 * 2 + (6 * 9) * 6 * 8)
3 + 4 * 2
6 * (3 * 2 + 3 + (6 + 3 + 7 * 4 + 2 * 7)) + 6 * 9 + 9 * 7
8 + 6 + 4 + 4 + (6 * 3 + 9) + 7
(4 + (3 * 5 * 7 * 7 + 4) * 5) * 2 * 6
8 + 4 + (5 * 5) + (6 + 8 * (7 + 3 + 7 * 7) + (6 + 4 + 9 * 8) * (2 + 6 + 7 + 4 * 3 * 7)) * (8 * 7 + 9)
((4 * 6 * 3 + 5 * 6 + 9) + 4 * 7 + 2 + 5) + (3 * 6 + 4) + (7 + 8 + 8)"""

tests = [
    "2 * 3 + (4 * 5)",
    "5 + (8 * 3 + 9 + 3 * 4 * 3)",
    "5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))",
    "((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2"
]

# normalize and tokenize input
def split_input(text):
    tokens = text.replace('(', ' ( ').replace(')', ' ) ').split(' ') # input
    tokens = list(filter(lambda t: t != '', tokens))
    return tokens

import re

from collections.abc import Iterable

def flatten(l):
    for el in l:
        if isinstance(el, Iterable) and not isinstance(el, (str, bytes)):
            yield from flatten(el)
        else:
            yield el


def parse_line(toks, depth=0):
    out = []
    i = 0
    while i < len(toks):
        c = toks[i]
        #print(f'i={i} => toki={toks[i]} d={depth}')
        #print(f'    {len(toks)} {toks}')
        if c == '(':
            sub = toks[i + 1:]
            (subArray, processedTokens) = parse_line(sub, depth + 1)
            #print(f'processedTokens={processedTokens}')
            out.append(subArray)
            i += processedTokens + 1
        elif c == ')':
            #print(f'break d={depth}')
            break
        elif c in ['*', '+']:
            out.append(c)
        elif re.search('^\d+$', c):
            out.append(int(c))
        else:
            print(f'parsing error: {c} not recognized')

        #print(f'i={i} out={out}')
        i += 1
    
    return (out, i)

def resolve_term(toks):
    total = 0
    operator = None
    for i, tok in enumerate(toks):
        if type(tok).__name__ == 'int':
            if operator:
                if operator == '*':
                    total *= tok
                elif operator == '+':
                    total += tok
            else:
                total = tok
        
        elif type(tok).__name__ == 'str':
            operator = tok

        elif type(tok).__name__ == 'list':
            if operator:
                if operator == '*':
                    total *= resolve_term(tok)
                elif operator == '+':
                    total += resolve_term(tok)
            else:
                total = resolve_term(tok)
    
    return total

"""for test in tests:
    (parsedTerm, _) = parse_line(split_input(test))
    print(f'result: {parsedTerm}')
    resolvedTerm = resolve_term(parsedTerm)
    print(resolvedTerm)"""

total = 0
for term in input.splitlines():
    (parsedTerm, _) = parse_line(split_input(term))
    #print(f'result: {parsedTerm}')
    resolvedTerm = resolve_term(parsedTerm)
    #print(resolvedTerm)
    total += resolvedTerm

print(f'total = {total}')
