n=int(input("Enter a positive integer: "))
sum_even = 0
if n > 0:
 for i in range(1, n + 1):
    if i % 2 == 0:
        sum_even += i        
 print(f"The sum of even numbers between 1 and {n} is {sum_even}.")
else: 
   print("wrong")
