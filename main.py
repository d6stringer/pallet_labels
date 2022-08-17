"""
Written by: Daniel Woodson
8/17/2022

Enter start and finish numbers and this will create a pdf with "BM" pallet numbers in that range
"""
from fpdf import FPDF


if __name__ == '__main__':
   pdf = FPDF()
   pdf.add_page(orientation='L', format='letter')
   pdf.set_font('Arial', 72)
   # cell size in mm
   #8.5" x 11" is 215.9mm x 279.4
   #This cell is 280 wide, 108 tall, has some text, line break, and centered
   pdf.cell(280, 216/2, 'BM - 1234', ln=1, 'C')
   pdf.cell(280, 216 / 2, 'BM - 1235', ln=1, 'C')
   pdf.output('BM_Pallets 1234-1235.pdf', 'F')