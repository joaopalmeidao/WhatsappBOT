# ///////////////////////////////////////////////////////////////
#
# BY: JOAO PEDRO A. OLIVEIRA
#
# ///////////////////////////////////////////////////////////////
# ///////////////////////////////////////////////////////////////
# IMPORT / MODULES
# ///////////////////////////////////////////////////////////////

from tkinter import *
from tkinter.ttk import Treeview
import webbrowser as wbb

from .whatsapp import *

# ///////////////////////////////////////////////////////////////
# GUI COLORS
# ///////////////////////////////////////////////////////////////

black = "#000000"  
white = "#feffff" 
green = "#25D366"  
grayblue = "#38576b" 
grey = "#403d3d"   

# ///////////////////////////////////////////////////////////////
# GUI 
# ///////////////////////////////////////////////////////////////

class App(Tk):
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        self.resizable(width=False,height=False)
        self.iconbitmap(icon_folder + "rpa_ico.ico")
        self.title(f"{program_name}")
        self.configure(background=white)
        self.resizable(width=FALSE,height=FALSE)
        self.bind("<Escape>", self.on_closing_event)
        self.protocol("WM_DELETE_WINDOW", self.on_closing)

    def on_firststart(self):
        contatos = get_contatos(folder)
        if len(contatos) != 0:
            self.withdraw()
            self.data_window()
        else:
            if messagebox.showinfo(f"{program_name} | Start", f"Nenhuma Planilha na pasta 'arquivos'!"):
                pass
    
    def on_firststart_event(self,event):
        self.on_firststart()

    def on_start(self):
        data_window.withdraw()
        self.deiconify()
        contatos = get_contatos(folder)

        if len(contatos) != 0:
            if messagebox.askokcancel(f"{program_name} | Start", f"Deseja iniciar o BOT?"):
                self.manager_init()
            else:
                self.withdraw()
                data_window.deiconify()
        else:
            if messagebox.showinfo(f"{program_name} | Start", f"Nenhuma Planilha na pasta 'arquivos'!"):
                self.deiconify()

    def manager_init(self):
        data_window.destroy()
        self.withdraw()
        time_spend = WhatsappBot().send_message(userentry.get(1.0, END))
        self.deiconify()
        on_final(time_spend)
        self.main_window()
    
    def on_closing(self):
        exit()

    def on_closing_event(self,event):
        if messagebox.askokcancel(f"{program_name} | Quit", "Deseja sair?"):
            exit()
    
    def main_window(self):
        global userentry

        self.titleframe = Frame(self,width=310, height=60,bg=white, relief="flat")
        self.titleframe.grid(row=0, column=0,pady=1, padx=0, sticky=NSEW)
        self.infoframe = Frame(self,width=240, height=300,bg=white, relief="flat")
        self.infoframe.grid(row=1, column=0,pady=1, padx=0, sticky=NSEW)

        titlelabel = Label(self.titleframe, text=f"{program_name}", height=1,anchor=NE, font=('Ivy 15'), bg=white, fg=grey)
        titlelabel.pack()
        linelabel = Label(self.titleframe, width=300, text="", height=1,anchor=NW, font=('Ivy 1 '), bg=green)
        linelabel.pack()
        infolabel = Label(self.infoframe, text="Escreva a Mensagem", height=1,anchor=NW, font=('Ivy 10 bold'), bg=white, fg=grey)
        infolabel.pack()
        userentry = Text(self.infoframe, height=8,width=50, font=("",15),highlightthickness=1, relief="solid")
        userentry.pack()

        startbutton = Button(self.infoframe, command=self.on_firststart, text="INICIAR", width=20, height=2, bg=green, fg=white, font=('Ivy 12 bold'), relief=RAISED, overrelief=RIDGE)
        startbutton.pack(pady=30)
        credtslabel = Label(self.infoframe,text=".::. By: João Pedro A. Oliveira .::.",anchor=NW,font="ivy 7 bold",bg=white,fg=black)
        credtslabel.pack()
        
        credtslabel.bind("<Double-Button-1>",lambda e: wbb.open_new(LinkedIn))

    def data_window(self):
        global data_window

        def on_datawindowclosing():
            data_window.destroy()
            self.deiconify()

        try:
            contatos = get_contatos(folder)

            id=1
            valores = []
            for n in contatos:
                valores.append((f'{(id)}', f'{n[6]}', f'{n[0]}', f'{n[1]}', f'{n[2]}', f'{n[3]}', f'{n[4]}'))
                id+=1
            
            data_window = Toplevel()
            data_window.iconbitmap(icon_folder + "rpa_ico.ico")
            data_window.title(f"{program_name} | CONTATOS")
            data_window.configure(background=white)
            data_window.resizable(width=FALSE,height=FALSE)
            data_window.protocol("WM_DELETE_WINDOW", on_datawindowclosing)

            titleframe = Frame(data_window,bg=white, relief="flat")
            titleframe.grid(row=0, column=0,pady=1, padx=0, sticky=NSEW)
            infoframe = Frame(data_window,bg=white, relief="flat")
            infoframe.grid(row=1, column=0,pady=1, padx=0, sticky=NSEW)

            
            columns = ('id', 'Nome', 'Telefone 1', 'Telefone 2', 'Telefone 3', 'Telefone 4', 'Telefone 5')

            tree = Treeview(infoframe, columns=columns, show='headings',height=20)

            tree.column('id',width=40,minwidth=25,stretch=NO)
            tree.column('Nome',width=300,minwidth=250,stretch=NO)
            tree.column('Telefone 1',width=100,minwidth=80,stretch=NO)
            tree.column('Telefone 2',width=100,minwidth=80,stretch=NO)
            tree.column('Telefone 3',width=100,minwidth=80,stretch=NO)
            tree.column('Telefone 4',width=100,minwidth=80,stretch=NO)
            tree.column('Telefone 5',width=100,minwidth=80,stretch=NO)
            

            tree.heading('id', text='ID')
            tree.heading('Nome', text='Nome')
            tree.heading('Telefone 1', text='Telefone 1')
            tree.heading('Telefone 2', text='Telefone 2')
            tree.heading('Telefone 3', text='Telefone 3')
            tree.heading('Telefone 4', text='Telefone 4')
            tree.heading('Telefone 5', text='Telefone 5')
            
            for i in valores:
                tree.insert('',END,values=i)
                    
            def item_selected(event):
                for selected_item in tree.selection():
                    item = tree.item(selected_item)
                    record = item['values']
                    if messagebox.askokcancel(title='Information', message=str(record)):
                        pass
            
            titlelabel = Label(titleframe, text="CONTATOS", height=1,anchor=NE, font=('Ivy 15'), bg=white, fg=grey)
            titlelabel.pack()
            linelabel = Label(titleframe, width=600, text="", height=1,anchor=NW, font=('Ivy 1 '), bg=green)
            linelabel.pack() 

            tree.grid(row=0, column=0, sticky='nsew')
            scrollbar = Scrollbar(infoframe, orient=VERTICAL, command=tree.yview)
            tree.configure(yscroll=scrollbar.set)
            scrollbar.grid(row=0, column=1, sticky='ns')
            linelabel = Label(infoframe, text="", height=3,anchor=NW, font=('Ivy 1 '), bg=white)
            linelabel.grid(row=2, column=0, sticky='nsew')
            startbutton = Button(infoframe, command=self.on_start, text="INICIAR", width=25, height=2, bg=green, fg=white, font=('Ivy 12 bold'), relief=RAISED, overrelief=RIDGE)
            startbutton.grid(row=3, column=0, sticky='nsew')
            credtslabel = Label(infoframe,text=".::. By: João Pedro A. Oliveira .::.",anchor=CENTER,font="ivy 7 bold",bg=white,fg=black)
            credtslabel.grid(row=4, column=0, sticky='nsew')
            
            credtslabel.bind("<Double-Button-1>",lambda e: wbb.open_new(LinkedIn))

        except:
            self.deiconify()
            if messagebox.showerror(f"{program_name} | ERROR","Erro ao ler a Planilha!"):
                pass
