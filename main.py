import webbrowser

from fpdf import FPDF


class Bill:
    """
    Object contains data of bill such as total amount and period of bill
    """

    def __init__(self, amount, period):
        self.amount = amount
        self.period = period


class Flatmate:
    """Create a flatmate person who lives in the
    flat and pays a share of the bill"""

    def __init__(self, name, days_in_house):
        self.days_in_house = days_in_house
        self.name = name

    def pay(self, bill, flatmate2):
        weight = self.days_in_house / (self.days_in_house + flatmate2.days_in_house)
        to_pay = bill.amount * weight
        return to_pay


class PdfReport:
    """Create a Pdf file that contains data about the flatmates:
    their names, due amount, period of the bill"""

    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatmate1, flatmate2, bill):
        flatmate1_pay = str(round(flatmate1.pay(bill, flatmate2), 2))
        flatmate2_pay = str(round(flatmate2.pay(bill, flatmate1), 2))

        pdf = FPDF(orientation='P', unit='pt', format='A4')
        pdf.add_page()

        # Add Icon
        pdf.image(name="house.png", w=30, h=30)

        # Add the title
        pdf.set_font(family='Times', size=24, style='B')
        pdf.cell(w=0, h=80, txt="Roommate Bill", border=1, align="C", ln=1)

        # Insert period label and value
        pdf.cell(w=100, h=40, txt="Period:", border=1)
        pdf.cell(w=150, h=40, txt=bill.period, border=1, ln=1)

        # Insert name and due amount of the first flatmate
        pdf.cell(w=100, h=40, txt=flatmate1.name, border=1)
        pdf.cell(w=150, h=40, txt=flatmate1_pay, border=1, ln=1)

        # Insert name and due amount of the second flatmate
        pdf.cell(w=100, h=40, txt=flatmate2.name, border=1)
        pdf.cell(w=150, h=40, txt=flatmate2_pay, border=1, ln=1)

        pdf.output("bill.pdf")

        webbrowser.open(self.filename)


amount = float(input("Hey user, enter the bill amount: "))
print("This is a", amount)
period = input("what is the bill period? E.g. December 2021")
name1 = input("What is your name? ")
days_in_house1 = int(input("how many days did {name1} stay in the house during the bill period? "))
name2 = input("What is name of other flatmate?  ")
days_in_house2 = int(input("how many days did {name2} stay in the house during the bill period? "))

the_bill = Bill(amount=a, period="March 2021")
flatmate1 = Flatmate(name1, days_in_house1)
flatmate2 = Flatmate(name2, days_in_house2)

print(f"{name1} pays: ", flatmate1.pay(the_bill, flatmate2))
print(f"{name2} pays: ", flatmate2.pay(the_bill, flatmate2))

pdf_report = PdfReport(filename="Report1.pdf")
pdf_report.generate(flatmate1, flatmate2, bill=the_bill)
