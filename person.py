name = input("Your name:\n ") #???,???? ??????
age = input("Your age:\n ") #????????,???? ??????
height = input("Height:\n ") #????,???? ??????
pasw = input("Your password:\n") #??????(?? ??????),???? ??????
ncon = "Your name: " + name + "\n" #?????????? ??????? ????? ????????? ? ??????????? ?????? ? ????????? ????????  user.txt
acon = "Your age: " + age + "\n" #?? ?? ?????
hcon = "Your height: " + height + "\n"

file = open('users.txt','a',encoding='utf-8') #????????? ???? users.txt, ????? ??????, ????????? UTF-8
file.write("\n") #??????
file.write(ncon) #????? ??????????
file.write(acon) #????
file.write(hcon) #????
file.close() #?????????? ????????
