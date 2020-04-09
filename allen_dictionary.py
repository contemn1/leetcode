class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        def smaller_than(first, second, order_map):
            for i in range(5):
                if order_map[first[i]] > order_map[second[i]]:
                    return False
            return len(first) < len(second)

        if not words or not order:
            return False
        
        if len(words) == 1:
            return True
        
            
        order_map = {char: i for i, char in enumerate(order)}
        
        for index in range(0, len(words) - 1):
            if not less_than(words[index], words[index + 1], order_map):
                return False
        
        return True
    
