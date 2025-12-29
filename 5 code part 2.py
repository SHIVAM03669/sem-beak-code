class Solution:
    def groupAnagrams(self, strs):
        mp = {}

        for x in strs:
            word = ''.join(sorted(x))
            if word not in mp:
                mp[word] = []
            mp[word].append(x)

        ans = []
        for key in mp:
            ans.append(mp[key])

        return ans
