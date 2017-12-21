"""
Implement a method to perform basic string compression using the counts of repeated characters.
For example, the string aabcccccaaa would become a2b1c5a3. If the "compressed" string would not
become smaller than the original string, your method should return the original string. You can
assume the string has only uppercase and lowercase letters (a - z).
"""

def stringCompression(s):


    sc = s[0]
    count = 1
    for i in range( len(s) -1 ):
        if s[i] == s[i + 1]:
            count += 1
        else:
            sc += str(count) + s[i + 1] # To improve performance we can append in a list and 
            count = 1                   # use ''.join(list) for concatenate the list into the sc
    sc += str(count)

    if len(s) > len(sc):
        return sc

    return s