import PyPDF2
import glob
import datetime
import time


def mergePDF(filesArr, result_filename):
    pdfFileObjArray = []
    for i in filesArr:
        pdfFileObj = PyPDF2.PdfFileReader(open(i, "rb"))
        pdfFileObjArray.append(pdfFileObj)
    pdfWriter = PyPDF2.PdfFileWriter()
    for i in pdfFileObjArray:
        for j in range(i.numPages):
            pdfWriter.addPage(i.getPage(j))
    pdfOutputFile = open("../MERGED DOCS HERE/"+result_filename, 'wb')
    pdfWriter.write(pdfOutputFile)
    pdfOutputFile.close()


if __name__ == "__main__":
    PdfArr = glob.glob('../DROP/*.pdf')
    print("{} Files found!!".format(len(PdfArr)))
    x = {}
    for i in range(len(PdfArr)):
        x[chr(i+97)] = PdfArr[i]
    for i, j in x.items():
        print(i, ":", j.split("\\")[1])
    temp = []
    y = input(
        "Enter letters of files to merge in required order(space seperated):").lower().split()
    for i in y:
        temp.append(x.get(i))
    inp = input("Enter name of Merged dopcument:").replace(" ", "-")
    result_filename = inp+".pdf"
    mergePDF(temp, result_filename)
    print("DONE!..Merged Document is in \'MERGED DOCS FOLDER\'.")
    time.sleep(5)
    print("Goodbye..")
