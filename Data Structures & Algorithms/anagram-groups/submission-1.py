class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mapper = defaultdict(list)
        for s in strs:
            key = [0] * 26
            for c in s:
                key[ord(c) - 97] += 1
            mapper[tuple(key)].append(s)
        result = [item for item in mapper.values()]
        return result

