# 🚨 Don't change the code below 👇
row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

horizontal = int(position[0])
vertical = int(position[1])

if horizontal == 1:
    if vertical == 1:
        map[0][0] = 'X'
    elif vertical == 2:
        map[1][0] = 'X'
    elif vertical == 3:
        map[2][0] = 'X'
elif horizontal == 2:
    if vertical == 1:
        map[0][1] = 'X'
    elif vertical == 2:
        map[1][1] = 'X'
    elif vertical == 3:
        map[2][1] = 'X'
elif horizontal == 3:
    if vertical == 1:
        map[0][2] = 'X'
    elif vertical == 2:
        map[1][2] = 'X'
    elif vertical == 3:
        map[2][2] = 'X'

#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")