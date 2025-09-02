import csv

# ------------------- SAME CANDIDATES + INITIALIZATION -------------------
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


# ------------------- FUNCTIONS -------------------
def show_candidates():
    print("\n--- Candidates List ---")
    for category in ["President", "Head Boy", "Head Girl"]:
        print(f"\n{category}:")
        for i, (cand, sym) in enumerate(candidates[category], start=1):
            print(f"{i}. {cand} {sym}")

    print("\nHouse Captains:")
    for house in candidates["House Captains"]:
        print(f"\n{house} House:")
        for i, (cand, sym) in enumerate(candidates["House Captains"][house], start=1):
            print(f"{i}. {cand} {sym}")

    print("\nPrefects (you can choose multiple):")
    for i, (cand, sym) in enumerate(candidates["Prefects"], start=1):
        print(f"{i}. {cand} {sym}")


def voting():
    print("\n===== START VOTING =====")
    # President
    choice = int(input("\nVote for President (enter number): "))
    pres = candidates["President"][choice-1][0]
    votes["President"][pres] += 1

    # Head Boy
    choice = int(input("\nVote for Head Boy (enter number): "))
    hb = candidates["Head Boy"][choice-1][0]
    votes["Head Boy"][hb] += 1

    # Head Girl
    choice = int(input("\nVote for Head Girl (enter number): "))
    hg = candidates["Head Girl"][choice-1][0]
    votes["Head Girl"][hg] += 1

    # House Captains
    for house in candidates["House Captains"]:
        print(f"\nVote for {house} House Captain:")
        choice = int(input("Enter number: "))
        hc = candidates["House Captains"][house][choice-1][0]
        votes["House Captains"][house][hc] += 1

    # Prefects
    print("\nVote for Prefects (you can select multiple, separated by commas):")
    choices = input("Enter numbers: ").split(",")
    for ch in choices:
        if ch.strip().isdigit():
            idx = int(ch.strip())-1
            if 0 <= idx < len(candidates["Prefects"]):
                pf = candidates["Prefects"][idx][0]
                votes["Prefects"][pf] += 1

    print("\n✅ Vote Recorded Successfully!")


def save_results_csv(filename="election_results.csv"):
    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Category", "Candidate", "Votes"])

        # Single categories
        for category in ["President", "Head Boy", "Head Girl"]:
            for cand, v in votes[category].items():
                writer.writerow([category, cand, v])

        # House captains
        for house in votes["House Captains"]:
            for cand, v in votes["House Captains"][house].items():
                writer.writerow([f"{house} House Captain", cand, v])

        # Prefects
        for cand, v in votes["Prefects"].items():
            writer.writerow(["Prefect", cand, v])

    print(f"\n📂 Results saved to '{filename}' (open in Excel).")


def show_results():
    print("\n===== FINAL RESULTS =====")
    for category in ["President", "Head Boy", "Head Girl"]:
        print(f"\n{category} Results:")
        for cand, v in votes[category].items():
            print(f"{cand}: {v} votes")
        winner = max(votes[category], key=votes[category].get)
        print(f"🏆 Winner: {winner}")

    print("\nHouse Captains Results:")
    for house in votes["House Captains"]:
        print(f"\n{house} House:")
        for cand, v in votes["House Captains"][house].items():
            print(f"{cand}: {v} votes")
        winner = max(votes["House Captains"][house], key=votes["House Captains"][house].get)
        print(f"🏆 Winner: {winner}")

    print("\nPrefects Results (multiple can win):")
    for cand, v in votes["Prefects"].items():
        print(f"{cand}: {v} votes")

    # Save to CSV automatically
    save_results_csv()


# ------------------- MAIN PROGRAM -------------------
while True:
    print("\n====== SCHOOL ELECTION SYSTEM ======")
    print("1. Show Candidates")
    print("2. Cast Vote")
    print("3. Show Results (and Save to Excel)")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        show_candidates()
    elif choice == "2":
        voting()
    elif choice == "3":
        show_results()
    elif choice == "4":
        print("Exiting... Thank you!")
        break
    else:
        print("Invalid choice! Try again.")
