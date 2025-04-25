# you can define helper methods if needed
# def is_palindrome(s):
#     # your implementation of the algorithm goes here
#     start_index, end_index = 0, len(s)-1
#     while start_index < end_index:
#         if s[start_index] != s[end_index]:
#             return False
#         start_index += 1
#         end_index -= 1
#     return True

def reverse(data):
    # your algorithm here - nums is the list containing the items
    low_index, high_index = 0, len(data)-1
    data = list(data)
    while low_index < high_index:
        data[high_index], data[low_index] = data[low_index], data[high_index]
        low_index += 1
        high_index -= 1
    return ''.join(data)

def is_palindrome(s):
    # your implementation of the algorithm goes here
    reversed_string = reverse(s)
    return reversed_string == s


print(is_palindrome('kevin'))
print(is_palindrome('madam'))