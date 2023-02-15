import PyPDF2

# Récupération du nom du fichier PDF à protéger et du mot de passe à utiliser
pdf_file = input("Nom du fichier PDF à protéger: ")
password = input("Mot de passe pour protéger le fichier PDF: ")

# Ouverture du fichier PDF et création d'un objet PDFReader
with open(pdf_file, 'rb') as file:
    pdf_reader = PyPDF2.PdfFileReader(file)

    # Vérification que le fichier PDF n'est pas déjà protégé par un mot de passe
    if pdf_reader.isEncrypted:
        print("Le fichier PDF est déjà protégé par un mot de passe.")
        exit()

    # Création d'un objet PDFWriter et copie de chaque page du PDF original
    pdf_writer = PyPDF2.PdfFileWriter()
    for page_num in range(pdf_reader.numPages):
        pdf_writer.addPage(pdf_reader.getPage(page_num))

    # Cryptage du PDF avec le mot de passe spécifié
    pdf_writer.encrypt(password)

    # Écriture du fichier PDF crypté sur le disque dur
    with open('secure_' + pdf_file, 'wb') as output_file:
        pdf_writer.write(output_file)

print("Le fichier PDF a été crypté avec succès avec le mot de passe spécifié.")

