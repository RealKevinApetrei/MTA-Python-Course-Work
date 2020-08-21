import os


def make_csv(word_count, filename):
    with open(filename, "w") as f:
        for key, value in word_count.items():
            row = "{},{}\n".format(key, value)
            f.write(row)


def get_file_info(filename, search_words):
    result = {}

    with open(filename, "r") as f:
        text = f.read()
        text = text.split(" ")
        for word in text:
            if word in search_words:
                if word in result:
                    result[word] += 1
                else:
                    result[word] = 1

    return result


if __name__ == "__main__":
    for text_file in os.listdir("text"):
        search_words = ["Frankenstein", "monster", "afraid", "the"]
        word_count = get_file_info("text/{}".format(text_file), search_words)
        new_filename = text_file.split(".")[0]
        make_csv(word_count, "{}_analysis.csv".format(new_filename))
