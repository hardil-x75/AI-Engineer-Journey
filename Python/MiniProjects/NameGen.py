import random

prefixes = ["Dark", "Cyber", "Neo", "Shadow", "Silent", "Quantum"]
suffixes = ["Wolf", "Blade", "Storm", "Strike", "Flame", "Ghost"]

num = int(input("How many beast names to generate? "))

for _ in range(num):
    pre = random.choice(prefixes)
    suf = random.choice(suffixes)
    print(f"{pre}{suf}")
