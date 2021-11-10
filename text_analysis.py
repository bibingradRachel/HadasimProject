import re

from colour import Color


# check if the word is color
def check_color(word):
    if word == '':
        return False
    try:
        Color(word)
        return True
    except ValueError:
        return False


def text_analysis(path_read_file, path_write_file):
    lines = []
    counter_words = 0  # מספר המילים
    max_len_line = 0  # אורך השורה המקסימלית
    sum_len_lines = 0  # סכום אורכי כול השורות לצורך הממוצע
    counter_unique_words = 0  # מספר מילים ייחודיות בקטע
    len_max_seq_without_k = 0  # אורך הקטע הארוך ביותר ללא K
    seq_without_k = ""  # אורך הקטע  ללא K
    longest_seq_without_k = ""  # הקטע הארוך ביותר ללא K
    max_num = 0 # מספר מקסימלי
    words = {}
    colors = {}
    numbers = {'one':'1','two':'2','three':'3','four':'4','five':'5','six':'6','seven':'7','eight':'8','nine':'9', 'ten':'10',
               'eleven':'11','twelve':'12','thirteen':'13', 'fourteen':'14', 'fifteen':'15','sixteen':'16',
               'seventeen':'17', 'eighteen':'18', 'nineteen': '19'}
    tens = {'twenty':'20','thirty':'30','forty':'40','fifty':'50','sixty':'60','seventy':'70','eighty':'80','ninety':'90'}
    scales = {"hundred":'00', "thousand":'000', "million":'000000', "billion":'00000000', "trillion":'0000000000'}

    max_num_now = 0

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

        # sum of all length lines
        sum_len_lines += len_line

        for i,word in enumerate(line):
            word = word.lower()
            # Removes characters from the word
            word = re.sub(r'[^\w]', '', word)

            # add the word to dict words
            if word in words:
                words[word] += 1
            else:
                words[word] = 1

            # find the longest sequence without k
            if 'k' in word:
                if len(seq_without_k) > len(longest_seq_without_k):
                    # len_max_seq_without_k = len(seq_without_k)
                    longest_seq_without_k = seq_without_k

                seq_without_k = ""
            else:
                seq_without_k = seq_without_k + " " + word
                # len_max_seq_without_k += 1

            # count the colors in the text
            if check_color(word):
                if word in colors:
                    colors[word] += 1
                else:
                    colors[word] = 1

            # check if the word is number
            if word.isdigit():
                if int(word) > max_num:
                    max_num = int(word)

            if word in numbers:
                # will check the next word if it number
                if i < len(line)-1:
                    line[i + 1] = line[i + 1].lower()
                    line[i + 1] = re.sub(r'[^\w]', '', line[i + 1])
                    if line[i + 1] in scales:
                        sum = numbers[word] + scales[line[i+1]]
                        max_num_now += int(sum)
                    else:
                        max_num_now += int(numbers[word])
                else:
                    max_num_now += int(numbers[word])

            elif word in tens:
                # will check the next word -> line[i+1]
                if i < len(line)-1:
                    line[i+1] = line[i+1].lower()
                    line[i+1] = re.sub(r'[^\w]', '', line[i+1])
                    if line[i+1] in numbers:
                        max_num_now += str(int(tens[word])//10)
                    elif line[i+1] in scales:
                        sum = tens[word] + scales[line[i + 1]]
                        max_num_now += int(sum)
                    else:
                        max_num_now += int(tens[word])
                else:
                    max_num_now += int(tens[word])

            elif word not in scales  and max_num_now > 0:
                if int(max_num_now) > max_num:
                    max_num = int(max_num_now)
                max_num_now = 0



    # k doesnt appear at all
    if len(longest_seq_without_k) == 0:
        longest_seq_without_k = seq_without_k

    counter_unique_words = list(words.values()).count(1)

    with open(path_write_file, 'w', encoding='utf-8') as f:

        f.write("כמות השורות בקובץ:  " + str(len(lines)))
        f.write('\n')
        f.write("כמות המילים בקובץ:  " + str(counter_words))
        f.write('\n')
        f.write("אורך השורה המקסימלית:  " + str(max_len_line))
        f.write('\n')
        f.write("אורך השורה הממוצע:  " + str(sum_len_lines / len(lines)))
        f.write('\n')
        f.write("מספר מילים יחודיות:  " + str(counter_unique_words))
        f.write('\n')
        f.write("רצף המילים הארוך ביותר ללא קיי:"  )
        f.write('\n')
        f.write(str(longest_seq_without_k))
        f.write('\n')
        f.write("שמות הצבעים בטקסט וכמה פעמים מופיע כול אחד:  " + str(colors))
        f.write('\n')
        f.write("המספר הגדול ביותר בטקסט:  " + str(max_num))


if __name__ == "__main__":
    path_read_file = 'random_file'
    path_write_file = 'result_file.txt'
    text_analysis(path_read_file, path_write_file)
