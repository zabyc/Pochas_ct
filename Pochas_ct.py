# Encryption file

from time import localtime
import random
from string import ascii_lowercase, ascii_uppercase, digits ,punctuation
import sys

def _exit() -> None:
    sys.exit()

class Encrypt:

    def __init__(self,target_file_path,consider_spaces=True,key=None,exit_file_path='encrypted_file.txt',use_larger_char_list=False):
        '''If you use a key it must be from plain to cipher'''
        self.target = target_file_path
        self.consider_spaces = consider_spaces
        self.exit_file_path = exit_file_path
        self.use_larger_char_list = use_larger_char_list
        with open(target_file_path,'r') as f:
            self.plain_text = f.read()
        if isinstance(key,dict) and len(key.values()) >= 26:
            self.p_c_key = key
        elif key == None:
            self.p_c_key = self.__new_key()
        else:
            print('Key must be either None or a dict with more than 26 values')
            _exit()
        self.c_p_key = {c:p for p,c in self.p_c_key.items()}
        self.cipher_text = self.__encrypt()

    def __str__(self):
        return self.cipher_text

    def __iter__(self):
        return iter(self.cipher_text)

    def __new_key(self):
        characters = list(ascii_lowercase) if not self.use_larger_char_list else list(ascii_lowercase+punctuation+digits)
        if self.consider_spaces:
            characters.append(' ')
        key_list = random.sample(characters,len(characters))
        key = dict()
        for c_letter, p_letter in zip(key_list, characters):
            key[p_letter] = c_letter
        return key

    def __encrypt(self) -> None:
        plain_text = self.plain_text
        key = self.p_c_key
        characters = tuple(set(plain_text))
        cipher_text = ''
        print('Encrypting...')
        if self.consider_spaces:
            for letter in plain_text:
                if letter == '\n':
                    cipher_text += '\n'
                else:
                    cipher_text += key[letter]
        elif not self.consider_spaces:
            for letter in plain_text:
                if letter == ' ':
                    cipher_text += ' '
                elif letter == '\n':
                    cipher_text += '\n'
                else:
                    cipher_text += key[letter]
        with open(self.exit_file_path,'w+') as f:
            f.write(cipher_text)
        print('Encrypted')
            

class Decrypt:
    import json
    
    with open(r'words.json','r') as f:
        raw_data = str(f.read())
        words = json.loads(raw_data)
    

    frequency_letters_considering_spaces_v1 = { 
        'a': 0.07,
        'b': 0.013,
        'c': 0.028,
        'd': 0.032,
        'e': 0.103,
        'f': 0.018,
        'g': 0.017,
        'h': 0.041,
        'i': 0.065,
        'j': 0.002,
        'k': 0.006,
        'l': 0.036,
        'm': 0.022,
        'n': 0.061,
        'o': 0.064,
        'p': 0.018,
        'q': 0.001,
        'r': 0.051,
        's': 0.057,
        't': 0.08,
        'u': 0.026,
        'v': 0.009,
        'w': 0.015,
        'x': 0.002,
        'y': 0.017,
        'z': 0.001,
        ' ': 0.145,
    }

    frequency_letters_considering_spaces_v2 = {
        'a': 0.067, 
        'b': 0.013, 
        'c': 0.027, 
        'd': 0.03, 
        'e': 0.099, 
        'f': 0.018, 
        'g': 0.017, 
        'h': 0.04, 
        'i': 0.062, 
        'j': 0.001, 
        'k': 0.006, 
        'l': 0.034, 
        'm': 0.021, 
        'n': 0.059, 
        'o': 0.062, 
        'p': 0.018, 
        'q': 0.001, 
        'r': 0.049, 
        's': 0.054, 
        't': 0.077, 
        'u': 0.025, 
        'v': 0.009, 
        'w': 0.014, 
        'x': 0.002, 
        'y': 0.016, 
        'z': 0.001, 
        ' ': 0.139, 
        '!': 0.001, 
        '"': 0.001, 
        '#': 0.001, 
        '$': 0.001, 
        '%': 0.001, 
        '&': 0.001, 
        "'": 0.001, 
        '(': 0.001, 
        ')': 0.001, 
        '*': 0.001, 
        '+': 0.001, 
        ',': 0.001, 
        '-': 0.001, 
        '.': 0.001, 
        '/': 0.001, 
        ':': 0.001, 
        ';': 0.001, 
        '<': 0.001, 
        '=': 0.001, 
        '>': 0.001, 
        '?': 0.001, 
        '@': 0.001, 
        '[': 0.001, 
        '\\': 0.001, 
        ']': 0.001, 
        '^': 0.001, 
        '_': 0.001, 
        '`': 0.001, 
        '{': 0.001, 
        '|': 0.001, 
        '}': 0.001, 
        '~': 0.001, 
        '0': 0.001, 
        '1': 0.001, 
        '2': 0.001, 
        '3': 0.001, 
        '4': 0.001, 
        '5': 0.001, 
        '6': 0.001, 
        '7': 0.001, 
        '8': 0.001, 
        '9': 0.001
    }

    frequency_letters_not_considering_spaces_v1 = {
        'a': 0.082,
        'b': 0.015,
        'c': 0.033,
        'd': 0.037, 
        'e': 0.121,
        'f': 0.021,
        'g': 0.020,
        'h': 0.048,
        'i': 0.075,
        'j': 0.002,
        'k': 0.007,
        'l': 0.042,
        'm': 0.026,
        'n': 0.071,
        'o': 0.075,
        'p': 0.022,
        'q': 0.001,
        'r': 0.060,
        's': 0.066,
        't': 0.093,
        'u': 0.030,
        'v': 0.011,
        'w': 0.017,
        'x': 0.002,
        'y': 0.019,
        'z': 0.001
    }

    frequency_letters_not_considering_spaces_v2 = {
        'a': 0.078, 
        'b': 0.015,
        'c': 0.031, 
        'd': 0.035, 
        'e': 0.115, 
        'f': 0.02, 
        'g': 0.019, 
        'h': 0.046, 
        'i': 0.072, 
        'j': 0.002, 
        'k': 0.007, 
        'l': 0.04, 
        'm': 0.024, 
        'n': 0.068, 
        'o': 0.072, 
        'p': 0.021, 
        'q': 0.001, 
        'r': 0.057, 
        's': 0.063, 
        't': 0.089, 
        'u': 0.029, 
        'v': 0.01, 
        'w': 0.016, 
        'x': 0.002, 
        'y': 0.018, 
        'z': 0.001, 
        '!': 0.001, 
        '"': 0.001, 
        '#': 0.001, 
        '$': 0.001, 
        '%': 0.001, 
        '&': 0.001, 
        "'": 0.001, 
        '(': 0.001, 
        ')': 0.001, 
        '': 0.001, 
        '+': 0.001, 
        ',': 0.001, 
        '-': 0.001, 
        '.': 0.001, 
        '/': 0.001, 
        ':': 0.001, 
        ';': 0.001, 
        '<': 0.001, 
        '=': 0.001, 
        '>': 0.001, 
        '?': 0.001, 
        '@': 0.001, 
        '[': 0.001, 
        '\\': 0.001, 
        ']': 0.001, 
        '^': 0.001, 
        '_': 0.001, 
        '`': 0.001, 
        '{': 0.001, 
        '|': 0.001, 
        '}': 0.001, 
        '~': 0.001, 
        '0': 0.001, 
        '1': 0.001, 
        '2': 0.001, 
        '3': 0.001, 
        '4': 0.001, 
        '5': 0.001, 
        '6': 0.001, 
        '7': 0.001, 
        '8': 0.001, 
        '9': 0.001
    }


    def __init__(self,
    target_file_path='Neccessary',
    consider_spaces=True,
    key=None,
    use_larger_char_list=False,
    accuracy_mode_test=False,
    tries=10000):
        '''
        Target file must be a txt file
        Accuracy mode requires a key
        Tries only applies to the accuracy mode
        '''
        try:
            if not isinstance(accuracy_mode_test,bool) or accuracy_mode_test == None:
                raise ValueError('The accuracy_mode_test can only be either True or False')
        except ValueError as e:
            print(e.args[0])
            exit_()
        else:
            self.accuracy_mode_test = accuracy_mode_test
        self.consider_spaces = consider_spaces
        self._wrong_keys = list()
        try:
            if not isinstance(use_larger_char_list,bool) or use_larger_char_list == None:
                raise ValueError('use_larger_list can only be either True or False')
            else:
                self.use_larger_char_list = use_larger_char_list
        except NameError as e:
            print(e.args[0])
            _exit()
        try:
            with open(target_file_path,'r') as f:
                self.cipher_text = f.read()
        except TypeError:
            print('Write a valid path\nThe path is neccessary')
            _exit()
        except FileNotFoundError:
            print('File not found')
            _exit()
        self.fr_cipher_text = self.__generate_frequency_of_c()
        if self.accuracy_mode_test == False:
            if key == None:
                result = self.decrypt()
            else:
                result = self.decrypt(key=key)
            self.c_p_key = result[0]
            self.p_c_key = {a:b for b,a in self.c_p_key}
            self.plain_text = result[1]
        else:
            try:
                if key == None:
                    raise ValueError('In accuracy_mode_test there must be a key')
            except ValueError as e:
                print(e.args[0])
                _exit()
            else:
                self.tries = tries 
                self.true_key = key
                self.accuracy_char, self.accuracy_key = self.__accuracy_mode()

    def __str__(self):
        return self.plain_text

    def __iter__(self):
        return self.plain_text


    def __generate_frequency_of_c(self):
        try:
            if self.consider_spaces:
                fr_l = self.frequency_letters_considering_spaces_v2.keys() if self.use_larger_char_list else self.frequency_letters_considering_spaces_v1.keys()
            else:
                fr_l = self.frequency_letters_not_considering_spaces_v2.keys() if self.use_larger_char_list else self.frequency_letters_not_considering_spaces_v1.keys()
            chars = list(set(self.cipher_text))
            if len(chars) < len(fr_l):
                chars = set(fr_l)
            total_len = len(self.cipher_text)
            dic = dict()
            for char in chars:
                c = self.cipher_text.count(char)
                dic[char] = round(c/total_len,3)
            return dic
        except KeyboardInterrupt:
            print('Exiting...')
            _exit()



    def __generate_key(self):
        try:
            while True:
                if self.consider_spaces:
                    letter_dic = Decrypt.frequency_letters_considering_spaces_v1.copy() if not self.use_larger_char_list else Decrypt.frequency_letters_considering_spaces_v2.copy()
                else:
                    letter_dic = Decrypt.frequency_letters_not_considering_spaces_v1.copy() if not self.use_larger_char_list else Decrypt.frequency_letters_not_considering_spaces_v2.copy()
                c_frequency = self.fr_cipher_text.copy()
                key = dict()
                for index,val in c_frequency.items():
                    num1 = 0.9
                    num2 = 1.1
                    lista = list()
                    while True:
                        for item,value in letter_dic.items():
                            if num1 < value < num2 and item not in lista:
                                lista.append(item)
                        if len(lista) < 4:
                            num1 -= 0.1
                            num2 += 0.1
                        else:
                            break    
                    choice = random.choice(lista)
                    key[index] = choice
                return key
        except KeyboardInterrupt:
            print('Exiting...')
            _exit()


    def __accuracy_mode(self):
        print('To exit the mode press Ctrl+c')
        try:
            accuracy_key = 0
            total_k = 0
            ocurrences_k = 0
            for x in range(1,self.tries):
                run = 1
                try_key = self.__generate_key()
                true_key = self.true_key
                total = 0
                ocurrences = 0
                for item,value in true_key.items():
                    if value == try_key[item]:
                        ocurrences += 1
                    total += 1
                if x == 1:
                    accuracy_char = ocurrences/total
                else:
                    accuracy_char = (accuracy_char*x + ocurrences/total)/x
                    accuracy_key = (ocurrences_k/total_k)*100
                if ocurrences/total == 1:
                    ocurrences_k += 1
                else:
                    self._wrong_keys.append(try_key)
                total_k += 1
                a = f"Accuracy of letter: {accuracy_char} %"
                b = f"Accuracy of key: {accuracy_key} %"
                print(a)
                print(b, end='', flush=True)
                print('\033[F', end='') 
            print(f'Accuracy of independent letter: {accuracy_char} %')
            print(f'Accuracy of key: {accuracy_key} %')
            return accuracy_char, accuracy_key
        except KeyboardInterrupt:
            print('Exiting accuracy mode...')
            try:
                print(f'Accuracy of independent letter: {accuracy_char} %')
                print(f'Accuracy of key: {accuracy_key} %')
            except NameError: print('No accuracy info could be collected :(')
            finally:
                import sys
                sys.exit()


    def decrypt(self,key=None):
        try:
            print('To exit press Ctr+c')
            print('Decrypting...')
            chars_possible = list(ascii_lowercase)
            if any(m in self.cipher_text for m in ascii_uppercase):
                chars_possible.extend(list(ascii_uppercase))
            elif any(pun in self.cipher_text for pun in punctuation):
                chars_possible.extend(list(punctuation))
            elif any(d in self.cipher_text for d in digits):
                chars_possible.extend(list(digits))
            if self.consider_spaces:
                chars_possible.append(' ')
            if not key == None:
                plain_text = ''
                if self.consider_spaces:
                    for letter in self.cipher_text:
                        if letter == ' ':
                            plain_text += ' '
                        elif letter == '\n':
                            plain_text += '\n'
                        else:
                            plain_text += key[letter]
                else:
                    for letter in self.cipher_text:
                            plain_text += key[letter]
                print('Decrypted')
                print(f'Plain text: {plain_text}')
            else:
                day1, hours1, mins1, secs1 = localtime().tm_mday, localtime().tm_hour, localtime().tm_min, localtime().tm_sec 
                total_secs1 = day1*24*3600 + hours1*3600 + mins1*60 + secs1
                cipher_text = self.cipher_text
                chars = tuple(set(cipher_text))
                self._wrong_keys.append(key)
                while True:
                    key = self.__generate_key()
                    plain_text = ''
                    for letter in cipher_text:
                        if letter == ' ' and not self.consider_spaces:
                            plain_text += ' '
                        elif letter == '\n':
                            plain_text += '\n'
                        else:
                            plain_text += key[letter]
                    ocurrences = 0
                    total = 0
                    for word in plain_text.split():
                        if word in Decrypt.words:
                            ocurrences += 1
                        total += 1
                    days2, hours2, mins2, secs2 = localtime().tm_mday, localtime().tm_hour, localtime().tm_min, localtime().tm_sec # I use this to set record of how much time was used, uses the time at the start of the program so it may not represent the actual time used
                    total_secs2 = days2*24*3600 + hours2*3600 + mins2*60 + secs2
                    difference = total_secs2 - total_secs1
                    daysd = difference//(3600*24)
                    hoursd = (difference - daysd*3600*24)//3600
                    minsd = (difference - daysd*3600*24 - hoursd*3600)//60
                    secsd = (difference - daysd*3600*24 - hoursd*3600 - minsd*60)
                    print(f'Time taken: {daysd} days {hoursd}:{minsd}:{secsd}',end='\r')
                    if ocurrences/total > 0.9:
                        print()
                        print('Decrypted...')
                        print(f'Possible key: {key}')
                        print(ocurrences/total)
                        print(f'Has taken: {daysd} days {hoursd}:{minsd}:{secsd}')
                    else:
                        self._wrong_keys.append(key)
            with open('plain_text.txt','w+') as f:
                f.write(plain_text)
            result = (key,plain_text)
            return result
        except KeyboardInterrupt:
            print('Exiting...')
            _exit()


def filter_txt_file(path,args):
    with open(path,'r') as f:
        text = list(f.read())
        for letter in text:
            if letter in args:
                text[text.index(letter)] = ''
            else:
                text[text.index(letter)] = letter.lower()
        text_t = ''
        for letter in text:
            text_t += letter
    with open(path,'w') as f:
        f.write(text_t)


if __name__ == '__main__':
    pass
