import tkinter as tk
from tkinter import messagebox

class Controle:
    def __init__(self):
        self.janela = tk.Tk()
        self.janela.geometry("800x600")
        self.janela.title("Calculo de desconto")

        self.label = tk.Label(self.janela, text="Calculo de desconto")
        self.label.pack()

        self.label_2 = tk.Label(self.janela, text="Salario:")
        self.label_2.pack()

        self.txtSalario = tk.Entry(self.janela)
        self.txtSalario.pack()

        self.label_3 = tk.Label(self.janela, text="Desconto:")
        self.label_3.pack()

        self.txtDesconto = tk.Entry(self.janela)
        self.txtDesconto.pack()

        self.btnCalcular = tk.Button(self.janela, text="Calcular", command=self.calcular)
        self.btnCalcular.pack()

        self.btnLimpar = tk.Button(self.janela, text="Limpar", command=self.limpar)
        self.btnLimpar.pack()

        self.btnSair = tk.Button(self.janela, text="Sair", command=self.sair)
        self.btnSair.pack()

        self.janela.mainloop()
    def calcular(self):
        try:
            salario = float(self.txtSalario.get())
            desconto = float(self.txtDesconto.get())
            valor_desconto = salario * (desconto / 100)
            salario_final = salario - valor_desconto
            messagebox.showinfo("Resultado", f"Salario final após desconto: {salario_final:.2f}")
        except ValueError:
            messagebox.showerror("Erro", "Por favor, insira valores numéricos válidos.")
    def limpar(self):
        self.txtSalario.delete(0, tk.END)
        self.txtDesconto.delete(0, tk.END)
    def sair(self):
        self.janela.destroy()
if __name__ == "__main__":
    controle = Controle()
    

    






