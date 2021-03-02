# BestBuyCodingChallenge
# Author: Surekshya Sharma
import statistics
import matplotlib.pyplot as plt
from collections import Counter


# open and read the file after the appending:


def readFile():
    try:
        FILENAME = 'fish.txt'
        print("Success Reading file...")
        lines_file = open(FILENAME, 'r').read().split('\n')
        print("-----------------------------------------------------------------------------------------------------")
        fishStatistic(lines_file)

    except IOError:
        print("Could not read file:", FILENAME)


def fishStatistic(lines_file):
    # Overall array of fish data
    fish_data = []
    # For graphical representation
    fish_Species = []
    location = []
    length = []
    # fish Species
    Walleye = []
    White_Sucker = []
    Yellow_Perch = []
    Smallmouth_Bass = []
    Northern_Pike = []
    Sunfish = []
    # location
    itasca = []
    vermilion = []
    snail = []
    superior = []
    carlos = []
    # total number of lines
    for i in lines_file:
        fish_Stat = i.split(",")
        # creating the 2D
        fish_data.append([fish_Stat[0], fish_Stat[1], fish_Stat[2]])
        # individual array for fish_Species, location and length for graphical representation
        fish_Species.append(fish_Stat[0])
        location.append(fish_Stat[1])
        length.append(fish_Stat[2])
    print("Length:", Counter(fish_Species).items())
    print("Location:", Counter(location).items())
    for i in fish_data:
        # creating array for different length of different fish species
        if i[0] == 'Walleye':
            Walleye.append(int(i[2]))
        if i[0] == 'White Sucker':
            White_Sucker.append(int(i[2]))
        if i[0] == 'Yellow Perch':
            Yellow_Perch.append(int(i[2]))
        if i[0] == 'Smallmouth Bass':
            Smallmouth_Bass.append(int(i[2]))
        if i[0] == 'Northern Pike':
            Northern_Pike.append(int(i[2]))
        if i[0] == 'Sunfish':
            Sunfish.append(int(i[2]))
        if i[1] == 'Itasca':
            itasca.append(int(i[2]))
        if i[1] == 'Vermilion':
            vermilion.append(int(i[2]))
        if i[1] == 'Snail':
            snail.append(int(i[2]))
        if i[1] == 'Superior':
            superior.append(int(i[2]))
        if i[1] == 'Carlos':
            carlos.append(int(i[2]))
    # creating 2D array
    fish_species_average = [["Walleye", find_average(Walleye)],
                            ["White Sucker", find_average(White_Sucker)],
                            ["Yellow Perch", find_average(Yellow_Perch)],
                            ["Smallmouth Bass", find_average(Smallmouth_Bass)],
                            ["Northern Pike", find_average(Northern_Pike)],
                            [" Sunfish", find_average(Sunfish)]]

    # calculating the average of all species
    print("1a.The average size of Walleye is", fish_species_average[0][1])
    print("1b.The average size of White Sucker is", fish_species_average[1][1])
    print("1c.The average size of Yellow Perch is", fish_species_average[2][1])
    print("1d.The average size of Smallmouth Bass is", fish_species_average[3][1])
    print("1e.The average size of Northern Pike is", fish_species_average[4][1])
    print("1f.The average size of Sunfish is", fish_species_average[5][1])

    max_num_1 = max(fish_species_average[0][1], fish_species_average[1][1], fish_species_average[2][1],
                    fish_species_average[3][1], fish_species_average[4][1], fish_species_average[5][1])

    for i in fish_species_average:
        largest = i[1]
        if largest == max_num_1:
            print("2.The average largest fish is", i[0])
            print(i)

    # lake with the largest fish
    average_Compare_lake = [[" Itasca", find_average(itasca)], ["Vermilion", find_average(vermilion)],
                            ["Snail", find_average(snail)], ["Superior", find_average(superior)],
                            ["Carlos", find_average(carlos)]]

    max_num_2 = max(average_Compare_lake[0][1], average_Compare_lake[1][1], average_Compare_lake[2][1],
                    average_Compare_lake[3][1], find_average(carlos))
    for i in average_Compare_lake:
        largest = i[1]
        if largest == max_num_2:
            print("3.The average largest fish is found in", i[0])
            print(i)

    # median = statistics.median(sorted(new_length))
    itasca.sort()
    median_itasca = statistics.median(sorted(itasca))
    vermilion.sort()
    median_vermilion = statistics.median(sorted(vermilion))
    snail.sort()
    median_snail = statistics.median(sorted(snail))
    superior.sort()
    median_superior = statistics.median(sorted(superior))
    carlos.sort()
    median_carlos = statistics.median(sorted(carlos))
    median_lake = [["Itasca", median_itasca], ['Vermilion', median_vermilion], ['Snail', median_snail],
                   ["Superior", median_superior], ["Carlos", median_carlos]]
    highest_median = max(median_itasca, median_vermilion, median_snail, median_superior, median_carlos)
    for i in median_lake:
        largest = i[1]
        if largest == highest_median:
            print("4.The lake with the largest median (50th percentile) fish", i[0])
            print(i)
    # error fixed using changing Length: ['15', '45', '30',.....] to Length: [15, 45, 30] .Error: 'str' to
    # numerator/ denominator
    print("------------------------------Date for all fish species "
          "comparision----------------------------------------------------")
    new_length = list(map(int, length))
    # print("1.The average size of all fish species is", average(new_length))
    print("5.The average highest size of all fish species is", max(new_length))
    index_of_Largest = new_length.index(max(new_length))
    print("6.The largest fish species is " + fish_data[index_of_Largest][0])
    print(fish_data[index_of_Largest])
    print("7.The lake with the largest fish species is " + fish_data[index_of_Largest][1])

    graphicalRepresentation(fish_Species, new_length, median_lake)


def find_average(input_array):
    sum_total = 0
    for y in input_array:
        sum_total = sum_total + y
        average = round(sum_total / len(input_array))
    return average


def graphicalRepresentation(fish_Species, new_length):
    # relation between fishSpecies and length.
    # the average Largest Fish
    plt.bar(fish_Species, new_length, color='g', label='File Data')
    plt.xlabel('Fish Species', fontsize=12)
    plt.ylabel('Length in Cm', fontsize=12)
    plt.title('The average Largest of all Fish Species', fontsize=20)
    plt.legend()
    plt.show()
    plt.bar(fish_Species, new_length, color='g', label='File Data')
    plt.xlabel('Fish Species', fontsize=12)
    plt.ylabel('Length in Cm', fontsize=12)
    plt.title('The average Largest of all Fish Species', fontsize=20)
    plt.legend()
    plt.show()
    # scatter plot showing the length of the fish species
    plt.scatter(new_length, fish_Species)
    plt.show()


readFile()
