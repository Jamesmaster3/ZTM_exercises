from translate import Translator

try:
    with open("Excercises\docs\\translate.txt", mode='r') as my_file:
        # mode= w creates a file, mode=a appends a file
        contents = my_file.read()
        my_file.close()

        file_translate = Translator(to_lang='ja')

        result = file_translate.translate(contents)

        with open("Excercises\docs\\translated_to_japanese.txt", mode='w', encoding="utf-8") as new_file:
            new_file.write(result)
            new_file.close()

except FileNotFoundError as err:
    print('File does not exist')
    # raise err
