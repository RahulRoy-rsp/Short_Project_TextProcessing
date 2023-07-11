import json
import string

# creating a class for text Processing
class TextProcessing():

    def __init__(self, file_path):
        self.file_path = file_path

    # function for reading text file        
    def read_file(self):
        with open(self.file_path, 'r') as f:
            text = f.read()
        return text

    # function for counting total number of words in the text file
    def countTotalWords(self):
        text = self.read_file()
        words = text.split()
        return len(words)

    # function for counting total number of unique words in the text file
    def countUniqueWords(self):
        text = self.read_file()
        words = text.split()
        unique_words = set(words)
        return len(unique_words)

    # function for counting occurrences of word in the text file
    def wordCountDict(self):
        text = self.read_file()
        words = text.split()
        word_count_dict = {}
        for word in words:
            if word in word_count_dict:
                word_count_dict[word] += 1
            else:
                word_count_dict[word] = 1
        return word_count_dict

    # function for lowering the characters & then counting occurrences of word in the text file        
    def lowerCaseWordCountDict(self):
        text = self.read_file()
        words = text.split()
        lower_case_words = [word.lower() for word in words]
        lower_case_word_count_dict = {}
        for word in lower_case_words:
            if word in lower_case_word_count_dict:
                lower_case_word_count_dict[word] += 1
            else:
                lower_case_word_count_dict[word] = 1
        return lower_case_word_count_dict

    # function for savinf dictionary into a json file
    def save_to_json(self, data, file_path):
        with open(file_path, 'w') as f:
            json.dump(data, f)

    # function for removing whitespaces
    def removeWhitespaces(self):
        text = self.read_file()
        text = ' '.join(text.split())
        return text

    # function for removing special characters
    def removeSpecialCharacters(self):
        text = self.read_file()
        text = ' '.join(text.split())
        text = text.translate(str.maketrans('', '', string.punctuation))
        return text
            
# 1. Reading the text file
# creating an object for the class
textProcessor = TextProcessing('t8.shakespeare.txt')

# 2. Finding number of unique words
uniqueWords = textProcessor.countUniqueWords()
print(f"Total Number of unique words in text file is {uniqueWords}")

# 3. Counting total words
totalWords = textProcessor.countTotalWords()
print(f"Total Number of words in text file is {totalWords}")

# 4. Creating a dictionary which contains the count of each word and saving the result to a json file.
wordCounts = textProcessor.wordCountDict()
textProcessor.save_to_json(wordCounts, 'wordCount.json')

# 5. Convert words to lower case and count each word occurrence and saving the result to a json file.
lowerCaseWordCounts = textProcessor.lowerCaseWordCountDict()
textProcessor.save_to_json(lowerCaseWordCounts, 'lowerCaseWordCount.json')

# 6. Removing additional whitespace
textWithoutWhitespaces = textProcessor.removeWhitespaces()

# 7. Removing special characters from the text files.
textWithoutSpec_Char_ = textProcessor.removeSpecialCharacters()

#8. Saving output to a new text file.
with open('cleaned.txt', 'w') as f:
    f.write(textWithoutSpec_Char_)
