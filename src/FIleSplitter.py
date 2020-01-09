import os

SINGLE_FILE_LENGTH = 8100
TOTAL_FILE_LENGTH = 810000


def get_file_relative_path(directory_path, file_name, file_suffix, file_extension):
    return directory_path + file_name + str(file_suffix) + file_extension


originData = open("../data/train.csv", "r")


dataDirectory = "../data/"
trainSetFileName = "train_"
trainSetExtension = ".csv"

for trainSetSuffix in range(1, TOTAL_FILE_LENGTH // SINGLE_FILE_LENGTH + 1):
    trainSetFilePath = get_file_relative_path(dataDirectory, trainSetFileName, trainSetSuffix, trainSetExtension)
    if not os.path.isfile(trainSetFilePath):
        f = open(trainSetFilePath, "w")
        f.close()

    f = open(trainSetFilePath, "a")

    lineCount = 0
    for line in originData:
        f.write(line)
        lineCount += 1

        if lineCount % SINGLE_FILE_LENGTH == 0:
            f.close()
            break

originData.close()