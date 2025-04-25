# you can define helper methods if needed
def is_palindrome(s):
    # your implementation of the algorithm goes here
    # print(s, s[::-1])
    return s == s[::-1]

print(is_palindrome('kevin'))
print(is_palindrome('madam'))