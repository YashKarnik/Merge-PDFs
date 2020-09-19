import glob
import datetime
import re
import time
import os
try:
    import PyPDF2
except Exception as e:
    inp = input("PyPDF2 module not found!!Do you want to install it? [y/n]: ")
    if(inp == 'y' or inp == 'Y'):
        os.system('pip install PyPDF2')
        print("Module Insatlled!!")
        time.sleep(0.5)
    else:
        print("Goodbye...")
        time.sleep(1)
        exit()


def GetResultantFilename(s):
    temp = s[:]
    num = 1
    while(os.path.isfile(os.getcwd()+"/../MERGED DOCS HERE/"+temp+".pdf")):
        temp = s[:]
        temp += "[{}]".format(num)
        num += 1
    return temp+".pdf"


def mergePDF(filesArr, result_filename):
    pdfFileObjArray = []
    for i in filesArr:
        pdfFileObj = PyPDF2.PdfFileReader(open(i, "rb"))
        pdfFileObjArray.append(pdfFileObj)
    pdfWriter = PyPDF2.PdfFileWriter()
    for i in pdfFileObjArray:
        for j in range(i.numPages):
            pdfWriter.addPage(i.getPage(j))
    try:
        os.mkdir(os.getcwd()+"/../MERGED DOCS HERE")
    except FileExistsError as e:
        pass
    pdfOutputFile = open("../MERGED DOCS HERE/"+result_filename, 'wb')
    pdfWriter.write(pdfOutputFile)
    pdfOutputFile.close()
    return result_filename


def main():
    PdfArr = glob.glob('../DROP/*.pdf')
    print("{} Files found!!".format(len(PdfArr)))
    if(len(PdfArr) == 0):
        print("Please drop files in the drop Folder!!")
        exit()
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
    result_filename = input(
        "Enter name of Merged dopcument:").replace(" ", "-")
    temp = mergePDF(temp, GetResultantFilename(result_filename))
    print("DONE!!...{} created in MERGED DOCS FOLDER".format(temp))
    time.sleep(1.5)
    print("Goodbye..")
    time.sleep(2)


if __name__ == "__main__":
    main()
