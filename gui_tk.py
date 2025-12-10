import tkinter as tk
from tkinter import messagebox


def mostrar_mensagem():
    messagebox.showinfo('Olá', 'Esta é uma GUI leve usando tkinter.')


def calcular_imc_window():
    def calcular():
        try:
            peso = float(entry_peso.get().replace(',','.'))
            altura = float(entry_altura.get().replace(',','.'))
            if altura <= 0:
                raise ValueError()
            imc = peso / (altura ** 2)
            messagebox.showinfo('Resultado', f'IMC = {imc:.2f}')
            top.destroy()
        except Exception:
            messagebox.showerror('Erro', 'Por favor, insira números válidos para peso e altura.')

    top = tk.Toplevel()
    top.title('Calculadora de IMC')
    tk.Label(top, text='Peso (kg):').grid(row=0, column=0, padx=8, pady=6)
    entry_peso = tk.Entry(top)
    entry_peso.grid(row=0, column=1, padx=8, pady=6)
    tk.Label(top, text='Altura (m):').grid(row=1, column=0, padx=8, pady=6)
    entry_altura = tk.Entry(top)
    entry_altura.grid(row=1, column=1, padx=8, pady=6)
    tk.Button(top, text='Calcular', command=calcular).grid(row=2, column=0, columnspan=2, pady=8)


def main():
    root = tk.Tk()
    root.title('Exemplo GUI - Curso_Python')
    root.geometry('300x160')

    tk.Label(root, text='GUI leve com tkinter', font=('Segoe UI', 12, 'bold')).pack(pady=8)

    btn_msg = tk.Button(root, text='Mostrar mensagem', width=20, command=mostrar_mensagem)
    btn_msg.pack(pady=6)

    btn_imc = tk.Button(root, text='Calculadora de IMC', width=20, command=calcular_imc_window)
    btn_imc.pack(pady=6)

    tk.Label(root, text='Feche a janela para sair.').pack(side='bottom', pady=6)

    root.mainloop()


if __name__ == '__main__':
    main()
