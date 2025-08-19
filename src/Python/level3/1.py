def isacronymn(acro, sentence):
    words = sentence.split()
    formed = ''.join(word[0].upper() for word in words)
    print(formed)
    return formed == acro.upper()

a = "NASA"
b = "National Aeronautics Space Administration"
c = isacronymn(a,b)
print(c)