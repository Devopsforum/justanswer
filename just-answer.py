import dictionary as dictionary
import row as row
def main():
 # display brief description of program
 print("This program will produce reports that display")
 print("Day, Daily Sales, Number Sold, and Average Sales")
 print("based on their data from their businesses.")
 print()
 # prompt user for file name to analyze
 dataFile = input("Enter file name to analyze: ")
 print()
 print("{0:^45}".format("Data analysis for file:",dataFile))
 print()
 # create a dictionary
 dictionary = dict("Monday",10927,276,
"Tuesday",12570,268,
"Wednesday",10765,258,
"Thursday",11995,191,
"Friday",10288,285)
 totalsDictionary = dict()
 # open, read, close data
 file = open(dataFile,'r')
 data = file.read()
 file.close()
 # split the information
 dataList = data.split("\n")
 # for loop to go through all the lines
 for line in dataList:
     try:
      row = line.split(',')
     except:
         continue
 # make key
 key = row[0]
 # calculate average sales
 average = (int(row[1])//int(row[2]))
 # create tuple
 value = (row[1],row[2],average)
 # add dictionary key and value with rest of data
 dictionary[key] = value
border = ("==================================================")
print(border)
print("{0:<12}{1:>12}{2:>14}{3:>12}".format("Day", "Daily Sales", "Number Sold", "Avg.Sale"))
print(border)
for day in dictionary:
 print("{0:<12}{1:>12}{2:>14}{3:>12}".format(day,*dictionary[day]))
 dailySales = dictionary[day:row[1]]
print(border)
# run it
main()
