num_word=0
with open ("textfile.txt",'r') as f:
    for i in f:
        word=i.split()
        num_word+=len(word)
print("number of words ={}".format(num_word))
