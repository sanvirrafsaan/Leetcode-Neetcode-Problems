class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #we take ascii value as key, and list of word as value. 
        count_dict = defaultdict(list)
        for word in strs:
            let_count = [0] * 26 #26 length ascii representation

            for letter in word:
                let_count[ord(letter) - ord("a")] += 1
            count_dict[tuple(let_co)].append(word)
        return list(count_dict.values())
