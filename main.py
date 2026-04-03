marks=[]
num_of_sub= int(input("How many subjects? "))
for i in range(num_of_sub):
m=int(input("you marks: "))
marks.append(m)
a=sum(marks)
avg=a/num_of_sub
print("your average is ", avg)
print("your best mark is",max(marks) )
print("your lowest score is:", min(marks))
if avg>=90:
print("Excellent ")
elif avg>=75:
print("good")
elif avg>=50:
print("need improvement ")
else:
print("very poor")
