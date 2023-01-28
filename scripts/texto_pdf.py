import fitz
import os

def texto_pdf(arquivo):
    '''Retorna o texto do arquivo PDF(espero)'''
    
    doc = fitz.open(arquivo)
    pag = doc[0]
    texto = pag.get_text()
    linhas = texto.split('\n')
    
    return linhas[0]

def get_arquivo(path, ext = '.pdf'):
    '''Retorna uma lista com o caminho dos arquivos com a extensão especificada.'''

    lista_arq = []
    for file in os.listdir(path):
        if file.endswith(ext):
            lista_arq.append(os.path.join(path, file))

    return lista_arq





if __name__ == '__main__':
    arq = "caminho\\para\\arquivo."

    path = "caminho\\para\\pasta"
    
    print(get_arquivo(path))