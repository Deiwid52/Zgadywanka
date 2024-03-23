import tkinter as tk
from tkinter import messagebox
import random


class ZgadywankaGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Gra w zgadywanie liczby")

        self.wylosowana_liczba = random.randint(1, 100)
        self.liczba_prob = 0

        self.label_wiadomosc = tk.Label(master, text="Komputer wylosuje liczbę z przedziału od 1 do 100.")
        self.label_wiadomosc.pack()

        self.entry = tk.Entry(master)
        self.entry.pack()

        self.button_zgaduj = tk.Button(master, text="Zgadnij", command=self.sprawdz_strzal)
        self.button_zgaduj.pack()

        self.button_reset = tk.Button(master, text="Zagraj ponownie", command=self.reset_gry)
        self.button_reset.pack()

    def sprawdz_strzal(self):
        strzal = int(self.entry.get())
        self.liczba_prob += 1

        if strzal < self.wylosowana_liczba:
            messagebox.showinfo("Wynik",
                                "Za mało! Liczba jest {}".format("parzysta" if strzal % 2 == 0 else "nieparzysta"))
        elif strzal > self.wylosowana_liczba:
            messagebox.showinfo("Wynik",
                                "Za dużo! Liczba jest {}".format("parzysta" if strzal % 2 == 0 else "nieparzysta"))
        else:
            messagebox.showinfo("Wynik",
                                f"Brawo! Odgadłeś liczbę {self.wylosowana_liczba} w {self.liczba_prob} próbach!")
            self.button_zgaduj.config(state=tk.DISABLED)

    def reset_gry(self):
        self.wylosowana_liczba = random.randint(1, 100)
        self.liczba_prob = 0
        self.label_wiadomosc.config(text="Komputer wylosuje liczbę z przedziału od 1 do 100.")
        self.button_zgaduj.config(state=tk.NORMAL)


def main():
    root = tk.Tk()
    zgadywanka_gui = ZgadywankaGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
