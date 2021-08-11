import os.path
import webbrowser

from fpdf import FPDF
from filestack import Client

#An api key is needed from filestack for the FileSharer function: https://dev.filestack.com 

class PdfReport:
    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatmate1, flatmate2, bill):
        flatmate1_pay = str(round(flatmate1.pays(bill, flatmate2), 2))
        flatmate2_pay = str(round(flatmate2.pays(bill, flatmate1), 2))
        pdf = FPDF(unit='pt')
        pdf.add_page()
        #Add icon
        pdf.image("files/house.png", w=30, h=30)
        # Insert title
        pdf.set_font(family="Times", size=24, style="B")
        pdf.cell(w=0, h=80, txt="Flatmates Bill", align="C", ln=1)
        # Insert period label
        pdf.set_font("Times",size=14, style="B")
        pdf.cell(w=100, h=40, txt="Period")
        pdf.cell(w=150, h=40, txt=bill.period, ln=1)
        # Name and amt for flatmate 1
        pdf.set_font("Times", size=12)
        pdf.cell(w=100, h=25, txt=flatmate1.name)
        pdf.cell(w=150, h=25, txt="£" + flatmate1_pay, ln=1)
        # Name and amt for flatmate 2
        pdf.cell(w=100, h=25, txt=flatmate2.name)
        pdf.cell(w=150, h=25, txt="£" + flatmate2_pay, ln=1)
        #generate
        pdf.output(f"files/{self.filename}")
        webbrowser.open('file://' + os.path.realpath(f"files/{self.filename}"))

class FileSharer:
    #insert api file key below
    def __init__(self, filepath, api_key=""):
        self.filepath = filepath
        self.api_key = api_key

    def share(self):
        client = Client(self.api_key)
        new_filelink = (client.upload(filepath=self.filepath))
        return new_filelink.url

