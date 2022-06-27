import tkinter as tk
import tkinter.font as tkfont
import pyperclip as clip
import os, sys

# PyInstaller Compatibility

def rsrc_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

# Initializing Window

root = tk.Tk()
root.title("Fraccents")
root.resizable(width=False, height=False)
root.iconbitmap(rsrc_path("icon.ico"))

# Variables

is_capital = tk.BooleanVar()

# Font Data

acc_font = tkfont.Font(root, family="Helvetica", size=18, weight="bold")

# Frames for Each Section

accents_frame = tk.Frame(root, padx=15, pady=15, width=300)

# Functions

def copy(char):
    if is_capital.get():
        try:
            clip.copy(char.upper())
            status["text"] = "Accent copié au presse-papiers!"
            status["fg"] = "#090"
        except:
            status["text"] = "Erreur!"
            status["fg"] = "#f00"
    else:
        try:
            clip.copy(char)
            status["text"] = "Accent copié au presse-papiers!"
            status["fg"] = "#090"
        except:
            status["text"] = "Erreur!"
            status["fg"] = "#f00"

def cap_btn_txt():
    if is_capital.get():
        e_aigu["text"] = e_aigu["text"].upper()
        a_grave["text"] = a_grave["text"].upper()
        e_grave["text"] = e_grave["text"].upper()
        u_grave["text"] = u_grave["text"].upper()
        c_cedille["text"] = c_cedille["text"].upper()
        a_cflexe["text"] = a_cflexe["text"].upper()
        e_cflexe["text"] = e_cflexe["text"].upper()
        i_cflexe["text"] = i_cflexe["text"].upper()
        o_cflexe["text"] = o_cflexe["text"].upper()
        u_cflexe["text"] = u_cflexe["text"].upper()
        e_trema["text"] = e_trema["text"].upper()
        i_trema["text"] = i_trema["text"].upper()
        u_trema["text"] = u_trema["text"].upper()
    else:
        e_aigu["text"] = e_aigu["text"].lower()
        a_grave["text"] = a_grave["text"].lower()
        e_grave["text"] = e_grave["text"].lower()
        u_grave["text"] = u_grave["text"].lower()
        c_cedille["text"] = c_cedille["text"].lower()
        a_cflexe["text"] = a_cflexe["text"].lower()
        e_cflexe["text"] = e_cflexe["text"].lower()
        i_cflexe["text"] = i_cflexe["text"].lower()
        o_cflexe["text"] = o_cflexe["text"].lower()
        u_cflexe["text"] = u_cflexe["text"].lower()
        e_trema["text"] = e_trema["text"].lower()
        i_trema["text"] = i_trema["text"].lower()
        u_trema["text"] = u_trema["text"].lower()

# Elements for Accents Frame

e_aigu = tk.Button(accents_frame, text="é", padx=5, pady=5, font=acc_font, command=lambda: copy("é"))
a_grave = tk.Button(accents_frame, text="à", padx=5, pady=5, font=acc_font, command=lambda: copy("à"))
e_grave = tk.Button(accents_frame, text="è", padx=5, pady=5, font=acc_font, command=lambda: copy("è"))
u_grave = tk.Button(accents_frame, text="ù", padx=5, pady=5, font=acc_font, command=lambda: copy("ù"))
c_cedille = tk.Button(accents_frame, text="ç", padx=5, pady=5, font=acc_font, command=lambda: copy("ç"))

a_cflexe = tk.Button(accents_frame, text="â", padx=5, pady=5, font=acc_font, command=lambda: copy("â"))
e_cflexe = tk.Button(accents_frame, text="ê", padx=5, pady=5, font=acc_font, command=lambda: copy("ê"))
i_cflexe = tk.Button(accents_frame, text="î", padx=8, pady=5, font=acc_font, command=lambda: copy("î"))
o_cflexe = tk.Button(accents_frame, text="ô", padx=5, pady=5, font=acc_font, command=lambda: copy("ô"))
u_cflexe = tk.Button(accents_frame, text="û", padx=5, pady=5, font=acc_font, command=lambda: copy("û"))

e_trema = tk.Button(accents_frame, text="ë", padx=5, pady=5, font=acc_font, command=lambda: copy("ë"))
i_trema = tk.Button(accents_frame, text="ï", padx=7, pady=5, font=acc_font, command=lambda: copy("ï"))
u_trema = tk.Button(accents_frame, text="ü", padx=5, pady=5, font=acc_font, command=lambda: copy("ü"))
guillemet_g = tk.Button(accents_frame, text="«", padx=5, pady=5, font=acc_font, command=lambda: copy("«"))
guillemet_d = tk.Button(accents_frame, text="»", padx=5, pady=5, font=acc_font, command=lambda: copy("»"))

# Capitalize Checkbox (Majuscule)

majuscule = tk.Checkbutton(root, text="Majuscule", variable=is_capital, command=cap_btn_txt)

# Status Bar

status = tk.Label(root, text="Cliquez sur un accent pour copier")

# Placing Elements on Window

accents_frame.pack(padx=15, pady=(15, 5))

e_aigu.grid(row=0, column=0)
a_grave.grid(row=0, column=1)
e_grave.grid(row=0, column=2)
u_grave.grid(row=0, column=3)
c_cedille.grid(row=0, column=4)

a_cflexe.grid(row=1, column=0)
e_cflexe.grid(row=1, column=1)
i_cflexe.grid(row=1, column=2)
o_cflexe.grid(row=1, column=3)
u_cflexe.grid(row=1, column=4)

e_trema.grid(row=2, column=0)
i_trema.grid(row=2, column=1)
u_trema.grid(row=2, column=2)
guillemet_g.grid(row=2, column=3)
guillemet_d.grid(row=2, column=4)

majuscule.pack(pady=(0, 10))
status.pack(pady=(0, 10))

# Set Icon, Keep Window on Top and From Closing

root.call('wm', 'attributes', '.', '-topmost', '1')
root.mainloop()