

import tkinter as tk
from tkinter import ttk
from produto import ControleEstoqueApp
from Proprietario import ControleProprietarioApp

class PaginaInicial:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Gerenciamento")
        self.root.geometry("400x300")
        
        #Configuração para deixar o grid no centro
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        
        #Frame principal(padrão que irá seguir todo o código a menos que for sobrescrito)
        self.main_frame = ttk.Frame(self.root, padding="20")
        self.main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        #Configurar o grid do frame principal
        self.main_frame.columnconfigure(0, weight=1)
        
        #Título
        ttk.Label(self.main_frame, text="Sistema de Gerenciamento", font=("Arial", 16, "bold")).grid(row=0, column=0, pady=20)
        
        #Padrões dos botões
        button_frame = ttk.Frame(self.main_frame)
        button_frame.grid(row=1, column=0, pady=20)
        
        #Botões de controle
        ttk.Button(button_frame, text="Controle de Estoque", command=self.abrir_controle_estoque, width=25).grid(row=0, column=0, pady=10)
        ttk.Button(button_frame, text="Controle de Proprietários", command=self.abrir_controle_proprietarios, width=25).grid(row=1, column=0, pady=10)
        ttk.Button(button_frame, text="Sair", command=self.root.destroy, width=25).grid(row=2, column=0, pady=10)
        
    def abrir_controle_estoque(self):
        #Criar uma nova janela para o controle de estoque
        estoque_window = tk.Toplevel(self.root)
        app = ControleEstoqueApp(estoque_window)
        
    def abrir_controle_proprietarios(self):
        #Criar uma nova janela para o controle de proprietários
        proprietario_window = tk.Toplevel(self.root)
        app = ControleProprietarioApp(proprietario_window)

if __name__ == "__main__":
    root = tk.Tk()
    app = PaginaInicial(root)
    root.mainloop() 