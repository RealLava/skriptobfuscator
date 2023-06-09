# Skript Obfuscator
import random
import string

def obfuscate_skript(skript_code):
    lines = skript_code.split('\n')
    obfuscated_lines = []
    variable_mapping = {}
    for line in lines:
        obfuscated_line = ''
        words = line.split(' ')
        for word in words:
            if word.startswith('{'):
                variable_name = word[1:]
                if variable_name not in variable_mapping:
                    obfuscated_name = obfuscate_word(variable_name)
                    variable_mapping[variable_name] = obfuscated_name
                obfuscated_line += '{' + variable_mapping[variable_name] + ' '
            else:
                obfuscated_line += word + ' '

        obfuscated_lines.append(obfuscated_line)

    obfuscated_code = '\n'.join(obfuscated_lines)
    return obfuscated_code

def obfuscate_skript2(skript_code):
    lines = skript_code.split('\n')
    obfuscated_lines = []
    for line in lines:
        obfuscated_line = ''
        if random.random() < 0.5:
            obfuscated_line += generate_useless_comment() + '\n'
        obfuscated_line += line
        obfuscated_lines.append(obfuscated_line)
    obfuscated_code = '\n'.join(obfuscated_lines)
    return obfuscated_code

def generate_useless_comment():
    comment = '# ' + ''.join(random.choices(string.ascii_lowercase, k=random.randint(5, 10)))
    return comment

def obfuscate_word(word):
    obfuscated_word = ''
    for char in word:
        if char.isalpha():
            obfuscated_word += random.choice('abcdefghijklmnopqrstuvwxyz')
        else:
            obfuscated_word += char
    return obfuscated_word

skript_code = ""
line = input("Enter the skript code (type END to finish)\n")
while line.strip() != "END":
    skript_code += line + "\n"
    line = input()

obfuscated_code = obfuscate_skript(skript_code)
obfuscated_skript = obfuscate_skript2(obfuscated_code)
print(obfuscated_skript)
input("Press enter to exit..")
