import os.path

# Data Setup
seqFile = "Sequence_Data//Output_Normal_new_1.csv" # Input Sequence Data
freqFile = "frequency_Normal_1.csv" # Output Frequency Data
freqDict = "frequency_Dict.txt" # Frequency Dictionary

frequency_Dic = []
frequency_Result = []


def frequency_DictRead(filename):
    freqLine = 0

    if os.path.isfile(filename): # If there is a dictionary,
        dictFile = open(filename, 'r') # Open in Additional Mode

        while True:
            line = dictFile.readline()
            line = line.strip('\n')  # \n Remove
            frequency_Dic.append(line)
            freqLine += 1
            if not line: break

        dictFile.close();
        return freqLine

    else:
        dictFile = open(filename, 'w') # Open as New File
        dictFile.close()

    return 0;


def split_CSV(fileName, maxLen):
    dataNum = 0 # Store the number of data
    num = 0

    with open(fileName) as f: # Examine the number of data
        for line in f:
            dataNum += 1

    data = [[0 for i in range(maxLen)] for j in range(dataNum)] # List to save data to

    with open(fileName) as f: # Save Data to List
        for line in f:
            line = line.strip('\n') # \n Remove
            data[num] = line.split(",")
            num += 1
            
    return data, dataNum


def frequency_Converter(fileName, maxLen):
    data, dataNum = split_CSV(fileName, maxLen) # Divide data

    print("Creating frequency dictionary...")
    for i in range(0, dataNum):
        print("Creating frequency dictionary... - " + str(i) + "/" + str(dataNum))

        for j in range(1, maxLen):
            try:
                if (data[i][j] not in frequency_Dic): # If there is no sequence in the prequence dictionary,
                    frequency_Dic.append(data[i][j]) # Add Sequence to Prequency Dictionary

            except IndexError: # If an array error
                break


    # Create Final Prequence
    print("Creating Finial frequency...")
    for i in range(0, dataNum):
        line = data[i][0]  # Insert File Name
        print("Creating Frequency... - " + str(i) + "/" + str(dataNum))

        for j in range(1, len(frequency_Dic)):

            if (frequency_Dic[j] in data[i]):
                line += ",1"
            else:
                line += ",0"

        frequency_Result.append(line)



def main():
    freqLine = frequency_DictRead(freqDict) # Recall dictionary data
    frequency_Converter(seqFile, 800)

    outputFile = open(freqFile, 'w')

    for line in frequency_Result:
        outputFile.write(line);

    outputFile.close()

    print("Sequence Count : ", len(frequency_Dic))
    print("Recording dictionary data...")


    dictFile = open(freqDict, 'a') # Record to Sequence Data
    for i in range(freqLine, len(frequency_Dic)):
        dictFile.write(frequency_Dic[i] + "\n")

    dictFile.close()


if __name__ == '__main__':
    main()

