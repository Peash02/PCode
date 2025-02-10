#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <string.h>

#define MAX_WORD_LENGTH 20
#define MAX_GUESSES 6

void drawHangman(int guesses);
void playGame(char *word);

int main() {
    char *words[] = {"apple", "banana", "cherry", "date", "elderberry"};
    int wordCount = sizeof(words) / sizeof(words[0]);
    srand(time(NULL));
    int randomIndex = rand() % wordCount;
    playGame(words[randomIndex]);
    return 0;
}

void playGame(char *word) {
    int wordLength = strlen(word);
    char guessedWord[wordLength + 1];
    for (int i = 0; i < wordLength; i++) {
        guessedWord[i] = '_';
    }
    guessedWord[wordLength] = '\0';
    int guesses = 0;
    while (guesses < MAX_GUESSES) {
        printf("%s\n", guessedWord);
        char guess;
        printf("Guess a letter: ");
        scanf(" %c", &guess);
        int correctGuess = 0;
        for (int i = 0; i < wordLength; i++) {
            if (word[i] == guess) {
                guessedWord[i] = guess;
                correctGuess = 1;
            }
        }
        if (!correctGuess) {
            guesses++;
            drawHangman(guesses);
        }
        if (strcmp(guessedWord, word) == 0) {
            printf("Congratulations! You guessed the word: %s\n", word);
            return;
        }
    }
    printf("Game over! The word was: %s\n", word);
}

void drawHangman(int guesses) {
    switch (guesses) {
        case 1:
            printf("   +---+\n");
            printf("   |   |\n");
            printf("       |\n");
            printf("       |\n");
            printf("       |\n");
            printf("       |\n");
            break;
        case 2:
            printf("   +---+\n");
            printf("   |   |\n");
            printf("   O   |\n");
            printf("       |\n");
            printf("       |\n");
            printf("       |\n");
            break;
        case 3:
            printf("   +---+\n");
            printf("   |   |\n");
            printf("   O   |\n");
            printf("   |   |\n");
            printf("       |\n");
            printf("       |\n");
            break;
        case 4:
            printf("   +---+\n");
            printf("   |   |\n");
            printf("   O   |\n");
            printf("  /|   |\n");
            printf("       |\n");
            printf("       |\n");
            break;
        case 5:
            printf("   +---+\n");
            printf("   |   |\n");
            printf("   O   |\n");
            printf("  /|\\  |\n");
            printf("       |\n");
            printf("       |\n");
            break;
        case 6:
            printf("   +---+\n");
            printf("   |   |\n");
            printf("   O   |\n");
            printf("  /|\\  |\n");
            printf("  /    |\n");
            printf("       |\n");
            break;
    }
}
