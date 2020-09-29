

print("\t\t\t.........WELCOME TO THE GRADE AVERAGE POINT CALCULATOR........")
name= input("Please enter your name: ")
num_of_grades = int(input("Please enter number of grades available: "))

grades_list= []

for num in range(num_of_grades):
    grades = int(input("please provide the grades: "))
    grades_list.append(grades)

grades_list.sort(reverse=True)

#avergage algorithm
def avarage():
    avg= float(sum(grades_list)/ len(grades_list))
    return avg

print("\n\nGrades Highest to Lowest: ", *grades_list,sep= "\n")

print(f"{name.title()}'s Grade Summary: \n Total Number of Grades: {num_of_grades}")
print("Highest Grade:",grades_list[0])
print("Lowest Grade:",grades_list[-1])
print("Average:", avarage())

desired_avg = float(input("\n\nWhat is your desired average:"))
print(f"Goodluck {name.title()}!")
print(f"To earn {desired_avg} ,you need to get {0}")





'''
example = 4
num= 0
list= [2,4,567,89]
for num in range(example):
    print(list[num])
    num+=1
'''

