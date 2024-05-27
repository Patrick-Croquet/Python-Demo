def Trouve(a, b):
    i = 0
    while i <= len(a) - len(b) and b != a[i:i+len(b)]:
        i += 1
    # print(b, a[i:i+len(b)])    
    if b != a[i:i+len(b)]:
        return 0
    else:
        # print(a[i:i+len(b)])
        return i

def PurgeMultiple(a, b):
    Sortie = ''
    for i in range(0, len(a)):
        if Trouve(b, a[i]) == 0:
            Sortie += a[i]
    return Sortie

voyelles = " aeiouy"
print(PurgeMultiple("J'ai horreur des voyelles", voyelles))