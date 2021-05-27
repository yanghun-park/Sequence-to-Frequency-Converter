import os.path

# 데이터
seqFile = "Sequence_Data//Output_Normal_new_1.csv" # 시퀀스 데이터 입력
freqFile = "frequency_Normal_1.csv" # 변환된 프리퀀시 데이터(출력)
freqDict = "frequency_Dict.txt" # 프리퀀시 사전

frequency_Dic = []
frequency_Result = []


def frequency_DictRead(filename):
    freqLine = 0

    if os.path.isfile(filename): # 만약 사전이 있다면
        dictFile = open(filename, 'r') # 추가모드로 열기

        while True:
            line = dictFile.readline()
            line = line.strip('\n')  # \n 제거
            frequency_Dic.append(line)
            freqLine += 1
            if not line: break

        dictFile.close();
        return freqLine

    else:
        dictFile = open(filename, 'w') # 새 파일로 열기
        dictFile.close()

    return 0;


def split_CSV(fileName, maxLen):
    dataNum = 0 # 데이터 갯수를 저장
    num = 0 # 데이터를 배열에 저장할때 사용하는 반복문용

    with open(fileName) as f: # 데이터 개수를 조사
        for line in f:
            dataNum += 1

    data = [[0 for i in range(maxLen)] for j in range(dataNum)] # 데이터를 저정할 리스트

    with open(fileName) as f: # 데이터를 리스트에 저장
        for line in f:
            line = line.strip('\n') # \n 제거
            data[num] = line.split(",")
            num += 1
            
    return data, dataNum


def frequency_Converter(fileName, maxLen):
    data, dataNum = split_CSV(fileName, maxLen) # 데이터를 나눔

    print("프리퀀시 사전 생성중...")
    for i in range(0, dataNum):
        print("프리퀀시 사전 생성중... - " + str(i) + "/" + str(dataNum))

        for j in range(1, maxLen):
            try:
                if (data[i][j] not in frequency_Dic): # 만약 프리퀀시 사전에 시퀀스가 없을경우
                    frequency_Dic.append(data[i][j]) # 프리퀀시 사전에 시퀀스 추가

            except IndexError: # 만약 배열 오류 발생시
                break # 반복문을 빠져나감


    # 최종 프리퀀시 만들기
    print("최종 프리퀀시 생성중...")
    for i in range(0, dataNum):
        line = data[i][0]  # 파일 이름 넣기
        print("프리퀀시 생성중... - " + str(i) + "/" + str(dataNum))

        for j in range(1, len(frequency_Dic)):

            if (frequency_Dic[j] in data[i]):
                line += ",1"
            else:
                line += ",0"

        frequency_Result.append(line)



def main():
    freqLine = frequency_DictRead(freqDict) # 사전데이터 불러오기
    frequency_Converter(seqFile, 800)

    outputFile = open(freqFile, 'w')

    for line in frequency_Result:
        outputFile.write(line);

    outputFile.close()

    print("시퀀스 개수 : ", len(frequency_Dic))
    print("사전데이터 기록중...")


    dictFile = open(freqDict, 'a') # 시퀀스 데이터를 추가모드로 열기
    for i in range(freqLine, len(frequency_Dic)):
        dictFile.write(frequency_Dic[i] + "\n")

    dictFile.close()


if __name__ == '__main__':
    main()

