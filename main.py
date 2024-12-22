def main():
    location_of_book_file = "books/frankenstein.txt"
    text = get_book_text(location_of_book_file)
    word_count = count_words(text)
    char_num = count_characters(text)
    rep = gen_report(location_of_book_file,word_count,sort_on(char_num))

    print(rep)

def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
        return file_contents


def count_words(text):
    count = len(text.split())
    return count


def count_characters(text):
    list_of_chars = {}
    text = text.lower()
    for char in text:
        if char.isalpha():
            if char in list_of_chars:
                list_of_chars[char] += 1
            else:
                list_of_chars[char] = 1
    
    return list_of_chars

def sort_on(d):
    return dict(sorted(d.items(), key=lambda item: item[1], reverse=True))

def gen_space(line):
    width = 64
    line_len = len(line)
    if line_len == 1:
        new_line = f"\n#{line * (width-3)}#"
    else:
        space = (width - line_len) - 8
        new_line = f"\n# -- {line} {'-' * space}#"
    return new_line

def gen_report(loc,word_num, char_num):
    
    block_of_report = gen_space(f"#")
    #some buetifyer
    block_of_report += gen_space(f"Report of [[{loc}]]")
    block_of_report += gen_space(f"#")
    block_of_report += gen_space(f"I have identified {word_num} words in the book file")
    block_of_report += gen_space(f"#")
    for item in char_num:
        block_of_report += gen_space(f"Character [{item}] was found {char_num[item]} times")
    block_of_report += gen_space(f"#")
    block_of_report += gen_space(f"End of report")
    block_of_report += gen_space(f"#")

    return block_of_report
main()