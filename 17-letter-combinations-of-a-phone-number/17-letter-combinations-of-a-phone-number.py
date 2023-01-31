class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        telephone = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }
        
        possible = []
        if len(digits) == 1:
            for i in telephone[digits[0]]:
                possible.append(i)
        if len(digits) == 2:
            for i in telephone[digits[0]]:
                for j in telephone[digits[1]]:
                    possible.append(f'{i}{j}')
        if len(digits) == 3:
            for i in telephone[digits[0]]:
                for j in telephone[digits[1]]:
                    for z in telephone[digits[2]]:
                        possible.append(f'{i}{j}{z}')
        if len(digits) == 4:
            for i in telephone[digits[0]]:
                for j in telephone[digits[1]]:
                    for z in telephone[digits[2]]:
                        for x in telephone[digits[3]]:
                            possible.append(f'{i}{j}{z}{x}')
        
        return possible