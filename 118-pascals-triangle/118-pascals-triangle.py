class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        rows = []
        for row in range(numRows):
            
            if not rows:
                rows.append([1])
                continue
            
            if len(rows) == 1:
                rows.append([1,1])
                continue
            
            prev_row = rows[-1]
            new_row = []
            for num_ind, num in enumerate(prev_row[:-1]):
                new_row.append(num + prev_row[num_ind+1])
                
            new_row.insert(0, 1)
            new_row.append(1)
            rows.append(new_row)
                
        return rows
                