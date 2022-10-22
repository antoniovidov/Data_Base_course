import io

with open('The_Machine_That_Won_the_War_AA.txt', 'r', encoding="utf-8") as f:
    count = 0
    f_content = f.read()
    print(f_content)
    for i,j in list(enumerate(f_content)):
        if f_content[i]=="в" and f_content[i+1]=="а" and f_content[i+2]=="к":
            count+=1
    

    f2 = list(reversed(f_content))
    count2=0
    for i,k in list(enumerate(f2)):
        print(k, end = "")
        if f2[i]=="в" and f2[i+1]=="а" and f2[i+2]=="к":
            count2+=1
    print(count)
    print(count2)
    
    