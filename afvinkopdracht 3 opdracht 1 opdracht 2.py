import random

def random_numbers():
    """"maakt 100 random nummers tussen 1 en 10
    input:
     de dictionary random

    output:
    random_numbers - dictionary """
    random_numbers = {}
    getallen = []
    i = 0
    for i in range(100):
     #   print(i)
        i+=1
        hoi = random.randint(1,11)
        #print(hoi)
        getallen.append(hoi)
    #print(getallen)
    print(getallen)
    nummer = 1
    number = []

    for i in range(11):
        nummers = getallen.count(nummer)
        print(nummers)
        number.append(nummers)
        nummer += 1
        print(nummer)
        #print(getallen)
    oss = 0
    breda = []
    for i in range(11):
        breda.append(oss)
        oss += 1
    index = 0
    for item in number:
        random_numbers[breda[index]] = number[index]
        index +=1
    print(random_numbers)
def main():
    random_numbers()
main()
