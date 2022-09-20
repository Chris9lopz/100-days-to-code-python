# Instructions
"""
You are going to write a program that calculates the average student height from a List of heights.

Important You should not use the sum() or len() functions in your answer. You should try to replicate 

their functionality using what you have learnt about for loops.
"""

# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
sum = 0
count = 0
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆
#Write your code below this row 👇
  sum += student_heights[n]
  count += 1

total = round(sum / count)
print(total)
