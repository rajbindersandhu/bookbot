from report import generate_report

def main():
    with open("Books/frankenstein.txt") as f:
        file_data = f.read()
    word_list = file_data.split()
    word_count = len(word_list)
    letter_count_dict = letter_count_for(file_data)
    generate_report(word_count, letter_count_dict)
    

def letter_count_for(text_string: str) -> str:
    if(type(text_string) == str):
        count_dict = {}
        for char in text_string:
            if(char.isalpha()):
                if char in count_dict:
                    count_dict[char] +=1
                else:
                    count_dict[char] = 1
    else:
        raise Exception("Please provide a string...")
    return count_dict
    


main()