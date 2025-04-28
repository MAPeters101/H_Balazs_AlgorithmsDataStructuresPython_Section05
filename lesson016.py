def is_anagram(str1, str2):

    # your algorithm goes here
    # return True if str1 and str2 are anagrams, otherwise return False
    if len(str1) != len(str2):
        return False

    str1 = sorted(str1)
    str2 = sorted(str2)

    for i in range(len(str1)):
        if str1[i] != str2[i]:
            return False
    return True

print(is_anagram("restful", "fluster"))
