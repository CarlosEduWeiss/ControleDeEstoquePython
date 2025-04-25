import tkinter as tk
from tkinter import ttk, messagebox
import re

class Proprietario:
    def __init__(self, nome="", cpf="", telefone="", email=""):
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone
        self.email = email

class ControleProprietarioApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Controle de Proprietários")
        self.root.geometry("800x600")
        
        self.proprietarios = []
        
        # Frame principal
        self.main_frame = ttk.Frame(self.root, padding="10")
        self.main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Configurar o grid para expandir
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        self.main_frame.columnconfigure(1, weight=1)
        
        # Botão para voltar à página inicial
        self.voltar_btn = ttk.Button(self.main_frame, text="Voltar", command=self.voltar_pagina_inicial)
        self.voltar_btn.grid(row=0, column=0, sticky=tk.W, pady=5)
        
        # Campos de entrada
        ttk.Label(self.main_frame, text="Nome:").grid(row=1, column=0, sticky=tk.W, pady=5)
        self.nome_entry = ttk.Entry(self.main_frame, width=30)
        self.nome_entry.grid(row=1, column=1, pady=5, sticky=tk.W)
        
        ttk.Label(self.main_frame, text="CPF:").grid(row=2, column=0, sticky=tk.W, pady=5)
        self.cpf_entry = ttk.Entry(self.main_frame, width=30)
        self.cpf_entry.grid(row=2, column=1, pady=5, sticky=tk.W)
        self.cpf_entry.bind('<KeyRelease>', self.formatar_cpf)
        
        ttk.Label(self.main_frame, text="Telefone:").grid(row=3, column=0, sticky=tk.W, pady=5)
        self.telefone_entry = ttk.Entry(self.main_frame, width=30)
        self.telefone_entry.grid(row=3, column=1, pady=5, sticky=tk.W)
        self.telefone_entry.bind('<KeyRelease>', self.formatar_telefone)
        
        ttk.Label(self.main_frame, text="Email:").grid(row=4, column=0, sticky=tk.W, pady=5)
        self.email_entry = ttk.Entry(self.main_frame, width=30)
        self.email_entry.grid(row=4, column=1, pady=5, sticky=tk.W)
        
        # Botão de registro
        self.registrar_btn = ttk.Button(self.main_frame, text="Registrar Proprietário", command=self.registrar_proprietario)
        self.registrar_btn.grid(row=5, column=0, columnspan=2, pady=20)
        
        # Lista de proprietários
        self.tree = ttk.Treeview(self.main_frame, columns=("Nome", "CPF", "Telefone", "Email"), show="headings")
        self.tree.heading("Nome", text="Nome")
        self.tree.heading("CPF", text="CPF")
        self.tree.heading("Telefone", text="Telefone")
        self.tree.heading("Email", text="Email")
        
        # Configurar largura das colunas
        self.tree.column("Nome", width=200)
        self.tree.column("CPF", width=150)
        self.tree.column("Telefone", width=150)
        self.tree.column("Email", width=200)
        
        self.tree.grid(row=6, column=0, columnspan=2, pady=10, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Scrollbar para a lista
        scrollbar = ttk.Scrollbar(self.main_frame, orient=tk.VERTICAL, command=self.tree.yview)
        scrollbar.grid(row=6, column=2, sticky=(tk.N, tk.S))
        self.tree.configure(yscrollcommand=scrollbar.set)
        
        # Configurar o grid para expandir a lista
        self.main_frame.rowconfigure(6, weight=1)

    def formatar_cpf(self, event=None):
        cpf = self.cpf_entry.get()
        cpf = ''.join(filter(str.isdigit, cpf))
        if len(cpf) > 11:
            cpf = cpf[:11]
        if len(cpf) > 9:
            cpf = f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"
        elif len(cpf) > 6:
            cpf = f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:]}"
        elif len(cpf) > 3:
            cpf = f"{cpf[:3]}.{cpf[3:]}"
        self.cpf_entry.delete(0, tk.END)
        self.cpf_entry.insert(0, cpf)

    def formatar_telefone(self, event=None):
        telefone = self.telefone_entry.get()
        telefone = ''.join(filter(str.isdigit, telefone))
        if len(telefone) > 11:
            telefone = telefone[:11]
        if len(telefone) > 10:
            telefone = f"({telefone[:2]}) {telefone[2:7]}-{telefone[7:]}"
        elif len(telefone) > 6:
            telefone = f"({telefone[:2]}) {telefone[2:6]}-{telefone[6:]}"
        elif len(telefone) > 2:
            telefone = f"({telefone[:2]}) {telefone[2:]}"
        self.telefone_entry.delete(0, tk.END)
        self.telefone_entry.insert(0, telefone)

    def validar_cpf(self, cpf):
        # Remove caracteres não numéricos
        cpf = ''.join(filter(str.isdigit, cpf))
        
        if len(cpf) != 11:
            return False
            
        # Verifica se todos os dígitos são iguais
        if cpf == cpf[0] * 11:
            return False
            
        # Validação do primeiro dígito verificador
        soma = sum(int(cpf[i]) * (10 - i) for i in range(9))
        digito1 = (soma * 10 % 11) % 10
        if int(cpf[9]) != digito1:
            return False
            
        # Validação do segundo dígito verificador
        soma = sum(int(cpf[i]) * (11 - i) for i in range(10))
        digito2 = (soma * 10 % 11) % 10
        if int(cpf[10]) != digito2:
            return False
            
        return True

    def validar_telefone(self, telefone):
        # Remove caracteres não numéricos
        telefone = ''.join(filter(str.isdigit, telefone))
        return len(telefone) >= 10 and len(telefone) <= 11

    def validar_email(self, email):
        padrao = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return bool(re.match(padrao, email))

    def registrar_proprietario(self):
        try:
            nome = self.nome_entry.get().strip()
            cpf = self.cpf_entry.get()
            telefone = self.telefone_entry.get()
            email = self.email_entry.get().strip()
            
            if not nome:
                messagebox.showerror("Erro", "Por favor, insira um nome!")
                return
                
            if not self.validar_cpf(cpf):
                messagebox.showerror("Erro", "CPF inválido!")
                return
                
            if not self.validar_telefone(telefone):
                messagebox.showerror("Erro", "Telefone inválido! Deve conter 10 ou 11 dígitos.")
                return
                
            if not self.validar_email(email):
                messagebox.showerror("Erro", "Email inválido!")
                return
                
            # Verificar se o CPF já está cadastrado
            for p in self.proprietarios:
                if p.cpf == cpf:
                    messagebox.showerror("Erro", "Este CPF já está cadastrado!")
                    return
                
            proprietario = Proprietario(nome, cpf, telefone, email)
            self.proprietarios.append(proprietario)
            
            # Adicionar à Treeview
            self.tree.insert("", tk.END, values=(nome, cpf, telefone, email))
            
            # Limpar campos
            self.nome_entry.delete(0, tk.END)
            self.cpf_entry.delete(0, tk.END)
            self.telefone_entry.delete(0, tk.END)
            self.email_entry.delete(0, tk.END)
            
            messagebox.showinfo("Sucesso", "Proprietário registrado com sucesso!")
            
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao registrar proprietário: {str(e)}")

    def voltar_pagina_inicial(self):
        self.root.destroy()  # Fecha a janela atual

if __name__ == "__main__":
    root = tk.Tk()
    app = ControleProprietarioApp(root)
    root.mainloop()

 
