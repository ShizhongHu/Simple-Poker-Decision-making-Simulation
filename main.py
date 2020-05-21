




firsthand = []
secondhand = []

## s refers to spades, c refers to clubs, d refers to diamonds, h refers to hearts
## 11 refers to jacks, 12 refers to queens, 13 refers to kings, 14 refer to aces

totalcash = input("Enter the amount of cash you have currently (in $) :")
firsthandnumber = input("Enter the number of your first card:")
firsthand.append(int(firsthandnumber))
firsthandsuit = input("Enter the suit of your first card:")
firsthand.append(firsthandsuit)
secondhandnumber = input("Enter the number of your second card:")
secondhand.append(int(secondhandnumber))
secondhandsuit = input("Enter the suit of your second card:")
secondhand.append(secondhandsuit)

preflopchecker = input ("Preflop turn? Yes(y) or No(n)?")
preflopbetsize = 0

if preflopchecker == "y":
    if int(firsthand[0]) - int(secondhand[0]) == 0 or int(secondhand[0]) - int(firsthand[0]) == 0:
        preflopbetsize = totalcash
        print("Your maximum bet size : " + preflopbetsize)
    elif (int(firsthand[0]) - int(secondhand[0]) ==1) or (int(secondhand[0])-int(firsthand[0])==1):
        preflopbetsize = 0.1 * int(totalcash) * (max(int(firsthand[0]), int(secondhand[0]))/11)
        print("Your maximum betting size:" + str(preflopbetsize))
    elif firsthand[1]== secondhand[1]:
        preflopbetsize = 0.07 * int(totalcash) * (max(int(firsttand[0]), int(secondhand[0])) / 10)
        print("Your maximum betting size:" + str(preflopbetsize))
    elif int(firsthand[0]) - int(secondhand[0]) == 2 or int(secondhand[0]) - int(firsthand[0]):
        if min(int(firsthand[0]), int(secondhand[0]))>10:
            preflopbetsize = 0.1 * int(totalcash)
            print("Your maximum betting size:" + str(preflopbetsize))
        else:
            print("Fold")
    elif firsthand[1] == secondhand[1]:
        preflopbetsize = 0.1*int(totalcash)
        print("Your maximum bet size:"+ str(preflopbetsize))
    else:
        print("Fold")


flopchecker = input ("Flop turn? Yes(y) or No(n)?")
floptotalcash = input("Enter the amount of cash you have currently (in $) :")

firstcommunitycard = []
secondcommunitycard = []
thirdcommunitycard = []
combination = [firsthand,secondhand,firstcommunitycard,secondcommunitycard,thirdcommunitycard]

firstcommunitycardnumber = input("Enter the number of the first community card:")
firstcommunitycard.append(int(firstcommunitycardnumber))
firstcommunitycardsuit = input("Enter the suit of the first community card:")
firstcommunitycard.append(firstcommunitycardsuit)
secondcommunitycardnumber = input("Enter the number of the second community card:")
secondcommunitycard.append(int(secondcommunitycardnumber))
secondcommunitycardsuit = input("Enter the suit of the second community card:")
secondcommunitycard.append(secondcommunitycardsuit)
thirdcommunitycardnumber = input("Enter the number of the third community card:")
thirdcommunitycard.append(int(thirdcommunitycardnumber))
thirdcommunitycardsuit = input("Enter the suit of the third community card:")
thirdcommunitycard.append(thirdcommunitycardsuit)

numberdifferencecount = 0
samenumbercount = 0
samesuitcount = 0
foldcounter = 0
flopbetsize = 0


if flopchecker == "y":
    for i in range(0,len(combination)):
        for n in range(1,len(combination)-i):
            if combination[i][0] == combination[i+n][0]:
                numberdifferencecount+=1
                combination.pop(i+n)
    if samenumbercount == 1:
        flopbetsize = 0.15 * int(floptotalcash)
        print("Check/Fold, but if your pair is Jacks or greater, your maximum bet size is:" + str(flopbetsize))
    if samenumbercount == 2:
        flopbetsize = 0.2 * int(floptotalcash)
        print("Your maximum bet size is:" + str(flopbetsize))
    if samenumbercount == 3:
        flopbetsize = 0.3* int(floptotalcash)
        print("Your maximum bet size is:" + str(flopbetsize))
    else:
        foldcounter+=1
    ##take into account pair, two pair, three of a kind, full house and four of a kind

    for i in range(len(combination)):
        numberdifferencecount+=combination[i+1][0]-combination[i][0]
    if numberdifferencecount == 4 or numberdifferencecount == -4:
        flopbetsize = int(floptotalcash)*0.4
        print("Your maximum bet size is:" + str(flopbetsize))
    else:
        foldcounter+=1
    ##take into account straight and possibly... four of a kind, three of a kind, two pair or pair

    for i in range(len(combination)):
        if combination[i+1][1] == combination[i][1]:
            samesuitcount+=1
    if samesuitcount == 4:
        flopbetsize = int(floptotalcash)*0.5
        print("Your maximum bet size is:" + str(flopbetsize))
    else:
        foldcounter+=1
    ##take into account a flush

    for i in range(len(combination)):
        if combination[i+1][1] == combination[i][1]:
            samesuitcount+=1
        numberdifferencecount += combination[i+1][0] - combination[i][0]
    if numberdifferencecount == 4 or numberdifferencecount == -4:
        if samesuitcount == 4:
            flopbetsize = int(floptotalcash)
            print("Your maximum betting size"+ str(flopbetsize))
        else:
            foldcounter+=1
    ##take into account a straight flush

    for i in range(0, len(combination)):
        for n in range(1, len(combination) - i):
            if combination[i][1] == combination[i+n][1]:
                samesuitcount += 1
                combination.pop(i+n)
    if samesuitcount == 3:
        flopbetsize = 0.18*2*preflopbetsize
        print("Your estimated ideal bet size:" + str(flopbetsize))
    else:
        foldcounter+=1
    ## we take 0.18, the probability of us drawing a flush during the turn , if we have
    ## 4 cards of the same suit in our combination, multiplied by the ante because that's our expected
    ## returns given that the opponent's hand is such that it is impossible for him to draw a flush
    ## during the turn

    if foldcounter == 5:
        print("Check. If the opponent raises, Fold .")


turnchecker = input("Turn turn? Yes(y) or No(n)?")

fourthcommunitycard = []

fourthcommunitycardnumber = input("Enter the number of the fourth community card:")
fourthcommunitycard.append(fourthcommunitycardnumber)
fourthcommunitycardsuit = input("Enter the suit of the fourth community card:")
fourthcommunitycard.append(fourthcommunitycardsuit)

combination.append(fourthcommunitycard)

turnbetsize = 0

while flopchecker == "y":
    if turnchecker == "y":
        for i in range(0,len(combination)):
            for n in range(1,len(combination)-i):
                if combination[i][0] == combination[i+n][0]:
                    numberdifferencecount+=1
                combination.pop(i+n)
        if samenumbercount == 1:
            turnbetsize = 0.15 * (int(flopbetsize) + int(preflopbetsize))
            print("Check/Fold, but if your pair is Jacks or greater, your maximum bet size is:" + str(turnbetsize))
        if samenumbercount == 2:
            turnbetsize = 0.2 * (int(flopbetsize) + int(preflopbetsize))
            print("Your maximum bet size is:" + str(flopbetsize))
        if samenumbercount == 3:
            turnbetsize = 0.3* (int(flopbetsize) + int(preflopbetsize))
            print("Your maximum bet size is:" + str(turnbetsize))
        else:
            foldcounter+=1
    ##take into account pair, two pair, three of a kind, full house and four of a kind

        for i in range(len(combination)):
            numberdifferencecount+=combination[i+1][0]-combination[i][0]
        if numberdifferencecount == 4 or numberdifferencecount == -4:
            turnbetsize = (int(flopbetsize) + int(preflopbetsize))*0.4
            print("Your maximum bet size is:" + str(turnbetsize))
        else:
            foldcounter+=1
    ##take into account straight and possibly... four of a kind, three of a kind, two pair or pair

        for i in range(len(combination)):
            if combination[i+1][1] == combination[i][1]:
                samesuitcount+=1
        if samesuitcount == 4:
            turnbetsize = (int(flopbetsize) + int(preflopbetsize))*0.5
            print("Your maximum bet size is:" + str(turnbetsize))
        else:
            foldcounter+=1
    ##take into account a flush

        for i in range(len(combination)):
            if combination[i+1][1] == combination[i][1]:
                samesuitcount+=1
            numberdifferencecount += combination[i+1][0] - combination[i][0]
            if numberdifferencecount == 4 or numberdifferencecount == -4:
                if samesuitcount == 4:
                    turnbetsize = (int(flopbetsize) + int(preflopbetsize))
                    print("Your maximum betting size"+ str(turnbetsize))
            else:
                foldcounter+=1
        ##take into account a straight flush

        if foldcounter == 4:
            print("Check. If the opponent raises, Fold .")



riverchecker = input("River turn? Yes(y) or No(n)?")
rivertotalcash = input("Input the total amount of cash you have currently ($):")


fifthcommunitycard = []

fifthcommunitycardnumber = input("Enter the number of the fourth community card:")
fifththcommunitycard.append(fifthcommunitycardnumber)
fifthcommunitycardsuit = input("Enter the suit of the fourth community card:")
fifthcommunitycard.append(fifthcommunitycardsuit)

combination.append(fifthcommunitycard)

riverbetsize = 0
sparecash = 0


while flopchecker == "y":
    while turnchecker == "y":
        if riverchecker == "y":
            for i in range(0,len(combination)):
                for n in range(1,len(combination)-i):
                    if combination[i][0] == combination[i+n][0]:
                        numberdifferencecount+=1
                    combination.pop(i+n)
            if samenumbercount == 1:
                riverbetsize = 0.15 * (int(flopbetsize) + int(preflopbetsize)+int(turnbetsize))
                print("Check/Fold, but if your pair is Jacks or greater, your maximum bet size is:" + str(riverbetsize))
            if samenumbercount == 2:
                riverbetsize = 0.2 * (int(flopbetsize) + int(preflopbetsize)+int(turnbetsize))
                print("Your maximum bet size is:" + str(riverbetsize))
            if samenumbercount == 3:
                riverbetsize = 0.3* (int(flopbetsize) + int(preflopbetsize)+int(turnbetsize))
                print("Your maximum bet size is:" + str(riverbetsize))
            else:
                foldcounter+=1
        ##take into account pair, two pair, three of a kind, full house and four of a kind

            for i in range(len(combination)):
                numberdifferencecount+=combination[i+1][0]-combination[i][0]
            if numberdifferencecount == 4 or numberdifferencecount == -4:
                riverbetsize = (int(flopbetsize) + int(preflopbetsize)+int(turnbetsize))*0.4
                print("Your maximum bet size is:" + str(riverbetsize))
            else:
                foldcounter+=1
        ##take into account straight and possibly... four of a kind, three of a kind, two pair or pair

            for i in range(len(combination)):
                if combination[i+1][1] == combination[i][1]:
                    samesuitcount+=1
            if samesuitcount == 4:
                riverbetsize = (int(flopbetsize) + int(preflopbetsize)+int(turnbetsize))*0.5
                print("Your maximum bet size is:" + str(riverbetsize))
            else:
                foldcounter+=1
        ##take into account a flush

            for i in range(len(combination)):
                if combination[i+1][1] == combination[i][1]:
                    samesuitcount+=1
                numberdifferencecount += combination[i+1][0] - combination[i][0]
                if numberdifferencecount == 4 or numberdifferencecount == -4:
                    if samesuitcount == 4:
                        riverbetsize = (int(flopbetsize) + int(preflopbetsize)+int(turnbetsize))
                        print("Your maximum betting size"+ str(riverbetsize))
                else:
                    foldcounter+=1
            ##take into account a straight flush

            if foldcounter == 4:
                sparecash = 0.05*int(rivertotalcash)
                print("Check. Fold if opponent raises above " + str(sparecash))































