from typing import List

def wordBreak(s: str, wordDict: List[str]) -> List[str]:
    def dfs(edge_map, index, res_string):
        if index == 0:
            yield res_string
        else:
            for children in edge_map[index]:
                yield from dfs(edge_map, children, s[children: index] + " " + res_string)
    
    if not wordDict:
        return False
    min_length = len(min(wordDict, key=len))
    length_map = {}
    prev_map = {}
    if len(s) < min_length:
        return False
    
    for ele in wordDict:
        if len(ele) in length_map:
            length_map[len(ele)].add(ele)
        else:
            length_map[len(ele)] = {ele}
    
    dp = [False for _ in range(len(s) + 1)]
    dp[0] = True
    for index in range(min_length, len(dp)):
        for length, word_map in length_map.items():
            if index - length < 0:
                continue
            if dp[index - length] and s[index - length: index] in length_map[length]:
                dp[index] = True
                if index in prev_map:
                    prev_map[index].append(index - length)
                else:
                    prev_map[index] = [index - length]
    return list(dfs(prev_map, len(s), ""))

if __name__ == "__main__":
    input_string = "pineapplepenapple"
    wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
    res = wordBreak(input_string, wordDict)
    print(res)