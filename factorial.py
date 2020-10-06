

def main():
    num = int(input("enter a number: "))
    f = factorial(num)
    print("%r factorial is %d" % (num, f))

def factorial(num):
   if num == 1 or num == 0:
         return 1
   res = factorial(num-1) * num
   return res

main()
