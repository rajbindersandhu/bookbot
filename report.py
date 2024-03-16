def generate_report(total_word_count, letter_count_dict: dict) -> None:
    print(f"""--- Begin report of books/frankenstein.txt ---
{total_word_count} words found in the document
          \n""")
    for key, value in letter_count_dict.items():
        print(f"The '{key}' character was found {value} times")
    print("--- End report ---")
