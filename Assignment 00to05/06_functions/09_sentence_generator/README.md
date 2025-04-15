📝 Sentence Generator 📖
📌 Overview
This program takes a word from the user and categorizes it as a noun, verb, or adjective, then generates a sentence accordingly.

🛠 How It Works?
make_sentence(word, part_of_speech)
This function takes two inputs: a word and a part_of_speech. It creates a sentence depending on the value of part_of_speech:

0: Noun — "I am excited to add this [word] to my vast collection of them!"

1: Verb — "It's so nice outside today it makes me want to [word]!"

2: Adjective — "Looking out my window, the sky is big and [word]!"

If the part_of_speech is invalid (anything other than 0, 1, or 2), it prints an error message.

main()

Takes a word from the user (could be a noun, verb, or adjective).

Prompts the user to specify the part of speech by typing 0, 1, or 2.

Calls make_sentence() with the word and part_of_speech.

🔍 Example Run
Input:

Please type a noun, verb, or adjective: sky
Is this a noun, verb, or adjective?
Type 0 for noun, 1 for verb, 2 for adjective: 2
Output:

Looking out my window, the sky is big and sky!