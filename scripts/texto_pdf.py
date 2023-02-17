import fitz
import os
import pandas as pd
import time
import datetime
import shutil


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
    
    #arrumar para funcionar com todos arquivos
     

    return output

def get_arquivo(path, ext = '.pdf'):
    '''Retorna uma lista com o caminho dos arquivos com a extensão especificada.'''

    lista_arq = []
    for file in os.listdir(path):
        if file.endswith(ext):
            data_c = os.stat(os.path.join(path, file)) # extrai informações sobre o arquivo tipo os.stat_result
            data_cri = time.ctime(data_c.st_ctime) # passa a informação para str 
            data = datetime.datetime.strptime(data_cri, '%a %b %d %H:%M:%S %Y') # passa para tipo datetime
            data_final = data.strftime('%d/%m/%Y') # altera o formato da data
            venc = data + datetime.timedelta(days = 10)
            #data_vencimento = venc.strftime('%d/%m/%Y')
            lista_arq.append([os.path.join(path, file), data_final, venc])

    return lista_arq

def troca_nome_dir(path): 
    '''Troca o caminho do diretório recebido'''

    path_split = path.split('\\')
    final_path = 'caminho' + '\\' + path_split[-1]
    return final_path


def att_excel(info):
    '''Atualiza a planilha de controle.'''
    #se doc já estiver na planilha, fazer nada
    #se não, atualizar planilha

    df = pd.read_excel()
    
 
if __name__ == '__main__':

    path = "caminho"
    
    df = pd.DataFrame(get_arquivo(path), columns=['Arquivo', 'Data de criação', 'Data de vencimento'])
    for i in range(0, len(df)):
        if df.iloc[i]['Data de vencimento'] < datetime.datetime.now():

            source = df.iloc[i]['Arquivo']
            destino = troca_nome_dir(source)
            shutil.move(source, destino)

