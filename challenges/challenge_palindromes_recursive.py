def is_palindrome_recursive(word, low_index, high_index):
    word = word.upper()
    if len(word) == 0:
        return False
    if len(word) == 1:
        return word[high_index] == word[low_index]
    if low_index >= high_index:
        return True
    return word[low_index] == word[high_index] and is_palindrome_recursive(
        word, low_index + 1, high_index - 1
        )
