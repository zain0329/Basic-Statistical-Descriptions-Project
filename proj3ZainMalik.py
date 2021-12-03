# Programming project 3 - Zain Malik
#import statistics module
import statistics
# print statements that state purpose of this program
print("This program will compute basic statistical descriptions of the following data:")
values = [13, 15, 16, 16, 19, 20, 20, 21, 22, 22, 25, 25, 25, 25, 30, 33, 33, 35, 35, 35, 35, 36, 40,
45, 46, 52, 70. ]

# set variables
mean = statistics.mean(values)
median = statistics.median(values)
mode = statistics.mode(values)
modality = statistics.multimode(values)
midrange = (min(values) + max(values)) /2
variance = statistics.variance(values)
standard = statistics.stdev(values)
quartile = statistics.quantiles(values, n=4)

# print statement that shows result
print()
print(values)
print()
print("The mean is ",format((mean), '.2f'))
print("The median is ", median)
print("The mode is ", mode)
print(modality, "This data is bimodal")
print("The midrange is ", midrange)
print("The variance is ",format((variance), '.2f'))
print("The Standard deviation is ",format((standard), '.2f'))
print("The first, second, and third quartiles are:", quartile)
print("The five number summary of the data is:", min(values), quartile, max(values))
