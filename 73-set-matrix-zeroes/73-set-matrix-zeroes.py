class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        to_be_zeroed = {line: [] for line in range(len(matrix))}
        for ind_line1, line1 in enumerate(matrix):
            for ind_num, num in enumerate(line1):
                
                if num == 0:
                    to_be_zeroed[ind_line1] = 'all'
                    for ind_line2, line2 in enumerate(matrix):
                        if to_be_zeroed[ind_line2] != 'all':
                            to_be_zeroed[ind_line2].append(ind_num)
                               
        for to_be_zeroed_line in to_be_zeroed:
            if to_be_zeroed[to_be_zeroed_line] == 'all':
                matrix[to_be_zeroed_line] = [0 for i in matrix[to_be_zeroed_line]]
            else:
                for ind_num in to_be_zeroed[to_be_zeroed_line]:
                    matrix[to_be_zeroed_line][ind_num] = 0
