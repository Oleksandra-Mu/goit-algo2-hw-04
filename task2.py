from trie import Trie


class LongestCommonWord(Trie):

    def find_longest_common_word(self, strings) -> str:
        if not strings or any(s == "" for s in strings):
            return ""

        for word in strings:
            self.put(word, None)

        longest_common_prefix = ""
        current = self.root

        while current and len(current.children) == 1:
            for char, child in current.children.items():
                longest_common_prefix += char
                current = child
        return longest_common_prefix


if __name__ == "__main__":
    # Тести
    trie = LongestCommonWord()
    strings = ["flower", "flow", "flight"]
    assert trie.find_longest_common_word(strings) == "fl"

    trie = LongestCommonWord()
    strings = ["interspecies", "interstellar", "interstate"]
    assert trie.find_longest_common_word(strings) == "inters"

    trie = LongestCommonWord()
    strings = ["dog", "racecar", "car"]
    assert trie.find_longest_common_word(strings) == ""
