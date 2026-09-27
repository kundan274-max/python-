import tkinter as tk
import math

def factorial():
    n = int(entry.get())
    result.config(text="Factorial = " + str(math.factorial(n)))

window = tk.Tk()
window.title("Factorial")
window.geometry("300x200")

tk.Label(window, text="Enter a number:").pack(pady=10)

entry = tk.Entry(window)
entry.pack()

tk.Button(window, text="Find Factorial", command=factorial).pack(pady=10)

result = tk.Label(window, text="")
result.pack()

window.mainloop()