import fitz
import os
import pandas as pd

def texto_pdf(arquivo):
    '''Retorna o texto do arquivo PDF(espero)'''
    
    doc = fitz.open(arquivo)
    pag = doc[0]
    texto = pag.get_text()
    linhas = texto.split('\n')
    doc.close()

    # arrumar para extrair apenas o texto desejado

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
    xl = "caminho\\para\\planilha.xlsm"
    
    if os.path.exists(xl):
        arquivos = get_arquivo(path)
        for arquivo in arquivos:
            # utilizar função texto_pdf(arquivo) para obter o texto do arquivo;
            # utilizar função para escrever no excel
            pass

    else:
        print('Arquivo não encontrado.') # talvez criar um arquivo novo
