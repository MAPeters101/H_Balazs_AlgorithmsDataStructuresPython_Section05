def is_anagram(str1, str2):

    # your algorithm goes here
    # return True if str1 and str2 are anagrams, otherwise return False
    lst1 = sorted(list(str1))
    lst2 = sorted(list(str2))
    #print(lst1)
    #print(lst2)
    return lst1 == lst2

print(is_anagram("restful", "fluster"))
