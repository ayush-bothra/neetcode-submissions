class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mapper = defaultdict(list)
        for s in strs:
            mapper["".join(sorted(s))].append(s)
        result = [item for item in mapper.values()]
        return result
        
