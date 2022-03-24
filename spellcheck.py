# Spell Check Starter
# This start code creates two lists
# 1: dictionary: a list containing all of the words from "dictionary.txt"
# 2: aliceWords: a list containing all of the words from "AliceInWonderland.txt"

import re  # Needed for splitting text with a regular expression
import time
# Binary search function
def binarySearch(aList, item):
    loindex = 0
    hiindex = len(aList) - 1

    while hiindex >= loindex:
        midindex = (hiindex + loindex) // 2 
        if item == aList[midindex]:
            return midindex
        elif item < aList[midindex]:
            hiindex = midindex - 1
        else:
            loindex = midindex + 1   
    return -1

    
# Linear search function
def linearSearch(aList, item):
    for i in range(len(aList)):
        if aList[i] == item:
            return i
    return -1

def main():

    # Load data files into lists
    dictionary = loadWordsFromFile("data-files/dictionary.txt")
    aliceWords = loadWordsFromFile("data-files/AliceInWonderLand.txt")

    # Print first 50 values of each list to verify contents
    print(dictionary[0:50])
    print(aliceWords[0:50])
    loop = True
    while loop:
        print("\nMain Menu")
        print("1. Spell Check a Word (Linear Search)")
        print("2. Spell Check a Word (Binary Search)")
        print("3. Spell Check Alice in Wonderland (Linear Search)")
        print("4. Spell Check Alice in Wonderland (Binary Search)")
        print("5. Exit")
        opt = input("Please Enter Your Menu Selection: ")
        if opt == "1":
            linitem = input("Please enter a word you want to spell check: ").lower()
            start = time.time()
            index = linearSearch(dictionary, linitem)
            if index == -1:
                end = time.time()
                print(f"\n{linitem} is NOT in the dictionary. ({end - start} seconds)")
            else:
                end = time.time()
                print(f"\n{linitem} is IN the dictionary at postion {index}. ({end - start} seconds)")   
        elif opt == "2":
            binitem = input("Please enter a word you want to spell check: ").lower()
            start = time.time()
            index = binarySearch(dictionary, binitem)
            if index == -1:
                end = time.time()
                print(f"\n{binitem} is NOT in the dictionary. ({end - start} seconds)")
            else:
                end = time.time()
                print(f"\n{binitem} is IN the dictionary at position {index} ({end - start} seconds)")
        elif opt == "3":
            count = 0
            start = time.time()
            for word in aliceWords:
                index = linearSearch(dictionary, word.lower())
                if index == -1:
                    count += 1
            end = time.time()
            print(f"Number of words not found in dictionary: {count} ({end - start} seconds)")
        elif opt == "4":
            count = 0
            start = time.time()
            for word in aliceWords:
                index = binarySearch(dictionary, word.lower())
                if index == -1:
                    count += 1
            end = time.time()
            print(f"Number of words not found in dictionary: {count} ({end - start} seconds)")
        elif opt == "5":
            loop = False
# end main()


def loadWordsFromFile(fileName):
    # Read file as a string
    fileref = open(fileName, "r")
    textData = fileref.read()
    fileref.close()

    # Split text by one or more whitespace characters
    return re.split('\s+', textData)
# end loadWordsFromFile()


# Call main() to begin program
main()
