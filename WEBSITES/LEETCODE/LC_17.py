def letterCombinations(digits):
    """
    :type digits: str
    :rtype: List[str]
    """

    char_map = ["0", "1", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]

    # assert len(char_map) == 10
    if digits == "" or not digits:
        return []

    permutations = []
    for i in digits:
        character_set = char_map[int(i)]

print(letterCombinations("23"))