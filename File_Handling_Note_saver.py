import os         # module of the make connection with the device os
import webbrowser
#  Use the Documents folder
folder_path = os.path.expanduser("~/Documents/Sample")

# List to store (file name, full path)
pdf_files = []

#   Find all PDF files
for root, dirs, files in os.walk(folder_path):# open   main path Documents
    for file in files: # open the one by one file
        if file.lower().endswith(".pdf"):
            full_path = os.path.join(root, file)
            name = os.path.splitext(file)[0]
            pdf_files.append((name, full_path))

#   Show the list of PDFs
if not pdf_files:
    print("No PDF files found .")
else:
    print(" -----------------------------------PDF Files  in Sample Folder-----------------------------------\n")
    for i, (name,_) in enumerate(pdf_files, start=1):
        print(f"\t\t\t {i}. {name}")

    # User selects one to open
    while True:
        choice = input("\nEnter PDF number to open (or exit to enter 'exit' ): ")
        if choice.lower() == 'exit':
            break
        if choice.isdigit():
            index = int(choice) - 1
            if 0 <= index < len(pdf_files):
                print(f"\n Open file: {pdf_files[index][0]}")
                webbrowser.open(pdf_files[index][1])
            else:
                print(" Invalid number.")
        else:
            print(" Please enter a number or 'exit'.\n")

''' 

 -----------------------------------PDF Files  in Sample Folder-----------------------------------

			 1. Sample File 01
			 2. Sample File 02
			 3. Sample File 03

Enter PDF number to open (or exit to enter 'exit' ): 1

 Open file: Sample File 01

Enter PDF number to open (or exit to enter 'exit' ): exit

Process finished with exit code 0

'''
