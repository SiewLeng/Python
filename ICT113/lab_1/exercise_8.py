"""
The formula to compute compound interest C for a loan L at the end of n
years at i % interest per annum is as follows:

C = L (1 + i / 100)^n

Write a program that has 3 inputs – loan amount, duration in years and
interest rate. The program displays the compound interest based on the
formula above.
"""

L = float(input("Enter loan amount ($): "))
i = float(input("Enter interest rate (%): "))
n = int (input("Enter duration of loan in years: "))

from math import pow

C = L * pow((1 + i / 100), n)

print(f"Compound interest ($): {C:.3f}")


