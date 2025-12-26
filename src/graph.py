import csv
import os
import matplotlib.pyplot as plt
from dotenv import load_dotenv

load_dotenv()

file_path = os.getenv("OPINION_VARIANCE_CSV")

if file_path is None:
    raise ValueError(
        "OPINION_VARIANCE_CSV not found in .env file"
    )


MAX_TIME = 28000    
Y_MIN = 0.0
Y_MAX = 0.1        


x = []
y = []

with open(file_path, newline='', encoding='utf-8') as f:
    reader = csv.reader(f)
    read_data = False

    for row in reader:
        # NetLogo header starts after 'x'
        if row and row[0] == 'x':
            read_data = True
            continue

        if read_data and len(row) >= 2:
            try:
                xi = float(row[0])
                yi = float(row[1])

                if xi <= MAX_TIME:
                    x.append(xi)
                    y.append(yi)

            except ValueError:
                pass


plt.figure(figsize=(6, 4))
plt.plot(x, y, linewidth=2)

plt.xlabel("time")
plt.ylabel("variance")

plt.xlim(0, MAX_TIME)
plt.ylim(Y_MIN, Y_MAX)

plt.tight_layout()
plt.show()

input("Press Enter to close the window...")
