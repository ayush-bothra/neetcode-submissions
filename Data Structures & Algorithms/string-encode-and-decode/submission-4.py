class Solution:

    def encode(self, strs: List[str]) -> str:
        cipher = ""
        for s in strs:
            cipher += str(len(s))
            cipher += "#"
            cipher += s
        return cipher

    def decode(self, s: str) -> List[str]:
        decipher = []
        i, j = 0,0
        n = len(s)
        while i < n and j < n:
            j = s.find('#', i)
            length = int(s[i:j])
            decipher.append(s[j+1:j+length+1])
            i = j + length + 1
        return decipher
