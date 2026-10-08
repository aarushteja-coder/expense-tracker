import csv
import os

FILE = "expenses.csv"


def load():
  if not os.path.exists(FILE):
    return []
  with open(FILE, "r", newline="") as f:
    return list(csv.DictReader(f))


def save(exps):
  with open(FILE, "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=["category", "amount"])
    w.writeheader()
    w.writerows(exps)


def main():
  exps = load()
  while True:
    print("\n1. Add  2. View  3. Summary  4. Exit")
    choice = input("Choice: ").strip()

    if choice == "1":
      cat = input("Category: ").strip()
      try:
        amt = float(input("Amount ($): "))
        exps.append({"category": cat, "amount": f"{amt:.2f}"})
        save(exps)
        print("Saved!")
      except ValueError:
        print("Invalid amount.")

    elif choice == "2":
      print("\n--- Expenses ---")
      for e in exps:
        print(f"{e['category']}: ${e['amount']}")

    elif choice == "3":
      totals = {}
      for e in exps:
        totals[e["category"]] = totals.get(e["category"], 0) + float(e["amount"])
      print("\n--- Summary ---")
      for cat, total in totals.items():
        print(f"{cat}: ${total:.2f}")

    elif choice == "4":
      break


if __name__ == "__main__":
  main()