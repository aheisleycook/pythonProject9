# This is a sample Python script.
import re


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
def loadfile(file):
    """:argument
    :return string
    """
    a = open(file)
    content = a.readlines()
    return content


def main():
    score = open("scores.txt","a")
    total = 0
    a = loadfile("test.txt")
    name = a[0]
    print(name)
    score.write("name: {0}".format(name))
    for b in a[1:]:
        print("score: {0}".format(b))
        score.write("score: {0}".format(b))
        total += int(b)

    print(total)
    score.write("total: {0}".format(b))
    average = (total/len(b))
    score.write("average: {0}".format(average))
    print(average)
    score.close()

main()
