def reverse_integer(n):
    # your implementation goes here
    rev_n = 0
    while n > 0:
        rev_n = rev_n * 10 + n%10
        n //= 10
    return rev_n

print(reverse_integer(1234))