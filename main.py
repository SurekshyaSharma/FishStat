# BestBuyCodingChallenge
# Author: Surekshya Sharma

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

    fish_Species = []
    location = []
    length = []
    # total number of lines
    for i in lines_file:
        fish_Stat = i.split(",")
        fish_Species.append(fish_Stat[0])
        location.append(fish_Stat[1])
        length.append(fish_Stat[2])

    # error fixed using changing Length: ['15', '45', '30',.....] to Length: [15, 45, 30] .Error: 'str' to
    # numerator/ denominator
    new_length = list(map(int, length))
    max_num = 0
    sum_total = 0

    for lenF in new_length:
        sum_total = sum_total + lenF
        if lenF >= len(new_length):
            max_num = lenF
    print("The average is", round(sum_total/len(new_length)))
    print("The average highest number is", max_num,)
    index_of_Largest = new_length.index(max_num) + 1

    # print(Counter(new_length).items())
    for il in location:
        index_of_Largest = il
    print(index_of_Largest)

    for nl in fish_Species:
       name = nl
    print(name)

    # comparing two different array location and length

    print('.....................................................................................................')
    graphicalRepresentation(fish_Species, location, new_length)


def graphicalRepresentation(fish_Species, location, new_length):
    # relation between fishSpecies and length.
    # the average Largest Fish
    plt.bar(fish_Species, new_length, color='g', label='File Data')
    plt.xlabel('Fish Species', fontsize=12)
    plt.ylabel('Length in Cm', fontsize=12)
    plt.title('The average Largest Fish', fontsize=20)
    plt.legend()
    # plt.show()
    # relation between fishSpecies and length and the lake with the average largest fish
    plt.bar(location, new_length, color='g', label='File Data')
    plt.xlabel('Fish Species', fontsize=12)
    plt.ylabel('Length in Cm', fontsize=12)
    plt.title('Location and  the length of the fish', fontsize=20)
    plt.legend()
    # plt.show()
    # boxplot The lake with the largest median (50th percentile) fish.
    plt.boxplot(new_length)
    # plt.show()
    # scatter plot showing the length of the fish species
    plt.scatter(new_length, fish_Species)
    # plt.show()


readFile()
