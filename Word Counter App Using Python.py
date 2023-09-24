file_path = "input.txt"

search_word = ["Python", "C", "OOP", "Hello", "Java","C++"]
search_words = [x.lower() for x in search_word]


def count_words_in_file(file_path, search_words):

    word_count = {word: 0 for word in search_words}

    with open(file_path, 'r') as file:

        for line in file:
            words = line.lower().strip().split()
            for word in words:
                if word in word_count:
                    word_count[word] += 1

    for word, count in word_count.items():
        print(f'{word} -> {count}')

count_words_in_file(file_path, search_words)
