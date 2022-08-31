# ///////////////////////////////////////////////////////////////
#
# BY: JOAO PEDRO A. OLIVEIRA
#
# ///////////////////////////////////////////////////////////////
# ///////////////////////////////////////////////////////////////
# IMPORT / MODULES
# ///////////////////////////////////////////////////////////////

from tkinter import messagebox
from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time
import urllib

from .contatos import *
from .config import *


def on_final(time):
    if messagebox.showinfo(f"{program_name}",f"Todas as mensagens foram enviadas em {int(time/60)} minuto(s)!"):
        return

class WhatsappBot():
    def __init__(self) -> None:
        self.browser = webdriver.Chrome()
        self.browser.get('https://web.whatsapp.com/')
        self.wait_side()
        
    def wait_side(self):
        while True:
            try:
                side = self.browser.find_element(By.ID,'side')
                break
            except:
                time.sleep(1)

    def check_number(self):
        time.sleep(1)
        try:
            self.browser.find_element(By.XPATH,'//*[@id="app"]/div/span[2]/div/span/div/div/div/div/div/div[2]/div/div/div/div')
            return False
        except:   
            return True
            
    def press_enter(self):
        try:
            textbox = self.browser.find_element(By.XPATH,'//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p')
            textbox.send_keys(Keys.ENTER)
        except:
            pass

    def send_message(self,mensagem):
        start = time.time()
        contatos = get_contatos(folder)
        cont = 1
        for contato in contatos:

            telefone1 = contato[0]
            telefone2 = contato[1]
            telefone3 = contato[2]
            telefone4 = contato[3]
            telefone5 = contato[4]

            telefones = [
                telefone1,
                telefone2,
                telefone3,
                telefone4,
                telefone5
            ]

            nome = str(contato[6])

            texto = urllib.parse.quote(f"{mensagem}")

            for tel in telefones:
                if tel != "":
                    if tel[3] != 3:
                        starteach = time.time()
                        print("///////////////////////////////////////////////////////////////")
                        print(f"ID: {cont} | ENVIANDO MENSAGEM PARA O NUMERO: {tel} | NOME: {nome}")
                        link = f"https://web.whatsapp.com/send?phone=+55{tel}&text={texto}"
                        self.browser.get(link)
                        self.wait_side()
                        check = self.check_number()
                        if check == True:
                            self.press_enter()
                            finaleach = time.time()
                            timespendeach = finaleach - starteach
                            print(f"MENSAGEM ENVIADA EM {int(timespendeach)} SEGUNDOS!")
                            print("///////////////////////////////////////////////////////////////")
                        else:
                            print(f"NUMERO NÃO POSSUI WHATSAPP!")
                            print("///////////////////////////////////////////////////////////////")
                    else:
                        pass
                else:
                    pass
            cont += 1
            
        final = time.time()
        timespend = final - start
        self.browser.quit()
        return timespend