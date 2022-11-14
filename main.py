# Morse Code Alphabet as a dictionary for easy conversion.
key = {
    "a": ".-", "b": "-...", "c": "-.-.", "d": "-..", "e": ".", "f": "..-.", "g": "--.", "h": "....", "i": "..",
    "j": ".---", "k": "-.-", "l": ".-..", "m": "--", "n": "-.", "o": "---", "p": ".--.", "q": "--.-", "r": ".-.",
    "s": "...", "t": "-", "u": "..-", "v": "...-", "w": ".--", "x": "-..-", "y": "-.--", "z": "--..", "1": ".----",
    "2": "..---", "3": "...--", "4": "....-", "5": "......", "6": "-....", "7": "--...", "8": "---..", "9": "----.",
    "0": "-----", " ": " ", "  ": "  "
}
# Obtain input from user.
text = input("Type what you want converted here (Do not use symbols or emojis)--> ")
# Simple way to keep the original input and feed it back to the user with the converted text.
original_text = text
# List comprehension to create a new list with the converted text.
morse_code_text = [key[n] for n in text.lower()]
# Output for user will show their original input and the converted text.
print(f"Your input: {original_text}\nConverted to Morse Code: {morse_code_text}")
