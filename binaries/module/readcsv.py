# ///////////////////////////////////////////////////////////////
#
# BY: JOAO PEDRO A. OLIVEIRA
#
# ///////////////////////////////////////////////////////////////
# ///////////////////////////////////////////////////////////////
# IMPORT / MODULES
# ///////////////////////////////////////////////////////////////

import csv
import os

class Read_csv():
    def __init__(self,directory) -> None:
        self.directory = directory
        
    def all_files(self):
        return [os.path.join(self.directory+file) for file in os.listdir(self.directory) if file.lower().endswith("csv")]

    def csv_data(self,file):
        contatos = []
        with open(file,"r") as arq:
            csv_file = csv.reader(arq,delimiter=";")
            cont = 0
            for i in csv_file:
                if cont != 0:
                    contatos.append(i)
                else:
                    pass
                cont += 1
        return contatos
            


