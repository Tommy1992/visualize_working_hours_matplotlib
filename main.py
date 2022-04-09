import matplotlib.pyplot as plt
import numpy

def getfile():
    f = open("d:\desktop\Arbeitszeiten.txt", "r")  # replace with own file directory
    lines = f.readlines()
    dates = []
    working_hours_per_day = []
    #print(lines)  # testing
    #print(type(lines))
    for each_line in lines:
        dates.append(each_line[:10])
        #each_line_10_plus = each_line[10:]
        #print(dates) #testing
        if each_line[-4] is int:                # it's string of course...!?????????????????!!!??!?!?!?!?!?
            working_hours_per_day.append(each_line[-3])
            print(working_hours_per_day)
    f.close()  # put this line after being done with the original fil e, else the program might crash

    plt.xlim(0, 20)
    counter = 0
    for element in working_hours_per_day:
        counter += 1
        print(f"{counter}. Zeile: {element}")
    #working_hours_per_day = working_hours_per_day.encode("ascii")
    #plt.barh(dates, int(working_hours_per_day))

   # plt.plot(dates, working_hours_per_day)
    plt.ylabel('working_hours_per_day')
    plt.show()


if __name__ == '__main__':
    getfile()

