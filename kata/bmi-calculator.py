height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

start = "\033[1m"
end = "\033[0;0m"

bmi = round(weight / height ** 2)
if bmi <18.5:
  print(f"Your BMI is {bmi}, you are {start}underweight{end}.")
elif bmi <25:
  print(f"Your BMI is {bmi}, you have a {start}normal weight{end}.")
elif bmi <30:
  print(f"Your BMI is {bmi}, you are {start}slightly overweight{end}.")
elif bmi <35:
  print(f"Your BMI is {bmi}, you are {start}obese{end}.")
else:
  print(f"Your BMI is {bmi}, you are {start}clinically obese{end}.")