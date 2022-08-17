"""
Written by: Daniel Woodson
8/17/2022

Enter start and finish numbers and this will create a pdf with "BM" pallet numbers in that range
"""
from fpdf import FPDF
import os
import tkinter as tk
from tkinter import filedialog

path = ''
start = 0
stop = 1


def get_dir():
    global path
    path = filedialog.askdirectory()
    file_location_entry.insert(0, path)
    return


def create_pdf():
    start = int(start_entry.get())
    stop = int(stop_entry.get())
    root.update_idletasks()
    global path
    print(start, stop)

    pdf = FPDF('L', 'in', 'Letter')
    pdf.set_font('Arial', 'B', size=150)
    pdf.set_margins(0, 0.5)
    for i in range(start, stop + 1):
        pdf.add_page()
        string = 'BM - ' + str(i)
        pdf.cell(10, 7.125 / 2, string, ln=1, align='C')
        pdf.cell(10, 7.125 / 2, string, ln=1, align='C')
    file_name = path + '/BM_Pallets ' + str(start) + '-' + str(stop) + '.pdf'
    print(file_name)
    pdf.output(file_name, 'F')


if __name__ == '__main__':
    n = 0
    root = tk.Tk()
    root.geometry('325x200')
    root.title('Bay Materials Pallet Labels')
    tk.Label(root, text="1. Enter a start and stop \"BM\" number \n"
                        "2. Select a file location to store the file\n"
                        "3. Open the pdf, verify it's correct and print\n", justify='left').grid(row=n, columnspan=2)
    n += 1

    tk.Label(root, text="Start Number", justify='left').grid(row=n)
    start_entry = tk.Entry(root)
    start_entry.insert(0, "0")
    start_entry.grid(row=n, column=1)
    n += 1

    tk.Label(root, text="Stop Number", justify='left').grid(row=n)
    stop_entry = tk.Entry(root)
    stop_entry.insert(0, "0")
    stop_entry.grid(row=n, column=1)
    n += 1

    tk.Label(root, text="File location:", justify='left').grid(row=n)
    n += 1

    file_location_entry = tk.Entry(root, justify='left')
    file_location_entry.grid(row=n)
    n += 1

    tk.Button(root, text="Select Folder", command=get_dir).grid(row=n)
    n += 1

    root.update_idletasks()
    tk.Button(root, text="Create PDF", command=create_pdf).grid(row=n)

    root.mainloop()
