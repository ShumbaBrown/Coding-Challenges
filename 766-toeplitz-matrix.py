# A matrix is Toeplitz if every diagonal from top-left to bottom-right has the same element.
#
# Now given an M x N matrix, return True if and only if the matrix is Toeplitz.



class Solution(object):
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        starts = self.getStarts(matrix)

        for each in starts:
            if self.sameDiag(each, matrix) == False:
                return False
        return True


    def getStarts(self, matrix):
        starts = list()
        for i in range(len(matrix)):
            starts.append((0,i))
        for i in range(len(matrix[0])):
            starts.append((i,0))
        return starts

    def sameDiag(self, start, matrix):
        y = start[1]
        x = start[0]
        val = matrix[y][x]

        while y < len(matrix) and x < len(matrix[0]):
            if matrix[y][x] != val:
                return False
            x += 1
            y += 1
        return True



    
