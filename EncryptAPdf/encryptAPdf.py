from PyPDF2 import PdfFileWriter, PdfFileReader


def encryption(inputPdf, outputPdf, password):

    print("\n\t_________Encryption function started!___________")
    pdf_writer = PdfFileWriter() #Use for write pdf pages
    pdf_reader = PdfFileReader(inputPdf) #Initialize pdf file reader object

    docInformation = pdf_reader.documentInfo # property for get the details about the pdf

    print("\nNumber of pages : "+str(pdf_reader.numPages))
    print("File name : "+docInformation.title)
    print("Is encrypted: "+str(pdf_reader.isEncrypted))

    for page in range(pdf_reader.getNumPages()):
        pdf_writer.addPage(pdf_reader.getPage(page)) #loop through the pages and add the page to new pdf file (creating one)

    pdf_writer.encrypt(user_pwd=password,owner_pwd=None,use_128bit=True) #Encrypt the created pdf file 

    with open(outputPdf, 'wb') as fh:
        pdf_writer.write(fh) # output the added pages as a single pdf file
    
    print("\nEncrypted copy of the file generated successfully. Must use the password to open it.")


def decryptAPdf(encryptedPdf,outputPdf, password):

    print("\n\t_________Decryption function started.(Remove the password verification to open the file)__________")

    pdf_reader = PdfFileReader(encryptedPdf)
    pdf_writer = PdfFileWriter()

    pdf_reader.decrypt(password = "mahela") #Decrypt the file

    print("\nNumber of pages: "+str(pdf_reader.numPages))
    print("Is Encrypted : "+str(pdf_reader.isEncrypted))

    for page in range(pdf_reader.getNumPages()):
        pdf_writer.addPage(pdf_reader.getPage(page))

    with open(outputPdf,"wb") as fh:
        pdf_writer.write(fh)

    print("\nDecrypted copy of the file generated successfully.")


encryption("resumeSamples.pdf","encryptedPdf.pdf","mahela") #should give a password
decryptAPdf("encryptedPdf.pdf","decrypted.pdf","mahela")
