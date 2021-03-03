# BestBuyCodingChallenge
# Author: Surekshya Sharma
import statistics
import matplotlib.pyplot as plt
from collections import Counter


# open and read the file after the appending


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
    fish_data_species = dict()
    fish_data_lake = dict()
    fish_data = []
    # For graphical representation
    fish_Species = []
    lakes = []
    length = []

    for i in lines_file:
        fish_Stat = i.split(",")
        # creating the 2D 2D[[][]...]
        fish_data.append([fish_Stat[0], fish_Stat[1], fish_Stat[2]])
        # individual array for fish_Species, location and length for graphical representation
        fish_Species.append(fish_Stat[0])
        lakes.append(fish_Stat[1])
        length.append(int(fish_Stat[2]))
        print(length)

    # creating a dynamic empty array for different fish species
    for i in Counter(fish_Species).items():
        fish_data_species[i[0]] = []
    # appending in an empty array of fish_data_species[i[0]] of different length of different fish species
    for i in fish_data:
        fish_data_species[i[0]].append(int(i[2]))
    # print(fish_data_species)

    # calculating the average of all species
    fish_species_average = dict()

    for i in fish_data_species:
        fish_species_average[i] = find_average(fish_data_species[i])
        print("1.The average size of ", i, "is", fish_species_average[i])

    largest_average = 0
    largest_species = ''
    for i in fish_species_average:
        if fish_species_average[i] > largest_average:
            largest_average = fish_species_average[i]
            largest_species = i

    print("2.fish species with Largest average is",largest_species," (",largest_average,")")

    # average lake---------------------------------------------------
    # creating a dynamic array for different lake species
    for i in Counter(lakes).items():
        fish_data_lake[i[0]] = []
    # print(fish_data_lake)
    for i in fish_data:
        # creating array for different length of different fish species
        fish_data_lake[i[1]].append(int(i[2]))
    # print(fish_data_lake)

    lakes_average = dict()
    for i in fish_data_lake:
        lakes_average[i] = find_average(fish_data_lake[i])
        print("3.The average size of ", i, "is", lakes_average[i])
    # print(lakes_average)

    largest_lake_average = 0
    largest_lake = ''
    for i in lakes_average:
        if lakes_average[i] > largest_lake_average:
            largest_lake_average = lakes_average[i]
            largest_lake = i

    print("Lake ith Largest average is", largest_lake, " (",largest_lake_average, ")")

    lakes_median = dict()
    for i in fish_data_lake:
        lakes_median[i] = find_median(fish_data_lake[i])
        print("4.The median size of ", i, "is", lakes_median[i])
    # print(lakes_median)

    largest_lake_median = 0
    largest_lake2 = ''
    for i in lakes_median:
        if lakes_median[i] > largest_lake_median:
            largest_lake_median = lakes_median[i]
            largest_lake2 = i

    print("4.Lake with Largest median is", largest_lake2, " (", largest_lake_median, ")")

    graphicalRepresentation(fish_Species, length, lakes_median, lakes_average, lakes)


def find_average(input_array):
    sum_total = 0
    for y in input_array:
        sum_total = sum_total + y
        average = round(sum_total / len(input_array))
    return average


def find_median(input_array):
    input_array.sort()
    # print(input_array)
    N = len(input_array)
    median_position = ((N+1)/2)-1
    if median_position % 2 == 0:
        median = input_array[int(median_position)]
    else:
        median = (input_array[int(median_position-0.5)] + input_array[int(median_position+0.5)])/2
    # print(statistics.median(input_array))
    return median


def graphicalRepresentation(fish_Species, length, lakes_median, lakes_average,lakes):
    # relation between fishSpecies and length.
    # the average Largest Fish of all species
    plt.bar(fish_Species, length, color='g', label='File Data')
    plt.xlabel('Fish Species', fontsize=12)
    plt.ylabel('Length in Cm', fontsize=12)
    plt.title('The average Largest of all Fish Species', fontsize=20)
    plt.show()
    # Showing The average largest fish is found
    for i in lakes_average:
        plt.bar(i, lakes_average[i], color='g', label='File Data')
        plt.xlabel('Fish Species', fontsize=12)
        plt.ylabel('Length in Cm', fontsize=12)
        plt.title('The average largest fish is found', fontsize=20)
    plt.show()
    # Showing The lake with the largest median (50th percentile) fish
    for i in lakes_median:
        plt.bar(i, lakes_median[i], color='g', label='File Data')
        plt.xlabel('Fish Species', fontsize=12)
        plt.ylabel('Length in Cm', fontsize=12)
        plt.title('The lake with the largest median (50th percentile) fish', fontsize=20)
    plt.show()

    # scatter plot showing the length of the all fish species
    plt.scatter(length, fish_Species)
    plt.show()


readFile()
