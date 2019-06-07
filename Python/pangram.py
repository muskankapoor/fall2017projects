def pangram(str):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for i in alphabet:
        if i not in str:
            return False

    return True

print (pangram("The quick brown fox jumps over the lazy dog"))