def menu():
    print("[1] option 1")
    print("[2] option 2")
    print("[0] exit the pgm")
menu()
option=int(input("enter your option:"))
while option!=0:
 if option==1:
  print("option 1 has been called:")
 elif option==2:
  print("option2 has been called:")
 else:
  print("invalid option")
 print()
 menu()
 option=int(input("enter your option:"))
 print("thanks for using this pgm.bye")
