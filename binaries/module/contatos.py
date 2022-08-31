from .readcsv import Read_csv


def get_contatos(folder):
    
    file = Read_csv(folder)
    all = file.all_files()

    tabelas = []
    for i in all: 
        result = file.csv_data(i)
        tabelas.append(result)
        
    contatos = []
    for table in tabelas:
        for row in table:
            contatos.append(row)
    return contatos
