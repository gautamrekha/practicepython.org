input_number = input("Enter the number you wanna check-out \n")
input_number_2 = input("Enter the number you wanna divide \n")
if (int(input_number_2) % int(input_number)) ==0:
    print("divisible")
mod = int(input_number) % 2
if int(input_number) % 4 ==0:
    print("can be divided 4")
elif mod == 0:
    print("Yes that's an even number")
else:
  print("That's an odd number")
