import re
from colour import Color

def check_color(word):
    if word == '':
        return False
    try:
        Color(word)
        return True
    except ValueError:
        return False

def text_analysis(path_read_file, path_write_file):
    lines =[]
    counter_words = 0 #מספר המילים
    max_len_line = 0 # אורך השורה המקסימלית
    sum_len_lines =0  #סכום אורכי כול השורות לצורך הממוצע
    counter_unique_words = 0  #  מספר מילים ייחודיות בקטע
    len_max_seq_without_k = 0 #אורך הקטע הארוך ביותר ללא K
    seq_without_k = "" # אורך הקטע  ללא K
    longest_seq_without_k = "" #  הקטע הארוך ביותר ללא K
    words = {}
    colors = {}

    with open(path_read_file, 'r') as f:
        # read the file into lines
        lines = f.readlines()

    for line in lines:
        # cut the \n from the string
        line = line[:-2]
        # convert string to array and count the words
        line = list(line.split(" "))
        len_line = len(line)
        counter_words += len_line

        # find the line with the maximum length
        if len_line > max_len_line:
            max_len_line = len_line

        # sumof all length lines
        sum_len_lines += len_line


        for word in line:
            word = word.lower()
            # Removes characters from the word
            word =re.sub(r'[^\w]', '', word)

            # add the word to dict words
            if word in words:
                words[word] += 1
            else:
                words[word] = 1

            # find the longest sequence without k
            if 'k' in word:
                if len(seq_without_k) > len_max_seq_without_k:
                    len_max_seq_without_k = len(seq_without_k)
                    longest_seq_without_k = seq_without_k

                seq_without_k  = ""
            else:
                seq_without_k = seq_without_k+ " " + word
                len_max_seq_without_k += 1

            # count the colors in the text
            if check_color(str(word)):
                if word in colors:
                    colors[word] += 1
                else:
                    colors[word] = 1

    # k doesnt appear at all
    if len(longest_seq_without_k) == 0:
        longest_seq_without_k = seq_without_k


    counter_unique_words = list(words.values()).count(1)

    with open(path_write_file, 'w',encoding='utf-8') as f:

        f.write("כמות השורות בקובץ:  "+str(len(lines)))
        f.write('\n')
        f.write("כמות המילים בקובץ:  "+ str(counter_words))
        f.write('\n')
        f.write("אורך השורה המקסימלית:  "+str(max_len_line))
        f.write('\n')
        f.write("אורך השורה הממוצע:  "+str(sum_len_lines / len(lines)))
        f.write('\n')
        f.write("מספר מילים יחודיות:  " + str(counter_unique_words))
        f.write('\n')
        f.write("רצף המילים הארוך ביותר ללא קיי:  " + str(longest_seq_without_k))
        f.write('\n')
        f.write("שמות הצבעים בטקסט וכמה פעמים מופיע כול אחד:  "+str(colors) )



text_analysis('random_file','result_file.txt')












