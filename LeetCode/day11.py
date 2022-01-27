# **********************************************
# 151. Reverse Words in a String
# space is ''
# **********************************************

def reverseWords(s):
    s = s[::-1]
    s1 = s.split(' ')
    s2 = []
    for i in range(len(s1)):
        if s1[i] == '':
            continue
        s1[i] = s1[i][::-1]
        s2.append(s1[i])
    return ' '.join(s2)
s = '  he   wod'
print(reverseWords(s))