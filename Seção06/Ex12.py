import string
import unicodedata

def count_letters(text):
    letter_counts = {letter: 0 for letter in string.ascii_lowercase}

    for char in text:
        normalized_char = unicodedata.normalize('NFKD', char).encode('ASCII', 'ignore').decode('utf-8').lower()
        if normalized_char in letter_counts:
            letter_counts[normalized_char] += 1

    return letter_counts

def main():
    file_path = input("Enter the path of the text file: ")

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()

            # Counting characters, lines, and words
            num_characters = len(content)
            num_lines = content.count('\n') + 1
            num_words = len(content.split())

            # Counting occurrences of each letter
            letter_counts = count_letters(content)

            # Displaying the results
            print(f"Number of characters: {num_characters}")
            print(f"Number of lines: {num_lines}")
            print(f"Number of words: {num_words}")
            print("Occurrences of each letter:")
            for letter, count in letter_counts.items():
                print(f"{letter}: {count}")

    except FileNotFoundError:
        print("File not found. Please check the path and try again.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
