# 🔤Romanian-English Flashcard App

This is a flashcard application built with Tkinter, designed to help users learn Romanian vocabulary. The app presents a Romanian word, waits for the user to memorize it, and then flips the card to reveal its English translation. Users can mark words they know, ensuring a personalized and focused learning experience.

# Features:
- Interactive Flashcards: Presents a Romanian word on the front of the card and flips to show the English translation after 3 seconds.
- Word Tracking: Keeps track of words you know and removes them from future practice sessions.
- Progress Saving: Saves your learning progress to a words_to_learn.csv file for seamless resumption.
- Customizable Vocabulary: Loads vocabulary from a romanian_words.csv file, allowing easy updates to the word list.
- Visual Appeal: A visually engaging interface with front and back card designs.

# How It Works:
- Word Display: Each card starts by showing a Romanian word on the front.
- Translation Flip: After 3 seconds, the card flips to display the English translation.
- Mark as Known: Click the checkmark button if you know the word to remove it from the list.
- Next Word: Click the cross button to skip to the next word.
- Data Persistence: Known words are removed from the learning list and saved for future sessions.

# Tech Stack:
- Tkinter: For building the graphical user interface.
- Pandas: To manage and save the vocabulary data.
- Random Module: To select random words for flashcards.

# How to Run:
- Clone or download the repository containing the project files.
- Ensure the following files are in the correct directories:
- data/romanian_words.csv: Contains the vocabulary data.
- data/words_to_learn.csv: Automatically created to save progress.
- images/card_front.png: Image for the front of the card.
- images/card_back.png: Image for the back of the card.
- images/wrong.png and images/right.png: Button images.
- Install required dependencies if needed (pandas library).
- Run the script using Python (python main.py).

Start learning Romanian with interactive flashcards!
This flashcard app makes language learning engaging and efficient by combining a clean interface with smart tracking of your progress. 🌍📚
