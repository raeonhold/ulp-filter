import os
from tqdm import tqdm

def filtrar_urls_em_arquivos(url_filtro):
    arquivos_txt = [arquivo for arquivo in os.listdir() if arquivo.endswith('.txt') and arquivo != 'result.txt']
    
    if not arquivos_txt:
        print("no '.txt' files found in the directory.")
        return
    
    resultados_encontrados = False
    
    with open('result.txt', 'w', encoding='utf-8') as result_file:
        for arquivo in tqdm(arquivos_txt, desc="processing files", ncols=100, ascii=True):
            try:
                with open(arquivo, 'r', encoding='utf-8') as f:
                    linhas = f.readlines()
            except UnicodeDecodeError:
                print(f"Error decoding the file '{arquivo}'. Skipping.")
                continue

            filtradas = [linha.strip() for linha in linhas if linha.startswith(url_filtro)]

            if filtradas:
                result_file.write(f"\tResults from file: {arquivo}\n")
                for linha in filtradas:
                    result_file.write(linha + '\n')
                result_file.write("\n")
                resultados_encontrados = True
    
    if resultados_encontrados:
        print(f"Filtered results for '{url_filtro}' were saved in the file 'result.txt'.")
    else:
        print(f"No results found for '{url_filtro}' in any file.")


print(r"""

        _           __  _  _  _  
       | |         / _|(_)| || | 
 _   _ | | _ __   | |_  _ | || |_   ___  _ __ 
| | | || || '_ \  |  _|| || || __| / _ \| '__|
| |_| || || |_) | | |  | || || |_ |  __/| |   
 \__,_||_|| .__/  |_|  |_||_| \__| \___||_|   
          | |                                
          |_|                    by: shft


    """)

url_filtro = input("Enter the URL you want to filter: ")
filtrar_urls_em_arquivos(url_filtro)
