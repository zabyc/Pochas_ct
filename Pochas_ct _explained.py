# Encryption file

from time import localtime # For a timer
import random # For generating the keys though i think it should not be used for this purpose
from string import ascii_lowercase, ascii_uppercase, digits ,punctuation # This will serve as the encoding letters
import sys # Just for the sys.exit()

def _exit() -> None: # The only purpose is to save time in writing
    sys.exit()

class Encrypt:

    def __init__(self,target_file_path,consider_spaces=True,exit_file_path='encrypted_file.txt',use_larger_char_list=False):
        self.target = target_file_path
        self.consider_spaces = consider_spaces # For comodity
        self.exit_file_path = exit_file_path
        self.use_larger_char_list = use_larger_char_list # Changes the amount of characters with which the text will be encoded
        with open(target_file_path,'r') as f: # This will serve as the plain text
            self.plain_text = f.read() # The plain text
        self.p_c_key = self.__new_key() # This is mainly for utilities it means plain to cipher
        self.c_p_key = {c:p for p,c in self.p_c_key.items()} # Means cipher to plain,  it can serve for the accuracy mode in the decrypt function
        self.cipher_text = self.__encrypt() # The cipher text

    def __str__(self): # For comodity
        return self.cipher_text

    def __iter__(self): # For comodity if you want to suggest others do it 
        return iter(self.cipher_text)

    def __new_key(self): # This produces a new key
        characters = list(ascii_lowercase) if not self.use_larger_char_list else list(ascii_lowercase+punctuation+digits) # This will be the dictionary of possible characters
        if self.consider_spaces:
            characters.append(' ')
        key_list = random.sample(characters,len(characters))
        key = dict()
        for c_letter, p_letter in zip(key_list, characters): # The mapping
            key[p_letter] = c_letter
        return key

    def __encrypt(self) -> None: # This part encrypts and is fairely easy
        plain_text = self.plain_text
        key = self.p_c_key
        characters = tuple(set(plain_text))
        cipher_text = ''
        print('Encrypting...') # Take the prints away if you wish
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
        with open(self.exit_file_path,'w+') as f: # It writes the result to a file already given
            f.write(cipher_text)
        print('Encrypted')
            

class Decrypt: # This is the decrypting part and was a hell of a hedache for me, i rewrote more than three times in more than thre different computers
    import json
    
    with open(r'words.json','r') as f: # This is crucial as is a list that contains thousends (i think i haven't counted them) of english words to check if the decryption is accurate
        raw_data = str(f.read())
        words = json.loads(raw_data)
    
# The following are the frequency tables that are used for mapping, they are crucial
# The v1 dont consider nor punctuation nor digits but the v2 do, they exist so decrypting can be faster. Somthing similar has to do with considering spaces, mostly due to comodity

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
    key=None, # Obligatory if accuracy mode is on, else just deciphers a normal key
    use_larger_char_list=False, # Use it if any you think that many characters are used
    accuracy_mode_test=False, # A special mode. STILL needs a sample file for mapping purposes
    tries=10000):
        '''
        Target file must be a txt file
        Accuracy mode requires a key
        Tries only applies to the accuracy mode
        '''
        # This part is confusing sorry
        try: # Just to prevent errors
            if not isinstance(accuracy_mode_test,bool) or accuracy_mode_test == None:
                raise ValueError('The accuracy_mode_test can only be either True or False')
        except ValueError as e:
            print(e.args[0])
            exit_()
        else:
            self.accuracy_mode_test = accuracy_mode_test # This is a special mode that mesures the accuracy of key generation angaist a given key
        self.consider_spaces = consider_spaces
        self._wrong_keys = list() # Also crucial to improve key accuracy over time
        try: # Just preventing errors
            if not isinstance(use_larger_char_list,bool) or use_larger_char_list == None:
                raise ValueError('use_larger_list can only be either True or False')
            else:
                self.use_larger_char_list = use_larger_char_list # Later decides whether v1 or v2 are used
        except NameError as e:
            print(e.args[0])
            _exit()
        try: # Again preventing errors
            with open(target_file_path,'r') as f:
                self.cipher_text = f.read()
        except TypeError: # Please enter a valid pathway
            print('Write a valid path\nThe path is neccessary')
            _exit()
        except FileNotFoundError: # Please check if the file exist
            print('File not found')
            _exit()
        self.fr_cipher_text = self.__generate_frequency_of_c() # CRUCIAL for mapping and creation of keys, it returns a dictionary with the cipher characters from the cipher text to its frequency in the text
        if self.accuracy_mode_test == False: # Just the normal mode, it just bruteforces till it finds a POSIBLE key, it does not guranty anything (i havent decrypted anything with it yet)
            if key == None:
                result = self.decrypt() # Decrypt returns a tuple with the key at 0 and the plain text at 1
            else:
                result = self.decrypt(key=key)
            self.key = result[0]
            self.plain_text = result[1]
        else: # Enters the accuracy mode
            try: # Avoiding errors
                if key == None:
                    raise ValueError('In accuracy_mode_test there must be a key')
            except ValueError as e:
                print(e.args[0])
                _exit()
            else:
                self.tries = tries # Just works for the accuracy mode, in normal mode just tries to bruteforce it
                self.true_key = key
                self.accuracy_char, self.accuracy_key = self.__accuracy_mode()

    def __str__(self):
        return self.plain_text

    def __iter__(self):
        return self.plain_text


    def __generate_frequency_of_c(self): # The crucial part that gets the cipher to frequncy dictionary
        try:
            if self.consider_spaces:
                fr_l = self.frequency_letters_considering_spaces_v2.keys() if self.use_larger_char_list else self.frequency_letters_considering_spaces_v1.keys()
            else:
                fr_l = self.frequency_letters_not_considering_spaces_v2.keys() if self.use_larger_char_list else self.frequency_letters_not_considering_spaces_v1.keys()
            chars = list(set(self.cipher_text))
            if len(chars) < len(fr_l): # Important when small text
                chars = set(fr_l)
            total_len = len(self.cipher_text)
            dic = dict()
            for char in chars: # Here the frequency is found and the dic created
                c = self.cipher_text.count(char)
                dic[char] = round(c/total_len,3)
            return dic
        except KeyboardInterrupt:
            print('Exiting...')
            _exit()



    def __generate_key(self): # Here the key is created
        try:
            while True:
                if self.consider_spaces:
                    letter_dic = Decrypt.frequency_letters_considering_spaces_v1.copy() if not self.use_larger_char_list else Decrypt.frequency_letters_considering_spaces_v2.copy()
                else:
                    letter_dic = Decrypt.frequency_letters_not_considering_spaces_v1.copy() if not self.use_larger_char_list else Decrypt.frequency_letters_not_considering_spaces_v2.copy()
                c_frequency = self.fr_cipher_text.copy()
                key = dict()
                for index,val in c_frequency.items():
                    num1 = 0.9 # This are important to get the key
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


    def __accuracy_mode(self): # This checkes for accuracy of key generation
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
                    accuracy_char = (accuracy_char*x + ocurrences/total)/x # Gets the accuracy
                    accuracy_key = (ocurrences_k/total_k)*100
                if ocurrences/total == 1:
                    ocurrences_k += 1
                else:
                    self._wrong_keys.append(try_key)
                total_k += 1
                a = f"Accuracy of letter: {accuracy_char} %" # I actually vibe code this print part because i had no idea of how to do it
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


    def decrypt(self,key=None): # The normal and key mode
        try:
            print('To exit press Ctr+c')
            print('Decrypting...')
            chars_possible = list(ascii_lowercase)
            if any(m in self.cipher_text for m in ascii_uppercase): # Used to get the list of possible chars
                chars_possible.extend(list(ascii_uppercase))
            elif any(pun in self.cipher_text for pun in punctuation):
                chars_possible.extend(list(punctuation))
            elif any(d in self.cipher_text for d in digits):
                chars_possible.extend(list(digits))
            if self.consider_spaces:
                chars_possible.append(' ')
            if not key == None: # Key mode
                plain_text = ''
                if self.consider_spaces:
                    for letter in self.cipher_text: # Decrypt fase
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
            else: # Normal mode
                day1, hours1, mins1, secs1 = localtime().tm_mday, localtime().tm_hour, localtime().tm_min, localtime().tm_sec # Used to display the time used
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
                    if ocurrences/total > 0.9: # I didn't vibe coded this part though
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


def filter_txt_file(path,args): # This is a utility to filter unwanted characters, change it to your convenience
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
    path = '/home/leno/Programas/Python/Encryption_Decription/target.txt'
    chars_eliminate = punctuation+digits+'’'+'‘'
    unwanted_stuff = list(chars_eliminate)
    filter_txt_file(path,unwanted_stuff)
    encrypt = Encrypt(
        target_file_path=path,
        consider_spaces=False,
        exit_file_path='encrypted_target.txt',
        use_larger_char_list=False
        )
    print(encrypt.c_p_key)
    decrypt = Decrypt(
        target_file_path=encrypt.exit_file_path,
        key=encrypt.c_p_key,
        consider_spaces=False,
        accuracy_mode_test=True,
        use_larger_char_list=False
    )