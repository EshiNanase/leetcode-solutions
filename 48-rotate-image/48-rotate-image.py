class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        
        from copy import deepcopy
        
        old_matrix = deepcopy(matrix)
        
        for line_index, line in enumerate(old_matrix):
            for index, value in enumerate(line):
                matrix[index][-line_index-1] = value
            print(matrix)