from zakariyya_scavotto_puzzle import Puzzle

# top, bottom, left, right, back, front
testPuzzle = Puzzle([['B', 'B', 'B'], ['B', 'B', 'B'], ['B', 'B', 'B']],
                    [['G', 'G', 'G'], ['G', 'G', 'G'], ['G', 'G', 'G']],
                    [['O', 'O', 'O'], ['O', 'O', 'O'], ['O', 'O', 'O']],
                    [['R', 'R', 'R'], ['R', 'R', 'R'], ['R', 'R', 'R']],
                    [['W', 'W', 'W'], ['W', 'W', 'W'], ['W', 'W', 'W']],
                    [['Y', 'Y', 'Y'], ['Y', 'Y', 'Y'], ['Y', 'Y', 'Y']])

# print("ORIGINAL CUBE")
# print(testPuzzle)
# Row tests
'''
print("ROTATE TOP ROW RIGHT")
testPuzzle.rotate_row_right(0)
print(testPuzzle)
print("ROTATE MIDDLE ROW RIGHT")
testPuzzle.rotate_row_right(1)
print(testPuzzle)
print("ROTATE BOTTOM ROW RIGHT")
testPuzzle.rotate_row_right(2)
print(testPuzzle)
print("ROTATE TOP ROW LEFT")
testPuzzle.rotate_row_left(0)
print(testPuzzle)
print("ROTATE MIDDLE ROW LEFT")
testPuzzle.rotate_row_left(1)
print(testPuzzle)
print("ROTATE BOTTOM ROW LEFT")
testPuzzle.rotate_row_left(2)
print(testPuzzle)
'''
# Col tests
'''
print("ROTATE LEFT COL UP")
testPuzzle.rotate_col_up(0)
print(testPuzzle)
print("ROTATE MIDDLE COL UP")
testPuzzle.rotate_col_up(1)
print(testPuzzle)
print("ROTATE RIGHT COL UP")
testPuzzle.rotate_col_up(2)
print(testPuzzle)
print("ROTATE LEFT COL DOWN")
testPuzzle.rotate_col_down(0)
print(testPuzzle)
print("ROTATE MIDDLE COL DOWN")
testPuzzle.rotate_col_down(1)
print(testPuzzle)
print("ROTATE RIGHT COL DOWN")
testPuzzle.rotate_col_down(2)
print(testPuzzle)
'''
# Face tests
'''
print("ROTATE CUBE RIGHT")
testPuzzle.rotate_cube_right()
print(testPuzzle)
print("ROTATE CUBE LEFT")
testPuzzle.rotate_cube_left()
print(testPuzzle)
print("ROTATE CUBE UP")
testPuzzle.rotate_cube_up()
print(testPuzzle)
print("ROTATE CUBE DOWN")
testPuzzle.rotate_cube_down()
print(testPuzzle)
'''
testPuzzle.solve_cube()
