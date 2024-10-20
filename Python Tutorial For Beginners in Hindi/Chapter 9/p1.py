with open("poems.txt", "r", encoding="utf-8") as f:
    for line in f:
        if "twinkle" in line.lower():
            print("Found 'twinkle' in the poems.")
