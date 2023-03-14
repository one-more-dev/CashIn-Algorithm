
print("The software will provide the least bank notes as possible, according to the value you asked")
print("I wondered how that algorithm would work based on when I withdraw money from the cash machine in my bank")

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
            try:
                total.pop(-tries)
            except:
                print("Not able to finish operation, lack of banknotes. Try another value")
                break
        else:
            print(f"Wait to cash the money: ${cash}, {total}")
            break
            return total
           
        if tries == len(banknotes):
	        print("Handle the money was not possible due the lack of banknotes. Try another value")
	        break


def execute():
	validCash = cashInValidation()
	c = calcNotes(validCash)


execute()
