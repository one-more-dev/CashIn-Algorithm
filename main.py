
print("The software will provide the least bank notes as possible, according to the value you asked")

banknotes = [20,50,100]
banknotes.sort()


def cashInValidation():
    validValue = False
    while validValue == False:
        cash = int(input("How much to cash in? "))
        if cash < banknotes[0]:
            validValue
        elif cash % 10 != 0:
            validValue
        else:
            validValue == True
            return cash



def calcNotes(cash):

    total = []
    reduceList = 0
    tries = 0

    while sum(total) != cash:
        for i in range(len(banknotes)-1+reduceList,-1,-1):
            while sum(total) < cash:
                total.append(banknotes[i])
                if sum(total) > cash:
                    total.pop(-1)
                    break
                elif sum(total) == cash:
                    print("Done!")
                    break
                
        if sum(total) != cash:
            reduceList -= 1
            tries += 1
            total.pop(-tries)
        else:
            print("Now let you go!")
            break
           
        if tries == len(banknotes):
            break

    return total


money = cashInValidation()
n = calcNotes(money)




