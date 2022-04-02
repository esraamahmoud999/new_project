def matching(new_first):
    new_first =second.replace(first,second)         
    for i in first:
        if i not in second and len(first)!=len(second):
            new_first += i
            new_first=second.replace(first,second)
            return (new_first, True)
        elif i in second and len(first)==len(second):
            return (new_first, True)
        else:
            print(False) 


def isPalindrome(s):
    return s == s[::-1]




def find_nth_occurrence(substring, str, occurrence=1):
    r = substring.split(str, occurrence)
    if len(r) <= occurrence:
        return -1
    return len(substring) - len(r[-1]) - len(str)


