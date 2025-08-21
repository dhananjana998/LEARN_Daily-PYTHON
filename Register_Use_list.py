Name = ["D.G.S.S.Dhananjana", "I.E.prasad", "D.G.M.Nimsarani"]
S_num = [2514, 2515, 2516]
Daily_Register = []

i = 0
present = 0
absence = 0

while i < len(Name):
    In_class = input(f"Is student {Name[i]} in class (yes/no)? ")
    if In_class.lower() == "yes":
        Daily_Register.append(f"{Name[i]} : {S_num[i]} : 1")
        present += 1
    else:
        Daily_Register.append(f"{Name[i]}  : {S_num[i]} : 0")
        absence += 1
    i += 1

print("\nDaily Register:")
for record in Daily_Register:
    print(record)

print(f"\nPresent students: {present}")
print(f"Absent students: {absence}")

'''Is student D.G.S.S.Dhananjana in class (yes/no)? yes
Is student I.E.prasad in class (yes/no)? no
Is student D.G.M.Nimsarani in class (yes/no)? yes

Daily Register:
D.G.S.S.Dhananjana : 2514 : 1
I.E.prasad : 2515 : 0
D.G.M.Nimsarani : 2516 : 1

Present students: 2
Absent students: 1
'''
