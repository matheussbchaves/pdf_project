import PyPDF2

# abrir o arquivo pdf
with open("C:\\Users\\mathe\\Downloads\\TrabalhoFinal.pdf", 'rb') as pdf_file:
    # criar um objeto pdf reader
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    
    # pegar o numero de páginas no pdf
    num_pages = len(pdf_reader.pages)
    
    # iterar sobre as páginas
    for i in range(len(pdf_reader.pages)):
        # pegar a página atual
        page = pdf_reader.pages[i]
        
        # extrair o texto da página
        text = page.extract_text()
        
        # imprimir o texto extraído
        print(text)

# fechar o arquivo pdf
pdf_file.close()     

