import random
import matplotlib.pyplot as plt
import numpy as np


def main():
    ### OPDRACHT 1 ###
    # Gebruik de lijsten x y en z voor de grafieken van opdracht 1
    # x = ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    # y = ([3, 6, 8, 10, 12, 12, 4, 14, 7, 10])
    # z = []
    # for i in range(0,10):
    #     n = random.randint(1,100)
    #     z.append(n)
    #     #print(z)

    # z = np.asarray()
    # plt.scatter(x = x, y = y)
    # plt.show()

    # plt.plot(x, y, label = "regel 1")
    # plt.title("twee regels op dezelfde grafiek")
    # plt.xlabel("x axis name")
    # plt.ylabel("y axis name")
    # plt.legend()
    # plt.show()

    # plt.hist(x = y, label = "y")
    # plt.hist(x = z, label = "z")
    # plt.grid(axis = "y", alpha = 0.75)
    # plt.xlabel("x naam")
    # plt.ylabel("y naam")
    # plt.title("histogram")
    # plt.legend()
    # plt.show()

    # fig1, ax1 = plt.subplots()
    # ax1.pie(x, explode=x, labels=x, autopct="%.001f%%",
    #       shadow=True, startangle=90)
    # ax1.axis("equal")
    # plt.show()

    # x_axis = np.arange(len(x))

    # plt.bar(x_axis - 0.2, y, 0.4, label = "y")
    # plt.bar(x_axis + 0.2, z, 0.4, label = "z")
    # plt.xticks(x_axis, x)
    # plt.xlabel("X label")
    # plt.ylabel("y label")
    # plt.title("the numbers jason what do they mean")
    # plt.legend()
    # plt.show()

    ### OPDRACHT 2 ###
    # Bestand voor opdracht 2
    #patienten = "patienten.csv"
    #data = []
    #med_A_tijdelijk = []
    #med_B_tijdelijk = []
    #patient_id_tijdelijk = []
    #doc = []
    #file = open(patienten, "r")
    #line = 0
    #for lines in file:
    #    line+=1
    #    lines = lines.replace("\n", "")

    #    lines = lines.split(",")

    #    data.append((lines))
        #print(data)
    #print(line)
   # index_med_a = 1
   # index_two = 1
   # index_med_b = 2
   # line -= 2
   # docter = 3
   # patient = 0

    #for medicin in range(line):
        #print(index_two)

     #   doc.append(data[index_two].pop(docter))
     #   med_B_tijdelijk.append(data[index_two].pop(index_med_b))
     #   med_A_tijdelijk.append(data[index_two].pop(index_med_a))
     #   patient_id_tijdelijk.append(data[index_two].pop(patient))

      #  index_two+=1
    #med_B = []
    #nummer = 0
    #print(med_B_tijdelijk)
    #for items in med_B_tijdelijk:

     #   B = med_B_tijdelijk.pop(nummer)
      #  float(B)
      #  med_B.append(B)
      #  nummer +=1
        #print(index_two)
        #print(med_A)
        #print(med_B)

    #med_A = []
    #patient_id = []
    #print(med_A_tijdelijk)
   # length = len(med_A_tijdelijk)
   # length += 1


 #   index = 0
 #   length = len(patient_id_tijdelijk)
 #   length+=1
 #   for i in range(length):
 #       nummer = med_A_tijdelijk[index]
 #       nummer = float(nummer)
 #       med_A.append(nummer)

 #       nummer = med_B_tijdelijk[index]
 #       nummer = float(nummer)
 #       med_B.append(nummer)


 #       nummer = patient_id_tijdelijk[index]
 #       nummer = float(nummer)
 #       patient_id.append(nummer)
 #       index+=1

 #   janssen = 0
 #   berends = 0
 #   doc_namen = []
 #   for items in doc:
 #       if items == "Janssen":
 #           janssen+=1
 #           if items not in doc_namen:
 #               doc_namen.append(items)
 #       elif items == "Berends":
 #           berends += 1
 #           if items not in doc_namen:
#                doc_namen.append(items)



    #doc_freq = []
    #doc_freq.append(janssen)
    #doc_freq.append(berends)

    #med_b_greater_50 = 0
    #med_b_40 = 0
    #med_b_smaller_40 = 0

    #for medicijn in med_B:

        #if float(medicijn) >= 50:

      #      med_b_greater_50 += 1
     #   elif float(medicijn) >= 40 and float(medicijn) < 50:
     #       med_b_40 += 1
     #   elif float(medicijn) < 40:
     #       med_b_smaller_40 +=1

    #totaal_patienten = med_b_greater_50 + med_b_40 + med_b_smaller_40
    #percentage_greater_50 = med_b_greater_50 / totaal_patienten * 100
    #percentage_40 = med_b_40 / totaal_patienten * 100
    #percentage_smaller_40 = med_b_smaller_40 / totaal_patienten * 100

    #groepen_med_b = [f"percentage smaller than 40 mg:{percentage_smaller_40}%", f"between 40mg and below 50 mg:{percentage_40}%", f"greater than 50mg: {percentage_greater_50}%"]
    #percentages_med_b = []
    #percentages_med_b.append(percentage_smaller_40)
    #percentages_med_b.append(percentage_40)
    #percentages_med_b.append(percentage_greater_50)

       # index_two += 1
        # print(med_A)
        # print(med_B)
    # print(data[3][2])
    #plt.scatter(x=med_A, y=med_B)
    #plt.show()

    #plt.plot(patient_id, med_A)
    #plt.title("med A per patient")
    #plt.xlabel("patient id")
    #plt.ylabel("medicin A")
    #plt.show()

    #plt.hist(x = doc)
    #plt.ylabel("berends en janssen")
    #plt.xlabel("amount of patients")
    #plt.show()


    #plt.pie(percentages_med_b, labels= groepen_med_b)
    #plt.show()
    #print(med_A)
    #plt.scatter( doc, med_A, label = "medicijn A")
    #plt.scatter( med_B, doc, label  = "medicijn B")
    #plt.legend()
    #plt.show()


    ### OPDRACHT 3 ###
    # Bestand voor opdracht 3
    # gist = "yeast_genes.csv"
    # file = open(gist, "r")
    # yeast = []
    # #status = 0
    # nummer = 0
    # for lines in file:
    #     lines = lines.replace("\n", "")
    #
    #
    #     lines = lines.split(",")
    #     #print(lines)
    #     if nummer == 0:
    #         status = lines.index("validation")
    #     #status += status
    #         #print(status)
    #         yeast.append(lines)
    #         nummer += 1
    #     else:
    #         yeast.append(lines)
    #         nummer+=1
    # #print(yeast)
    #
    # #status = yeast.index("validation")
    # #print(status)
    #
    # #status = yeast[0].index("validation")
    # #print(status)
    # #print(yeast[0][1])
    # state_of_gene = []
    # total_states_of_gene = []
    # index = 0
    # for item in yeast:
    #     #print(item)
    #
    #     if yeast[index][status] not in state_of_gene:
    #         state_of_gene.append(yeast[index][status])
    #         #print(state_of_gene)
    #         total_states_of_gene.append(yeast[index][status])
    #         index +=1
    #     else:
    #         total_states_of_gene.append(yeast[index][status])
    #         index+=1
    #
    # if "validation" in state_of_gene:
    #
    #     gello = state_of_gene.index("validation")
    #     state_of_gene.pop(gello)
    #     #print(state_of_gene)
    # #print(state_of_gene)
    # #print(state_of_gene)
    # getal = 0
    # total_values = []
    # for items in state_of_gene:
    #     values = total_states_of_gene.count(state_of_gene[getal])
    #
    #     total_values.append(values)
    #     getal+=1
    # #print(total_values)
    # #print(total_states_of_gene)
    # #print(state_of_gene)
    # plt.bar(state_of_gene, total_values)
    # plt.title("twee regels op dezelfde grafiek")
    # plt.xlabel("status van gen")
    # plt.ylabel("aantal keer dat genstatus voorkomt")
    # plt.title("het aantal voorkomen in bestand van genstatus")
    # plt.legend(["aantal dat de genstatus voorkomt in het bestand "])
    # plt.show()

    ### OPDRACHT 4 ###
    # Bestand voor opdracht 4
    test = "test.csv"
    file = open(test, "r")

    eten = []
    nummer = 0
    for lines in file:
        lines = lines.replace("\n", "")

        lines = lines.split(";")
        # print(lines)
        if nummer == 0:
            status = lines.index("validation")
            # status += status
            # print(status)
            eten.append(lines)
            nummer += 1
        else:
            eten.append(lines)
            nummer += 1
    # print(yeast)

    # status = yeast.index("validation")
    # print(status)

    # status = yeast[0].index("validation")
    # print(status)
    # print(yeast[0][1])
    state_of_eten = []
    total_states_of_eten = []
    index = 0
    for item in eten:
        # print(item)

        if eten[index][status] not in state_of_eten:
            state_of_eten.append(eten[index][status])
            # print(state_of_gene)
            total_states_of_eten.append(eten[index][status])
            index += 1
        else:
            total_states_of_eten.append(eten[index][status])
            index += 1

    if "validation" in state_of_eten:
        gello = state_of_eten.index("validation")
        state_of_eten.pop(gello)
        # print(state_of_gene)
    # print(state_of_gene)
    # print(state_of_gene)
    getal = 0
    total_eten = []
    for items in state_of_eten:
        values = total_states_of_eten.count(state_of_eten[getal])

        total_eten.append(values)
        getal += 1

    plt.bar(state_of_eten, total_eten)
    plt.xlabel("status van unieke identifier")
    plt.ylabel("aantal keer dat unieke identifier voorkomt")
    plt.title("het aantal voorkomen in bestand van status unieke identifier")
    plt.legend(["aantal dat status van de unieke identifier voorkomt in het bestand "])
    plt.show()


main()

