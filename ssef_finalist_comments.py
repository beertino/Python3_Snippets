from csv import reader
import pdfplumber           #pdfplumber reads text from pdf better than PyPDF2
import PyPDF2               #Need PyPDF2 to append PDF page objects

# read csv file as a list of lists to extract the successful projects, 
with open('success.csv', 'r') as read_obj:
    # pass the file object to reader() to get the reader object
    csv_reader = reader(read_obj)
    # Pass reader object to list() to get a list of lists
    finalist = list(csv_reader)[0]
    # I needed to update the first entry as it was a strange 'ï»¿BE001' initially
    finalist[0]='BE001'             

# Put the Judges Comments pdf from SSEF in the same folder as the script
SSEF_filename=["From SSEF/2020_NJC_JudgesComments_PartOne.pdf","From SSEF/2020_NJC_JudgesComments_PartTwo.pdf"]

for raw_file in SSEF_filename:
    pdf = PyPDF2.PdfFileReader(open(raw_file,'rb'))
    num_page= pdf.getNumPages()
    pdf = pdfplumber.open(raw_file)

    finalist_page=[]
    #The two loops below extract the page numbers in each pdf that contains the finalists
    for f in finalist:
        for i in range(0,num_page):
            page = pdf.pages[i]
            text = page.extract_text()
            if f in text:
                finalist_page.append(i)
    pdf.close()
    pdf_writer = PyPDF2.PdfFileWriter()

    object= PyPDF2.PdfFileReader(raw_file)

    for i in finalist_page:
        pdf_writer.addPage(object.getPage(i))

    with open(raw_file[10:],'wb') as out:
        pdf_writer.write(out)

print('Done Processing!')
