import fitz
import os
import pandas as pd

def texto_pdf(arquivo):
    '''Retorna o texto do arquivo PDF.'''
    
    doc = fitz.open(arquivo)
    pag = doc[0]
    texto = pag.get_text()
    linhas = texto.split('\n')
    doc.close()

    output = {
            'Checkdate': linhas[83],
            'Name of User': linhas[84],
            'Department': linhas[85],
            'User-Id': linhas[86],
            'Order': linhas[87:88],
            'AWV': linhas[89],
            'Order Recipient (Seller)': linhas[41],
            'Customer(Buyer)': linhas[45],
            'Recipient of Goods/Service': linhas[49],
            'Ultimate End-User': linhas[53],
            'Sender / Suplier': linhas[57]
            }
     

    return output

def get_arquivo(path, ext = '.pdf'):
    '''Retorna uma lista com o caminho dos arquivos com a extensão especificada.'''

    lista_arq = []
    for file in os.listdir(path):
        if file.endswith(ext):
            lista_arq.append(os.path.join(path, file))

    return lista_arq

def att_excel(info):
    '''Atualiza a planilha de controle.'''
    #se doc já estiver na planilha, fazer nada
    #se não, atualizar planilha


if __name__ == '__main__':

    arq = "arquivo.pdf"
    path = "diretório"
    xl = "planilha.xlsm"
    

    info = pd.DataFrame(texto_pdf(arq))

    print(info)

    print(get_arquivo(path))

    
    if os.path.exists(xl):
        arquivos = get_arquivo(path)
        for arquivo in arquivos:
            # utilizar função texto_pdf(arquivo) para obter o texto do arquivo;
            # utilizar função para escrever no excel
            pass

    else:
        print('Arquivo não encontrado.') # talvez criar um arquivo novo
