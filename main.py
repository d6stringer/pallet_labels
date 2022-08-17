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
    if start > stop:
       start, stop = stop, start
    root.update_idletasks()
    global path
    pdf = FPDF('L', 'in', 'Letter')
    pdf.set_font('Arial', 'B', size=150)
    pdf.set_margins(0, 0.5)
    for i in range(start, stop + 1):
        pdf.add_page()
        string = 'BM - ' + str(i)
        pdf.cell(10, 7.125 / 2, string, ln=1, align='C')
        pdf.cell(10, 7.125 / 2, string, ln=1, align='C')
    file_name = path + '/BM_Pallets ' + str(start) + '-' + str(stop) + '.pdf'
    pdf.output(file_name, 'F')


if __name__ == '__main__':
    n = 0
    root = tk.Tk()
    # root.geometry('325x200')
    root.title('Bay Materials Pallet Labels')
    frame = tk.Frame(root, relief='sunken')
    frame.pack(fill='both', expand=True, padx=10, pady=10)
    tk.Label(frame, text="1. Enter a start and stop \"BM\" number \n"
                        "2. Select a file location to store the file\n"
                        "3. Open the pdf, verify it's correct and print\n", justify='left').grid(row=n, columnspan=2, sticky='w')
    n += 1

    tk.Label(frame, text="Start Number").grid(row=n, sticky='w')
    start_entry = tk.Entry(frame)
    start_entry.insert(0, "0")
    start_entry.grid(row=n, column=1, sticky='e')
    n += 1

    tk.Label(frame, text="Stop Number", justify='left').grid(row=n, sticky='w')
    stop_entry = tk.Entry(frame)
    stop_entry.insert(0, "0")
    stop_entry.grid(row=n, column=1, sticky='e')
    n += 1

    tk.Label(frame, text="File location:", justify='left').grid(row=n, sticky='w')
    n += 1

    file_location_entry = tk.Entry(frame, justify='left', width=38)
    file_location_entry.grid(row=n, columnspan=2, sticky='w')
    n += 1

    tk.Button(frame, text="Select Folder", command=get_dir).grid(row=n, sticky='w')
    n += 1

    root.update_idletasks()
    tk.Button(frame, text="Create PDF", command=create_pdf).grid(row=n, sticky='w')

    root.mainloop()
