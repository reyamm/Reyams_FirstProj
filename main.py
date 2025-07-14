import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file
df = pd.read_csv("data.csv")

print(" Welcome to the Education Resources Customizer!")
print("Available Subjects:", df['Subject'].unique())

subject = input("Enter a subject: ").strip()
difficulty = input("Enter difficulty level (Beginner, Intermediate, Advanced): ").strip()

# Filter the data
filtered = df[
    (df['Subject'].str.lower() == subject.lower()) &
    (df['Difficulty'].str.lower() == difficulty.lower())
]

if filtered.empty:
    print("No resources found for your selection.")
else:
    print(f"\n📚 Resources for {subject.title()} ({difficulty.title()}):")
    for idx, row in filtered.iterrows():
        print(f"- {row['Title']} | {row['Type']} | {row['Duration']} | {row['Link']}")

# Optional: Visualize resources per subject
plt.figure(figsize=(8, 6))
df['Subject'].value_counts().plot(kind='bar', color='skyblue')
plt.title("Number of Resources per Subject")
plt.ylabel("Count")
plt.xlabel("Subject")
plt.tight_layout()
plt.show()