translation = {
    "Ghuroor":"Pride",
    "Tasawwur":"Imagination",
    "Harkat":"Movement",
    "Virtues":"Fazaail",
    "Aarzoo":"Desire",
    "Construction":"Taameer",
}

words = input("Gimme some words to tell you or u gae: ")

answer = translation.get(words)

print(f"The meaing of the word '{words}' is {answer}")