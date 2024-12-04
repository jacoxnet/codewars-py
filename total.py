#total area covered by rectangles 3kyu
def calculate(rectangles):
    points = set()
    bottom_left_x = 0
    bottom_left_y = 1
    top_right_x = 2
    top_right_y = 3
    for rect in rectangles:
        for x in range(rect[bottom_left_x], rect[top_right_x]):
            for y in range(rect[bottom_left_y], rect[top_right_y]):
                points.add((x,y))
    return len(points)
    


import codewars_test as test

TESTS = (
    ("basic cases", (
        ("0 rectangles",                          0,    []),
        ("1 rectangle",                           1,    [(0,0,1,1)]),
        ("1 rectangle (version 2)",               22,   [(0, 4, 11, 6)]),
        ("2 rectangles",                          2,    [(0,0,1,1), (1,1,2,2)]),
        ("2 rectangle (version 2)",               4,    [(0,0,1,1), (0,0,2,2)]),
        ("3 rectangle ",                          36,   [(3,3,8,5), (6,3,8,9),(11,6,14,12)]),
    )),
    ("More fixed cases", (
        ("1 under 2",                             6,    [ ( 1, 7, 3, 10 ),  ( 1, 8, 3, 9 )]),
        ("nested",                                9,    [ ( 6, 7, 9, 10 ),  ( 7, 8, 8, 9 )]),
        ("nested 2",                              9,    [ ( 1, 7, 4, 10 ),  ( 2, 7, 4, 9 ),  ( 3, 7, 4, 9 )]),
        ("intersection up",                       7,    [ ( 1, 1, 4, 3 ),  ( 2, 2, 3, 4 )]),
        ("intersetion right",                     7,    [ ( 5, 0, 7, 3 ),  ( 6, 1, 8, 2 )]),
        ("intersection up right",                 7,    [ ( 9, 0, 11, 2 ),  ( 10, 1, 12, 3 )]),
        ("intersection down",                     7,    [ ( 13, 1, 16, 3 ),  ( 14, 0, 15, 2 )]),
        ("intersection down right",               7,    [ ( 17, 1, 19, 3 ),  ( 18, 0, 20, 2 )]),
        ("intersection of the entire right side", 7,    [ ( 13, 5, 15, 6 ),  ( 14, 4, 16, 7 )]),
        ("intersection 3 rect",                   20,   [ ( 1, 3, 4, 6 ),  ( 2, 1, 5, 4 ),  ( 3, 2, 6, 5 )]),
        ("3*3",                                   9,    [(1,1,2,2),(2,1,3,2),(3,1,4,2),(1,2,2,3),(2,2,3,3),(3,2,4,3),(1,3,2,4),(2,3,3,4),(3,3,4,4)]),
        ("intersection",                          25,   [( 1, 1, 6, 6 ),( 1, 3, 4, 6 ),( 2, 3, 4, 6 ),( 2, 4, 5, 6 ),( 3, 5, 4, 6 )]),
        ("shift right",                           25,   [(1,1,6,6),(2,1,6,6),(3,1,6,6),(4,1,6,6),(5,2,6,5)]),
        ("shift right down",                      70,   [(1,1,7,6),(2,2,8,7),(3,3,9,8),(4,4,10,9),(5,5,11,10)]),
        ("wings",                                 38,   [ ( 1, 4, 5, 6 ),  ( 2, 5, 6, 7 ),( 3, 6, 7, 8 ),( 4, 7, 8, 9 ),( 2, 3, 6, 5 ),( 3, 2, 7, 4 ),( 4, 1, 8, 3 )]),
        ("intersection cross",                    5,    [ ( 9, 5, 12, 6 ),  ( 10, 4, 11, 7 )]),
        ("intersection 2",                        53,   [ ( 7, 1, 11, 7 ),  ( 8, 0, 12, 3 ),  ( 8, 4, 13, 5 ),  ( 9, 5, 14, 8 ),( 10, 2, 15, 6 )]),
        ("pyramid",                               36,   [(1,2,6,6),(1,3,5,5),(1,1,7,7)]),
        ("circle",                                37,   [(1,2,3,7),(2,1,7,3),(6,2,8,7),(2,6,7,8),(4,4,5,5)]),
        ("one",                                   1,    [(1,1,2,2),(1,1,2,2),(1,1,2,2),(1,1,2,2),(1,1,2,2),(1,1,2,2)]),
        ("very hard!",                            52,   [(3,3,6,5),(4,4,6,6),(4,3,7,5),(4,2,8,5),(4,3,8,6),(9,0,11,4),(9,1,10,6),(9,0,12,2),(10,1,13,5),(12,4,15,6),(14,1,16,5),(12,1,17,2)]),
        ("waterfall",                             390,  [(2, 2, 17, 2), (2, 2, 17, 4), (2, 2, 17, 6), (2, 2, 17, 8), (2, 2, 17, 10), (2, 2, 17, 12), (2, 2, 17, 14), (2, 2, 17, 16), (2, 2, 17, 18), (2, 2, 17, 20), (2, 2, 17, 22), (2, 2, 17, 24), (2, 2, 17, 26), (2, 2, 17, 28)]),
        ('overlap E',                             10,   [(0,0,3,1), (0,0,10,1)]),
        ('overlap W',                             10,   [(3,0,10,1), (0,0,10,1)]),
        ('overlap N',                             30,   [(0,0,3,1), (0,0,3,10)]),
        ('overlap S',                             30,   [(0,0,3,10), (0,3,3,10)]),
    ))
)


for title,its in TESTS:
    @test.describe(title)
    def _():
        for sub_title,exp,rects in its:
            @test.it(sub_title)
            def _():
                test.assert_equals(calculate(rects), exp)
