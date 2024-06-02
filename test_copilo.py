def compute_letter_frequencies(text):
    frequencies = {}
    total_letters = 0
    for char in text.lower():
        if char.isalpha():
            frequencies[char] = frequencies.get(char, 0) + 1
            total_letters += 1
    for char, count in frequencies.items():
        frequencies[char] = count / total_letters
    return frequencies

# Exemple d'utilisation :
french_reference = {'a': 0.084, 'b': 0.009}  # Fréquences de lettres en français
english_reference = {'a': 0.081, 'b': 0.015}  # Fréquences de lettres en anglais

text_to_check = "Bonjour tout le monde !"  # Votre texte à analyser
frequencies = compute_letter_frequencies(text_to_check)




similarity_french = sum(min(frequencies.get(char, 0), french_reference.get(char, 0)) for char in french_reference)
similarity_english = sum(min(frequencies.get(char, 0), english_reference.get(char, 0)) for char in english_reference)

if similarity_french > similarity_english:
    print("Le texte est probablement en français.")
else:
    print("Le texte est probablement en anglais.")