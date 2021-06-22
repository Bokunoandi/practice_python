import tkinter as tk
import math

window = tk.Tk()
window.title('Calculator')
window.geometry('480x700')
window.resizable(False, False)
window.config(bg='white')


# Фунцкія вираховування операцій калькулятору
def calculate(operation):
    global formula

    if operation == 'C':
        formula = ''
    elif operation == "DEL":
        formula = formula[0:-1]
    elif operation == "^2":
        formula = str((eval(formula)) ** 2)
    elif operation == "cos":
        formula = str(math.cos(eval(formula)))
    elif operation == "sin":
        formula = str(math.sin(eval(formula)))
    elif operation == "tan":
        formula = str(math.tan(eval(formula)))
    elif operation == "ln":
        formula = str(math.log1p(eval(formula)))
    elif operation == "log":
        formula = str(math.log(eval(formula)))
    elif operation == "ctg":
        formula = str(math.cos(eval(formula)) / math.sin(eval(formula)))
    elif operation == "bin":
        formula = str(bin(eval(formula)))
    elif operation == "=":
        formula = str(eval(formula))
    else:
        if formula == '0':
            formula = ''
        formula += operation
    label_text.configure(text=formula)


# Створення вікна для виводу результатів
formula = '0'
label_text = tk.Label(text=formula, font=('Arial', 21))
label_text.place(x=11, y=50)

# Кнопки
buttons = ["C", "DEL", "*", "=",
           "1", "2", "3", "/",
           "4", "5", "6", "+",
           "7", "8", "9", "-",
           "(", "0", ")", "^2",
           "cos", "sin", "tan", "ctg",
           "log", "ln", "%", "bin"]

x = 10
y = 140
for button in buttons:
    get_lbl = lambda x=button: calculate(x)
    tk.Button(text=button, bg='purple', font=('Arial', 21), command=get_lbl).place(x=x, y=y, width=115, height=79)
    x += 117
    if x > 400:
        x = 10
        y += 81

window.mainloop()
