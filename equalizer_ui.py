import tkinter as tk
from tkinter import messagebox

# Equalizer APO 設定ファイルのパス
CONFIG_PATH = r"C:\Program Files\EqualizerAPO\config\config.txt"

def set_preamp(value):
    try:
        db_value = f"Preamp: {value} dB\n"
        with open(CONFIG_PATH, "r", encoding="utf-8") as f:
            lines = f.readlines()
        with open(CONFIG_PATH, "w", encoding="utf-8") as f:
            found = False
            for line in lines:
                if line.strip().lower().startswith("preamp:"):
                    f.write(db_value)
                    found = True
                else:
                    f.write(line)
            if not found:
                f.write("\n" + db_value)
        messagebox.showinfo("完了", f"Preampを {value} dB に設定しました！")
    except Exception as e:
        messagebox.showerror("エラー", f"設定ファイルの更新に失敗しました:\n{e}")

# UI作成
root = tk.Tk()
root.title("Equalizer APO 簡易コントロール")
root.geometry("300x150")

tk.Label(root, text="Preamp（全体音量）").pack(pady=5)
slider = tk.Scale(root, from_=-60, to=-40, orient="horizontal", resolution=1)
slider.set(-40)  # デフォルト -40dB（1%程度）
slider.pack()

tk.Button(root, text="適用", command=lambda: set_preamp(slider.get())).pack(pady=10)

root.mainloop()
