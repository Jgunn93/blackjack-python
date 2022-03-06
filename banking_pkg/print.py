def printer(hands):
    for i in range(len(hands)):
        if(hands[i][1] < 10):
            print(hands[i][1],"of",hands[i][0])
        elif(hands[i][1]==11):
            print("J of",hands[i][0])
        elif(hands[i][1]==12):
            print("Q of",hands[i][0])
        elif(hands[i][1]==13):
            print("K of",hands[i][0])
        elif(hands[i][1]==14):
            print("A of",hands[i][0])