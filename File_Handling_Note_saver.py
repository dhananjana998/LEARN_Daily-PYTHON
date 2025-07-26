import os         # module of the make connection with the device os
import webbrowser
#  Use the Documents folder
folder_path = os.path.expanduser("~/Documents")

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
    print(" PDF Files  in Downloads:")
    for i, (name,_) in enumerate(pdf_files, start=1):
        print(f"{i}. {name}")

    # User selects one to open
    while True:
        choice = input("\nEnter PDF number to open (or exit to enter 'exit' ): ")
        if choice.lower() == 'exit':
            break
        if choice.isdigit():
            index = int(choice) - 1
            if 0 <= index < len(pdf_files):
                print(f"Open file: {pdf_files[index][0]}")
                webbrowser.open(pdf_files[index][1])
            else:
                print(" Invalid number.")
        else:
            print(" Please enter a number or 'exit'.")

'''     out put
 PDF Files  in Downloads:
1. 10.2478_bjreecm-2023-0015
2. 2020-2021 EEI4366-EEX4366
3. 222513158_EEI4366_TMA2
4. 222513158_MHZ3459
5. 46-T15091
6. 47-S15110
7. BookDao
8. Current status of construction contractors in time of crisis and implications on economy _ Daily FT
9. Grade 9 evaluation[1]anex
10. L5 WD_protected
11. LargeScaleContractors_KandyConference_14th
12. MHZ4256
13. MSME-Presentation-English
14. MSMEs_Report (1).pdf (1).crdownload
15. oop QA Note
16. S22009883
17. S22009883_4369Lab1
18. S22009883_4369Lab4
19. S22009883_EEI4369_First_Progress_Review
20. s22009883_Miniproject_4465
21. SRI LANKA One million Sri Lankan construction workers have lost their jobs
22. todaypri2
23. volume-2-online-333-343 (4)
24. x
25. 222513158_MP
26. GUIslice_ref
27. 222513158_EEI4366_TMA2

Enter PDF number to open (or exit to enter 'exit' ): 3
Opening: 222513158_EEI4366_TMA2

Enter PDF number to open (or exit to enter 'exit' ): '''
