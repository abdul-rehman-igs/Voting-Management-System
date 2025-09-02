import tkinter as tk
from tkinter import ttk, messagebox
import csv
from PIL import ImageTk, Image

# ---------------- CANDIDATES ----------------
candidates = {
    "President": [("Ali", "🌟"), ("Sara", "🏆"), ("Hamza", "🦁")],
    "Head Boy": [("Ahmed", "⚡"), ("Bilal", "🔥"), ("Danish", "🚀")],
    "Head Girl": [("Ayesha", "🌸"), ("Hina", "🌺"), ("Maryam", "🌼")],
    "House Captains": {
        "Yellow": [("Usman", "☀️"), ("Owais", "🍋")],
        "Red": [("Zara", "🌹"), ("Iqra", "🍎")],
        "Green": [("Aliya", "🌿"), ("Noor", "🍏")],
        "Blue": [("Fatima", "🌊"), ("Hira", "💎")]
    },
    "Prefects": [("Kashif", "🎯"), ("Saad", "📘"), ("Mona", "🎶"), ("Anam", "📗")]
}

# ---------------- VOTES ----------------
votes = {
    "President": {},
    "Head Boy": {},
    "Head Girl": {},
    "House Captains": {"Yellow": {}, "Red": {}, "Green": {}, "Blue": {}},
    "Prefects": {}
}

# Initialize votes
for category in ["President", "Head Boy", "Head Girl"]:
    for cand, sym in candidates[category]:
        votes[category][cand] = 0
for house in candidates["House Captains"]:
    for cand, sym in candidates["House Captains"][house]:
        votes["House Captains"][house][cand] = 0
for cand, sym in candidates["Prefects"]:
    votes["Prefects"][cand] = 0


# ---------------- FUNCTIONS ----------------
def cast_vote():
    pres = president_var.get()
    hb = headboy_var.get()
    hg = headgirl_var.get()
    hy = yellow_var.get()
    hr = red_var.get()
    hg_cap = green_var.get()
    hb_cap = blue_var.get()
    prefs = [cand for cand, var in prefect_vars.items() if var.get() == 1]

    if not pres or not hb or not hg or not hy or not hr or not hg_cap or not hb_cap:
        messagebox.showerror("Error", "Please select for all categories!")
        return

    votes["President"][pres] += 1
    votes["Head Boy"][hb] += 1
    votes["Head Girl"][hg] += 1
    votes["House Captains"]["Yellow"][hy] += 1
    votes["House Captains"]["Red"][hr] += 1
    votes["House Captains"]["Green"][hg_cap] += 1
    votes["House Captains"]["Blue"][hb_cap] += 1
    for pf in prefs:
        votes["Prefects"][pf] += 1

    messagebox.showinfo("Success", "✅ Your vote has been recorded!")
    reset_form()


def reset_form():
    president_var.set("")
    headboy_var.set("")
    headgirl_var.set("")
    yellow_var.set("")
    red_var.set("")
    green_var.set("")
    blue_var.set("")
    for var in prefect_vars.values():
        var.set(0)


def save_results_csv(filename="election_results.csv"):
    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Category", "Candidate", "Votes"])
        for category in ["President", "Head Boy", "Head Girl"]:
            for cand, v in votes[category].items():
                writer.writerow([category, cand, v])
        for house in votes["House Captains"]:
            for cand, v in votes["House Captains"][house].items():
                writer.writerow([f"{house} House Captain", cand, v])
        for cand, v in votes["Prefects"].items():
            writer.writerow(["Prefect", cand, v])


def show_results():
    result_win = tk.Toplevel(root)
    result_win.title("Election Results")
    result_win.geometry("500x500")

    text = tk.Text(result_win, font=("Arial", 12))
    text.pack(expand=True, fill="both")

    for category in ["President", "Head Boy", "Head Girl"]:
        text.insert("end", f"\n{category}:\n")
        for cand, v in votes[category].items():
            text.insert("end", f"{cand}: {v} votes\n")
        winner = max(votes[category], key=votes[category].get)
        text.insert("end", f"🏆 Winner: {winner}\n")

    text.insert("end", "\nHouse Captains:\n")
    for house in votes["House Captains"]:
        text.insert("end", f"\n{house} House:\n")
        for cand, v in votes["House Captains"][house].items():
            text.insert("end", f"{cand}: {v} votes\n")
        winner = max(votes["House Captains"][house], key=votes["House Captains"][house].get)
        text.insert("end", f"🏆 Winner: {winner}\n")

    text.insert("end", "\nPrefects:\n")
    for cand, v in votes["Prefects"].items():
        text.insert("end", f"{cand}: {v} votes\n")

    save_results_csv()
    text.insert("end", "\n📂 Results also saved in 'election_results.csv'\n")


# ---------------- GUI ----------------
root = tk.Tk()
root.title("Pak British Voting Management System")
root.geometry("800x800")

# Background Image (replace 'school_bg.jpg' with your image path)
try:
    bg_image = Image.open(r"C:\Users\Tab & Tech\Documents\python\practice\voting management\school_bg.jpg")
    bg_image = bg_image.resize((800, 800), Image.LANCZOS)
    bg_photo = ImageTk.PhotoImage(bg_image)
    bg_label = tk.Label(root, image=bg_photo)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)
    bg_label.image = bg_photo
except:
    # Fallback if image not found
    root.configure(bg="#f0f0f0")

# Main Frame with semi-transparent background
main_frame = tk.Frame(root, bg="#ffffff", bd=2, relief=tk.RIDGE)
main_frame.place(relx=0.5, rely=0.5, anchor="center", width=750, height=750)

# School Logo (replace 'school_logo.png' with your logo path)
try:
    logo_img = Image.open(r"C:\Users\Tab & Tech\Documents\python\practice\voting management\school_logo.png")
    logo_img = logo_img.resize((80, 80), Image.LANCZOS)
    logo_photo = ImageTk.PhotoImage(logo_img)
    logo_label = tk.Label(main_frame, image=logo_photo, bg="#ffffff")
    logo_label.image = logo_photo
    logo_label.grid(row=0, column=0, padx=10, pady=10, sticky="nw")
except:
    pass  # Continue without logo if image not found

# Title
title_frame = tk.Frame(main_frame, bg="#ffffff")
title_frame.grid(row=0, column=1, columnspan=2, sticky="nsew")

tk.Label(title_frame, 
         text="PAK BRITISH VOTING MANAGEMENT SYSTEM", 
         font=("Arial", 18, "bold"), 
         bg="#ffffff", fg="#2c3e50").pack(pady=10)

# Variables
president_var = tk.StringVar()
headboy_var = tk.StringVar()
headgirl_var = tk.StringVar()
yellow_var = tk.StringVar()
red_var = tk.StringVar()
green_var = tk.StringVar()
blue_var = tk.StringVar()
prefect_vars = {cand: tk.IntVar() for cand, _ in candidates["Prefects"]}

# Create Notebook for different categories
notebook = ttk.Notebook(main_frame)
notebook.grid(row=1, column=0, columnspan=3, padx=10, pady=10, sticky="nsew")

# President Tab
pres_tab = tk.Frame(notebook, bg="#ffffff")
notebook.add(pres_tab, text="President")
tk.Label(pres_tab, text="Select President:", font=("Arial", 12, "bold"), bg="#ffffff").pack(pady=5)
for cand, sym in candidates["President"]:
    tk.Radiobutton(pres_tab, text=f"{cand} {sym}", variable=president_var, 
                  value=cand, font=("Arial", 14), bg="#ffffff",
                  indicatoron=0, width=15, height=2).pack(pady=5)

# Head Boy Tab
hb_tab = tk.Frame(notebook, bg="#ffffff")
notebook.add(hb_tab, text="Head Boy")
tk.Label(hb_tab, text="Select Head Boy:", font=("Arial", 12, "bold"), bg="#ffffff").pack(pady=5)
for cand, sym in candidates["Head Boy"]:
    tk.Radiobutton(hb_tab, text=f"{cand} {sym}", variable=headboy_var, 
                  value=cand, font=("Arial", 14), bg="#ffffff",
                  indicatoron=0, width=15, height=2).pack(pady=5)

# Head Girl Tab
hg_tab = tk.Frame(notebook, bg="#ffffff")
notebook.add(hg_tab, text="Head Girl")
tk.Label(hg_tab, text="Select Head Girl:", font=("Arial", 12, "bold"), bg="#ffffff").pack(pady=5)
for cand, sym in candidates["Head Girl"]:
    tk.Radiobutton(hg_tab, text=f"{cand} {sym}", variable=headgirl_var, 
                  value=cand, font=("Arial", 14), bg="#ffffff",
                  indicatoron=0, width=15, height=2).pack(pady=5)

# House Captains Tab
hc_tab = tk.Frame(notebook, bg="#ffffff")
notebook.add(hc_tab, text="House Captains")

hc_notebook = ttk.Notebook(hc_tab)
hc_notebook.pack(expand=True, fill="both")

# Create tabs for each house
for house, cand_list in candidates["House Captains"].items():
    house_tab = tk.Frame(hc_notebook, bg="#ffffff")
    hc_notebook.add(house_tab, text=f"{house} House")
    
    tk.Label(house_tab, text=f"Select {house} House Captain:", 
            font=("Arial", 12, "bold"), bg="#ffffff").pack(pady=5)
    
    var = {"Yellow": yellow_var, "Red": red_var, "Green": green_var, "Blue": blue_var}[house]
    for cand, sym in cand_list:
        tk.Radiobutton(house_tab, text=f"{cand} {sym}", variable=var, 
                      value=cand, font=("Arial", 14), bg="#ffffff",
                      indicatoron=0, width=15, height=2).pack(pady=5)

# Prefects Tab
pf_tab = tk.Frame(notebook, bg="#ffffff")
notebook.add(pf_tab, text="Prefects")
tk.Label(pf_tab, text="Select Prefects (can choose multiple):", 
        font=("Arial", 12, "bold"), bg="#ffffff").pack(pady=5)
for cand, sym in candidates["Prefects"]:
    tk.Checkbutton(pf_tab, text=f"{cand} {sym}", variable=prefect_vars[cand], 
                  font=("Arial", 14), bg="#ffffff", onvalue=1, offvalue=0).pack(pady=5)

# Buttons Frame
buttons_frame = tk.Frame(main_frame, bg="#ffffff")
buttons_frame.grid(row=2, column=0, columnspan=3, pady=20)

tk.Button(buttons_frame, text="Cast Vote", command=cast_vote, 
         bg="#2ecc71", fg="white", font=("Arial", 12, "bold"),
         width=15, height=2).pack(side=tk.LEFT, padx=10)

tk.Button(buttons_frame, text="Show Results", command=show_results, 
         bg="#3498db", fg="white", font=("Arial", 12, "bold"),
         width=15, height=2).pack(side=tk.LEFT, padx=10)

tk.Button(buttons_frame, text="Exit", command=root.quit, 
         bg="#e74c3c", fg="white", font=("Arial", 12, "bold"),
         width=15, height=2).pack(side=tk.LEFT, padx=10)

# Configure grid weights
main_frame.grid_rowconfigure(1, weight=1)
main_frame.grid_columnconfigure(0, weight=1)
main_frame.grid_columnconfigure(1, weight=1)
main_frame.grid_columnconfigure(2, weight=1)

root.mainloop()