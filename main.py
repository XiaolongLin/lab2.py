temp = input("Enter temperature: ")
unit = input ("Enter unit in F/f or C/c: ")
temp = float(temp)
if unit == "F" or "f":
  c = (temp-32)/1.8
  print(str(temp)+"° in Fahrenheit is equivalent to "+str(c)+"° Celsius.")
elif unit == "C" or "c":
  f = temp*1.8+32
  print(str(temp)+"° in Celsius is equivalent to" +str(f)+"° Fahrenheit.")
else:
  bad = unit
  print(f"Invalid unit(bad).") 
      

 