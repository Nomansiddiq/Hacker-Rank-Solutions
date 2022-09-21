Problem Statment
Implement a function that takes a string that consists of
lowercase letters and digits and returns a string that 
consists of all digits and lowercase English letters that are not present in the string. 
The digits should come first, in ascending order, followed by characters, also in ascending order.



def missingCharacters(s):
    l=[0]*123
    result=""
    for i in range(len(s)):
        x=ord(s[i])
        l[x]+=1
    for i in range(48,58):
        if(l[i]==0):
            result+=chr(i)
    for i in range(97,123):
        if(l[i]==0):
            result+=chr(i)
    return result
