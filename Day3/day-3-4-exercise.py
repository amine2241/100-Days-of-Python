# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n").lower()
name2 = input("What is their name? \n").lower()
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
T=name1.count("t")+name1.count("r")+name1.count("u")+name1.count("e")
T+=name2.count("t")+name2.count("r")+name2.count("u")+name2.count("e")
L=name1.count("l")+name1.count("o")+name1.count("v")+name1.count("e")
L+=name2.count("l")+name2.count("o")+name2.count("v")+name2.count("e")
TL=str(T)+str(L)
TL=int(TL)
if TL<10 or TL>90:
  print(f"Your score is {TL}%, you go together like coke and mentos.")
elif TL>=40 and TL<=50:
  print(f"Your score is {TL}%, you are alright together")
else:
  print(f"Your score is {TL}%")

