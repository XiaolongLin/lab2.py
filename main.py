
def sum_n(n):
  if n<=0:
    return 0;
  else:
    sum = n + sum_n(n-1)
    return sum
def print_n(s,n):
  if n==0:
    return 0
  else:
    print(s)
    print_n(s,n-1)

def run():
  num = int(input("Enter an int: "))
  print(f"sum is {sum_n(num)}.")
  sen = input("Enter a string: ")
  print_n(sen,num)

if __name__ == "__main__":
  run() 
      

 