import re

def is_anagram(s1,s2):
    s11 = re.sub(r'[^a-z]', '',s1.lower())
    s21 = re.sub(r'[^a-z]', '',s2.lower())
    return sorted(s11) == sorted(s21)

s1 = "listen"
s2 = "silent"

a = is_anagram(s1,s2)
print(a)
