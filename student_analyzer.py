n = int(input("Enter the number of students: "))
marks = []
i = 0
while(i<n):
    mark = int(input(f"Enter the marks of student {i+1}: "))
    marks.append(mark)
    i +=1
print()
print(marks)
print()
#to find the topper
topper = max(marks)
print("the topper is: ",topper)
print()
#avg
avg =sum(marks)/n
print("the avg marks: ", avg)
print()
#failed students
failed = []
for m in marks:
    if(m<40):
        failed.append(m)
print("the failed students are: ",failed)
print()
print(sorted(marks,reverse=True))
