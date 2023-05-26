def is_palindrome_iterative(word):
    if not word:
        return False
    rev = ''.join(reversed(word))
    if word != rev:
        return False
    return True
        

