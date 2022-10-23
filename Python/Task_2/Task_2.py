import io 
import os
import sys
import datetime
## важни бибилиотеки
##with open("bonbon.txt","w") as f:
##   pass
def insert():   ##дефинираме функция
    answer = ""
<<<<<<< Updated upstream
    with open("bonbon.txt", "a") as f: ## отваряме текстовия фаил за append


        f.write( "Name~~~~~~~~~~~Family~~~~~~~~~~~~~~Numb~Town~~~~~~~~~~~~~~~~GROMB_Date~~~~Scor" +"\n")

=======
    thetop = "Name~~~~~~~~~~~Family~~~~~~~~~~~~~~Numb~Town~~~~~~~~~~~~~~~~GROMB_Date~~~~Scor"+"\n"
    value = bool
    with open("bonbon.txt", "a") as f:
        print("Welcome")
    f.close()
    with open("bonbon.txt","r") as f:
        if thetop not in f.read():
            value = True
        else:
            value = False
    f.close()        
    with open("bonbon.txt", "a") as f: ## отваряме текстовия фаил за append
        if value == True:
            f.write(thetop)
        elif value == False:
            f.write("\n")
>>>>>>> Stashed changes

        q = input("Do you want to make a new lineY/N-> ")
        if q=="N":
            print("bye bye!")
            exit()
        Name = input("Enter your first name:") ## вкарваме име под колона name и проверяваме дали е по-голямо от 15 символа 
        NumberS =""
        while len(Name) > 15:
            print("Error: Name cannot be more then 15 characters,want to try again Y/N")
            answer = input()
            if answer=="Y":
                Name = input("Enter your first name:")
            elif answer=="N":
                exit()
        while len(Name)<15:
            Name = Name+"~"
        f.seek(0)
        f.write(Name)


        Family = input("Enter your second name:")## вкарваме фамилно име под колона family и проверяваме дали е по-голямо от 20 символа
        while len(Family) > 20:
            print("Error: Family cannot be more then 20 characters,want to try again Y/N")
            answer = input()
            if answer=="Y":
                Family = input("Enter your second name:")
            elif answer=="N":
                exit()
        while len(Family)<20:
            Family = Family+"~"
        f.seek(15)
        f.write(Family)


        Number = int(input("Enter your class number: "))## вкарваме число под колона Numb и проверяваме дали е по-голямо от 5 символа
        NumberS =""
        while len(NumberS) > 5:
            print("Error: Number cannot be more then 5 characters,want to try again Y/N")
            answer = input()
            if answer=="Y":
                Number = input("Enter your class number:")
            elif answer=="N":
                exit()
        NumberS = str(Number)       
        while len(NumberS)<5:
            NumberS = NumberS + "~"
        f.seek(35)
        f.write(NumberS)


        Town = input("Enter your Town name:")## вкарваме име на град под колона Town и проверяваме дали е по-голямо от 20 символа
        while len(Town) > 20:
            print("Error: Town name cannot be more then 20 characters,want to try again Y/N")
            answer = input()
            if answer=="Y":
                Town = input("Enter your Town name:")
            elif answer=="N":
                exit()
        while len(Town)<20:
            Town = Town+"~"
        f.seek(40)
        f.write(Town)

        Gender = input("Enter your gender->M/W/N : ")## вкарваме пола под  колона Gender и проверяваме дали е по-голямо от 1 символ
        while len(Gender) > 1:
            print("Error: Gender  cannot be more then 1 character,want to try again Y/N")
            answer = input()
            if answer=="Y":
                Gender = input("Enter your Gender :")
            elif answer=="N":
                exit()
        f.seek(60)
        f.write(Gender)


        Room = int(input("Enter your room number "))## вкарваме пола под  колона Rom и проверяваме дали е по-голямо от 3 символa
        RoomS = ""
        RoomS = str(Room)
        while len(RoomS) > 3:
            print("Error: Room  cannot be more then 3 character,want to try again Y/N")
            answer = input()
            if answer=="Y":
                Room = input("Enter your Room number :")
            elif answer=="N":
                exit()
        while len(RoomS)<3:
            RoomS = RoomS + "~" 
        f.seek(61)
        f.write(RoomS)

        d=input("When is your B'day? (in YYYY-MM-DD) ") ## вкарваме пола под  колона B_Date и проверяваме дали е по-голямо от 10 символa
        d=datetime.datetime.strptime(d,'%Y-%m-%d').date()##трябва да се направи try catch проверка
        dS = str(d)
        f.seek(64)
        f.write(dS)
<<<<<<< Updated upstream
<<<<<<< Updated upstream

        score = float(input(" Number from 2 to 6 - > "))## вкарваме пола под  колона Score и проверяваме дали е по-голямо от 4 символa
=======
        
        score = float(input("Number from 2 to 6 - > "))## вкарваме пола под  колона Score и проверяваме дали е по-голямо от 4 символa
        while score < 2 or score > 6:
            print("Error: Score must be between 2 and 6")
            score = float(input("Number from 2 to 6 - > "))
>>>>>>> Stashed changes
=======
        score = float(input("Score from 2 to 6 - > "))## вкарваме пола под  колона Score и проверяваме дали е по-голямо от 4 символa
        while score < 2 or score > 6:
            print("Invalid score,try again")
            score = float(input("Score from 2 to 6 - > "))

>>>>>>> Stashed changes
        scoreS = ""
        scoreS = str(score)
        while len(scoreS) > 4:
            print("Error: Number cannot be more then 4 characters,want to try again Y/N")
            answer = input()
            if answer=="Y":
                score = input("Enter your class number:")
            elif answer=="N":
                exit()
        while len(scoreS) < 4:
            scoreS = scoreS + "~"
        f.seek(74)
        f.write(scoreS)
<<<<<<< Updated upstream

<<<<<<< Updated upstream
=======

>>>>>>> Stashed changes



    f.close()    

insert()
=======
        
        
        
        
    f.close()    
##insert()
def select():
    selection = input("What criteria do you want to search by -> Name/Family/Numb/Town/G/ROM/B_Date/Scor")
    with open("bonbon.txt", 'r') as fp:
        lines = len(fp.readlines())
        print('Total Number of lines:', lines)
def main():
    choice = input("What do you want to do -> Insert/Select/Exit -> ")
    while choice != "Exit":
        if choice == "Insert":
            insert()
            choice = ""
        elif choice == "Select":
            try:
                with open("bonbon.txt","r") as f:
                    f.read()
                f.close()
                select()
                choice = ""
            except:
                SV = False
                while SV == False:
                    choice = ""
                    choice = input("File not created , need to use Insert first! What do you want to do -> Insert/Exit ->")
                    if choice == "Exit":
                        sys.exit()
                    elif choice == "Insert":
                        insert()
                        SV = True    
        choice = input("What do you want to do -> Insert/Select/Exit -> ")    
    print("Bye bye!")        
    sys.exit()
main()
>>>>>>> Stashed changes
