import tkinter as tk
from tkinter import ttk, messagebox

class Produto:
    def __init__(self, nome="", preco=0, estoque=0):
        self.nome = nome
        self.preco = preco
        self.estoque = estoque
        self.minEstoque = 0
        self.maxEstoque = 30

class ControleEstoqueApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Controle de Estoque")
        self.root.geometry("600x400")
        
        self.produtos = []
        
        
        self.main_frame = ttk.Frame(self.root, padding="10")
        self.main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        #Botão para voltar a página inicial
        self.voltar_btn = ttk.Button(self.main_frame, text="Voltar", command=self.voltar_pagina_inicial)
        self.voltar_btn.grid(row=0, column=0, sticky=tk.W, pady=5)
        
        #Campo para inserir dados
        ttk.Label(self.main_frame, text="Nome do Produto:").grid(row=1, column=0, sticky=tk.W, pady=5)
        self.nome_entry = ttk.Entry(self.main_frame, width=30)
        self.nome_entry.grid(row=1, column=1, pady=5)
        
        ttk.Label(self.main_frame, text="Preço:").grid(row=2, column=0, sticky=tk.W, pady=5)
        self.preco_entry = ttk.Entry(self.main_frame, width=30)
        self.preco_entry.grid(row=2, column=1, pady=5)
        
        ttk.Label(self.main_frame, text="Quantidade em Estoque:").grid(row=3, column=0, sticky=tk.W, pady=5)
        self.estoque_entry = ttk.Entry(self.main_frame, width=30)
        self.estoque_entry.grid(row=3, column=1, pady=5)
        
        #Botão de registrar
        self.registrar_btn = ttk.Button(self.main_frame, text="Registrar Produto", command=self.registrar_produto)
        self.registrar_btn.grid(row=4, column=0, columnspan=2, pady=20)
        
        #Lista dos produtos registrados
        self.tree = ttk.Treeview(self.main_frame, columns=("Nome", "Preço", "Estoque"), show="headings")
        self.tree.heading("Nome", text="Nome")
        self.tree.heading("Preço", text="Preço")
        self.tree.heading("Estoque", text="Estoque")
        self.tree.grid(row=5, column=0, columnspan=2, pady=10)
        
        #Scrollbar para a lista
        scrollbar = ttk.Scrollbar(self.main_frame, orient=tk.VERTICAL, command=self.tree.yview)
        scrollbar.grid(row=5, column=2, sticky=(tk.N, tk.S))
        self.tree.configure(yscrollcommand=scrollbar.set)

    def verificar_estoque(self, estoque):
        if estoque < 0:
            messagebox.showerror("Erro", "Número de unidades insuficiente!")
            return False
        elif estoque > 30:
            messagebox.showerror("Erro", "Você ultrapassou os limites do estoque!")
            return False
        return True

    def registrar_produto(self):
        try:
            nome = self.nome_entry.get()
            preco = float(self.preco_entry.get())
            estoque = int(self.estoque_entry.get())
            
            if not nome:
                messagebox.showerror("Erro", "Por favor, insira um nome para o produto!")
                return
                
            if not self.verificar_estoque(estoque):
                return
                
            produto = Produto(nome, preco, estoque)
            self.produtos.append(produto)
            
            #Adicionar à Treeview(Função que adiciona campos como se fosse lista)
            self.tree.insert("", tk.END, values=(nome, f"R${preco:.2f}", estoque))
            
            #Limpar
            self.nome_entry.delete(0, tk.END)
            self.preco_entry.delete(0, tk.END)
            self.estoque_entry.delete(0, tk.END)
            
            messagebox.showinfo("Sucesso", "Produto registrado com sucesso!")
            
        except ValueError:
            messagebox.showerror("Erro", "Por favor, insira valores válidos para preço e estoque!")

    def voltar_pagina_inicial(self):
        self.root.destroy()  

if __name__ == "__main__":
    root = tk.Tk()
    app = ControleEstoqueApp(root)
    root.mainloop() 