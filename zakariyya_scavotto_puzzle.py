class Puzzle:

    def __init__(self, top, bottom, left, right, back, front):

        self.top = top
        self.bottom = bottom
        self.left = left
        self.right = right
        self.back = back
        self.front = front

    def getFaceString(self, face):
        # Method that gets the string for either the face (in case of back or front)
        # or for the whole row of faces (in the case of left, bottom, right, top)
        if face == self.back or face == self.front:
            toReturn = ""
            for i in range(len(face)):
                for j in range(len(face[i])):
                    toReturn += " " + face[i][j]
                if i != 2:
                    toReturn += "\n      "
                else:
                    toReturn += "\n"
            return toReturn
        else:
            # Get string for the "middle" faces (L, BOT, R, TOP)
            toReturn = ""
            # top row
            for subface in face:
                for j in range(len(subface[0])):
                    if j == 0 and subface != self.left:
                        # divider bar between faces
                        toReturn += "|" + subface[0][j]
                    else:
                        toReturn += " " + subface[0][j]
            toReturn += "\n"
            # middle row
            for subface in face:
                for j in range(len(subface[1])):
                    if j == 0 and subface != self.left:
                        # divider bar between faces
                        toReturn += "|" + subface[1][j]
                    else:
                        toReturn += " " + subface[1][j]
            toReturn += "\n"
            # bottom row
            for subface in face:
                for j in range(len(subface[2])):
                    if j == 0 and subface != self.left:
                        # divider bar between faces
                        toReturn += "|" + subface[2][j]
                    else:
                        toReturn += " " + subface[2][j]
            toReturn += "\n"
            return toReturn

    def __str__(self):
        # Simple toString method for printing the cube nicely
        toReturn = ""
        toReturn += "      " + self.getFaceString(self.back)
        toReturn += self.getFaceString([self.left,
                                       self.bottom, self.right, self.top])
        toReturn += "      " + self.getFaceString(self.front)
        return toReturn

    def rotate_face_90_CW(self, face):
        # Helper method to rotate face 90 degrees clockwise
        faceData = []
        '''For which ever face is given, make a copy of its data, 
        then iteratively put it in the right place'''
        if face == 'right':
            faceData = [item[:] for item in self.right]
            for row in range(len(faceData)):
                for col in range(len(faceData[row])):
                    self.right[col][2-row] = faceData[row][col]
        elif face == 'left':
            faceData = [item[:] for item in self.left]
            for row in range(len(faceData)):
                for col in range(len(faceData[row])):
                    self.left[col][2-row] = faceData[row][col]
        elif face == 'top':
            faceData = [item[:] for item in self.top]
            for row in range(len(faceData)):
                for col in range(len(faceData[row])):
                    self.top[col][2-row] = faceData[row][col]
        elif face == 'bottom':
            faceData = [item[:] for item in self.bottom]
            for row in range(len(faceData)):
                for col in range(len(faceData[row])):
                    self.bottom[col][2-row] = faceData[row][col]
        elif face == 'front':
            faceData = [item[:] for item in self.front]
            for row in range(len(faceData)):
                for col in range(len(faceData[row])):
                    self.front[col][2-row] = faceData[row][col]
        elif face == 'back':
            faceData = [item[:] for item in self.back]
            for row in range(len(faceData)):
                for col in range(len(faceData[row])):
                    self.back[col][2-row] = faceData[row][col]

    def rotate_face_90_CCW(self, face):
        # Helper method to rotate face 90 degrees counter-clockwise
        faceData = []
        '''For which ever face is given, make a copy of its data, 
        then iteratively put it in the right place'''
        if face == 'right':
            faceData = [item[:] for item in self.right]
            for row in range(len(faceData)):
                for col in range(len(faceData[row])):
                    self.right[2-col][row] = faceData[row][col]
        elif face == 'left':
            faceData = [item[:] for item in self.left]
            for row in range(len(faceData)):
                for col in range(len(faceData[row])):
                    self.left[2-col][row] = faceData[row][col]
        elif face == 'top':
            faceData = [item[:] for item in self.top]
            for row in range(len(faceData)):
                for col in range(len(faceData[row])):
                    self.top[2-col][row] = faceData[row][col]
        elif face == 'bottom':
            faceData = [item[:] for item in self.bottom]
            for row in range(len(faceData)):
                for col in range(len(faceData[row])):
                    self.bottom[2-col][row] = faceData[row][col]
        elif face == 'front':
            faceData = [item[:] for item in self.front]
            for row in range(len(faceData)):
                for col in range(len(faceData[row])):
                    self.front[2-col][row] = faceData[row][col]
        elif face == 'back':
            faceData = [item[:] for item in self.back]
            for row in range(len(faceData)):
                for col in range(len(faceData[row])):
                    self.back[2-col][row] = faceData[row][col]

    def rotate_row_right(self, row_num):
        # row_num denotes which row is being rotated right
        # write your implementation below
        '''Front becomes right, Right becomes back, Back becomes left, Left becomes front
                Top/bottom (depends on row_num) face rotates 90 degrees counter-clockwise'''
        # Save the row data
        frontRow = self.front[row_num]
        rightRow = self.right[row_num]
        backRow = self.back[row_num]
        leftRow = self.left[row_num]

        # Rotate rows
        self.right[row_num] = frontRow
        self.back[row_num] = rightRow
        self.left[row_num] = backRow
        self.front[row_num] = leftRow

        # Check if top or bottom face needs rotating, if so rotate
        if (row_num == 0):
            self.rotate_face_90_CCW("top")
        elif (row_num == 2):
            self.rotate_face_90_CCW("bottom")

    def rotate_row_left(self, row_num):
        # row_num denotes which row is being rotated left
        # write your implementation below
        '''Front becomes left, Left becomes back, Back becomes right, Right becomes front
                Top/bottom (depends on row_num) face rotates 90 degrees clockwise'''
        # Save the row data
        frontRow = self.front[row_num]
        rightRow = self.right[row_num]
        backRow = self.back[row_num]
        leftRow = self.left[row_num]

        # Rotate rows
        self.left[row_num] = frontRow
        self.back[row_num] = leftRow
        self.right[row_num] = backRow
        self.front[row_num] = rightRow

        # Check if top or bottom face needs rotating, if so rotate
        if (row_num == 0):
            self.rotate_face_90_CW("top")
        elif (row_num == 2):
            self.rotate_face_90_CW("bottom")

    def rotate_col_up(self, col_num):
        # col_num denotes which col is being rotated up
        # write your implementation below
        '''Front becomes top, Top becomes back, Back becomes bottom, Bottom becomes front
                Right/left (depends on col_num) face rotates 90 degrees clockwise'''
        # Save the column data
        frontCol = [row[col_num] for row in self.front]
        topCol = [row[col_num] for row in self.top]
        backCol = [row[col_num] for row in self.back]
        bottomCol = [row[col_num] for row in self.bottom]

        # Make the rotation
        # Front to top
        for i in range(len(self.top)):
            self.top[i][col_num] = frontCol[i]

        # Top to back
        for i in range(len(self.back)):
            self.back[i][col_num] = topCol[i]

        # Back to bottom
        for i in range(len(self.bottom)):
            self.bottom[i][col_num] = backCol[i]

        # Bottom to front
        for i in range(len(self.front)):
            self.front[i][col_num] = bottomCol[i]

        # Check if right or left face needs rotating, if so rotate
        if (col_num == 0):
            self.rotate_face_90_CW("left")
        elif (col_num == 2):
            self.rotate_face_90_CW("right")

    def rotate_col_down(self, col_num):
        # col_num denotes which col is being rotated down
        # write your implentation below
        '''Front becomes bottom, Bottom becomes back, Back becomes top, Top becomes front
                Right/left (depends on col_num) face rotates 90 degrees counter-clockwise'''
        # Save the column data
        frontCol = [row[col_num] for row in self.front]
        topCol = [row[col_num] for row in self.top]
        backCol = [row[col_num] for row in self.back]
        bottomCol = [row[col_num] for row in self.bottom]

        # Make the rotation
        # Front to bottom
        for i in range(len(self.top)):
            self.bottom[i][col_num] = frontCol[i]

        # Bottom to back
        for i in range(len(self.back)):
            self.back[i][col_num] = bottomCol[i]

        # Back to top
        for i in range(len(self.bottom)):
            self.top[i][col_num] = backCol[i]

        # Top to front
        for i in range(len(self.front)):
            self.front[i][col_num] = topCol[i]

        # Check if right or left face needs rotating, if so rotate
        if (col_num == 0):
            self.rotate_face_90_CCW("left")
        elif (col_num == 2):
            self.rotate_face_90_CCW("right")

    def rotate_cube_right(self):
        # write your implementation below
        '''Front face becomes right, Right becomes back, Back becomes left, Left becomes front
                Top and bottom faces rotate 90 degrees counter-clockwise'''
        # Save face data
        frontFace = self.front
        rightFace = self.right
        backFace = self.back
        leftFace = self.left

        # Reassign faces
        self.right = frontFace
        self.back = rightFace
        self.left = backFace
        self.front = leftFace

        # Rotate top and bottom 90 degrees CCW
        self.rotate_face_90_CCW("top")
        self.rotate_face_90_CCW("bottom")

    def rotate_cube_left(self):
        # write your implementation below
        '''Front face becomes left, Left becomes back, Back becomes right, Right becomes front
                Top and bottom faces rotate 90 degrees clockwise'''
        # Save face data
        frontFace = self.front
        rightFace = self.right
        backFace = self.back
        leftFace = self.left

        # Reassign faces
        self.left = frontFace
        self.back = leftFace
        self.right = backFace
        self.front = rightFace

        # Rotate top and bottom 90 degrees CW
        self.rotate_face_90_CW("top")
        self.rotate_face_90_CW("bottom")

    def rotate_cube_up(self):
        # write your implementation below
        '''Front face becomes top, Top becomes back, Back becomes bottom, Bottom becomes front
                Right and left faces rotate 90 degrees clockwise'''
        # Save face data
        frontFace = self.front
        bottomFace = self.bottom
        backFace = self.back
        topFace = self.top

        # Reassign faces
        self.top = frontFace
        self.back = topFace
        self.bottom = backFace
        self.front = bottomFace

        # Rotate top and bottom 90 degrees CW
        self.rotate_face_90_CW("right")
        self.rotate_face_90_CW("left")

    def rotate_cube_down(self):
        # write your implementation below
        '''Front face becomes bottom, Bottom becomes back, Back becomes top, Top becomes front
                Right and left faces rotate 90 degrees counter-clockwise'''
        # Save face data
        frontFace = self.front
        bottomFace = self.bottom
        backFace = self.back
        topFace = self.top

        # Reassign faces
        self.bottom = frontFace
        self.back = bottomFace
        self.top = backFace
        self.front = topFace

        # Rotate top and bottom 90 degrees CCW
        self.rotate_face_90_CCW("right")
        self.rotate_face_90_CCW("left")

    def solve_cube(self):
        # Article reference: https://www.cubelelo.com/blogs/cubing/how-to-solve-a-rubik-s-cube-blindfolded
        # I tried to find an algorithm that allows for blind solving, since it is unknown which colors are going to be in which positions when method is tested
        '''Algorithm
        Will need to make a mapping of the edge letter scheme to the different matrix cells for the faces (make a dictionary?)
        Buffer piece - piece that allows cube to move without the rest of cube changing
            - Sounds like it would be good to make sure past edges put in the right spot don't accidentally get moved

        Actual Ponchmann Method to Solve a Cube (corners + edges)
        1. Corners
        Corner buffer is top left corner (A) (self.back[0][2]?)
        Bring piece to switch to bottom right red face (P) (according to the image they use for cube orientation in the article) (self.right[2][0]?)
        TO SOLVE THE CORNER: use a Y Perm (Rubik's cube term for a different type of permutation) without the first F rotation
        - R U' R' U' R U R' F' R U R' U' R' F R F'
        Do this process for all corners
        2. EDGES!!!
        Edge buffer is B (self.back[1][0]?), bring piece to be switched to D (self.back[1][2]?)
        Rather than using Y Perm to solve, use a T Perm, setup moves for each position case on the internet (what does this mean?)
        - Method depends on cycles being even-numbered (cycle: permutation that moves pieces in a cycle)
        - If odd, will have to do a parity algorithm after solving the edges, an Rb perm
        - - How to determine the parity of a cube? Finding results online for 4x4 and higher cubes, but nothing on 3x3s
        - - Well that's because upon another google search 3x3 cubes don't have parity: 
        - - - https://www.cubelelo.com/blogs/cubing/why-do-you-get-parity-on-4x4-and-not-on-3x3#:~:text=You%20cannot%20get%20parity%20on,it%20is%20designed%20like%20that
        - T Perm: (U) R U2 R' U2 R' F R2 U' R' U' R U R' F' R U R' U R U2 R' (U’)

        How to use Ponchmann for cross on 6 sides
        Is it possible to skip the corner solving and jump right into the edge solving? If so, 
        1) Put the edge that needs to be solved that's in the D position into its spot using the T Perm
        2) Repeat step 1 until edge in the D position is a solved edge
        3) If there are still edges to be solved, reorient cube such that an unsolved edge is in the D position, repeat 1)-3) until all edges solved
        4) Once all edges are solved, if cycles are odd numbered use parity algorithm, otherwise the cube should be solved
        '''
        print('ORIGINAL CUBE:')
        print('================================================================\n')
        print(self)

        print('Due to the many midterms that I have this week, I was able to fully solve one problem, the machine learning problem.')
        print('For the Rubiks Cube problem, I was able to implement the row, column, and cube turning methods, and I intended to implement a variation of the Old Pochmann algorithm to solve the cube and I am confident that I could have done so without the conflict with midterms.')
        print('In the solve_cube method, I put in the comments some notes on the Old Pochmann algorithm and how I would modify and use it to solve the cube problem.')
