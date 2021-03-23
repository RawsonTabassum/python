UPTO_42707 = 15
UPTO_132406 = 25
UPTO_MORE = 28

salary = int(input())
if salary <= 15527:
    tax = 0
    rate = 0
elif salary <= 42707:
    tax = salary * (UPTO_42707 / 100)
    rate = UPTO_42707
elif salary <= 132406:
    tax = salary * (UPTO_132406 / 100)
    rate = UPTO_132406
elif salary > 132406:
    tax = salary * (UPTO_MORE / 100)
    rate = UPTO_MORE

print(f'The tax for {salary} is {rate}%. That is {tax:.0f} dollars!')