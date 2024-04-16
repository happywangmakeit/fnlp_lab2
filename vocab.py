VOCAB={}
for i in range(26):
    VOCAB[(' ',ord("a")+i)]=0
    VOCAB[(ord('a')+i,' ')]=0
    VOCAB[(' ',ord('A')+i)]=0
    VOCAB[(ord('A')+i,' ')]=0
    for j in range(26):
        VOCAB[(ord('a')+i,ord('a')+j)]=0
        VOCAB[(ord('A')+i,ord('A')+j)]=0

print(VOCAB)