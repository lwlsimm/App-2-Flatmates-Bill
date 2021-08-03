from flat import Bill, Flatmate
from report import PdfReport

amount = float(input("Hey user, enter the bill amount: "))
period = input("Input the period of the bill: ")
flatmate_a_name = input("Input the name of the first flatmate: ")
flatmate_a_days = int(input(f"Input the number of days in the period that {flatmate_a_name} occupied the house: "))
flatmate_b_name = input("Input the name of the second flatmate: ")
flatmate_b_days = int(input(f"Input the number of days in the period that {flatmate_b_name} occupied the house: "))

the_bill = Bill(amount, period)
flatmate_a = Flatmate(flatmate_a_name, flatmate_a_days)
flatmate_b = Flatmate(flatmate_b_name, flatmate_b_days)

flatmate_a.pays(the_bill, flatmate_b)
flatmate_b.pays(the_bill, flatmate_a)
pdf_report = PdfReport(filename=f"{period}.pdf")
pdf_report.generate(flatmate_a,flatmate_b,the_bill)