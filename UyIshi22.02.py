#   Barcha saralsh algorithmlarini o'rganib chiqib ham sonlarni, ham harflarni saralaydigan universal saralash algoritmini tuzing. 
#   (Saralash jarayonida birinchi sonlar, keyin esa harflar va harf birikmalari joylashadi)
#   Masalan, 
#   Input: 
#   ls=[5,1,35,21,'salom',5,'A','Hayr',12]
#   Output:
#   [1,5,5,12,21,35,'A','Hayr','salom']
ls=[5,1,'C',35,21,'salom',5,'A','Hayr',12]

def BubbleSort(arr:list):
    digit=[]
    letter=[]
    word=[]
    for i in arr:
        if type(i)==str:
            if len(i)==1:
                letter.append(i)
            else:
                word.append(i)
        else:
            digit.append(i)
    ls.clear()

    for i in range(0,len(digit)):
        for j in range(0,len(digit)-1-i):
            if digit[j]>digit[j+1]:
                digit[j],digit[j+1]=digit[j+1],digit[j]
    
    for i in range(0,len(letter)):
        for j in range(0,len(letter)-1-i):
            if letter[j]>letter[j+1]:
                letter[j],letter[j+1]=letter[j+1],letter[j]
    
    for i in range(0,len(word)):
        for j in range(0,len(word)-1-i):
            if word[j]>word[j+1]:
                word[j],word[j+1]=word[j+1],word[j]
    ls.extend(digit)
    ls.extend(letter)
    ls.extend(word)
    print(ls)
    
BubbleSort(ls)