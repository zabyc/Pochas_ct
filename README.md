Hello!
This is my first real coding project, it is about two tools for description and encryption, they are relatively simple (especially the encryption one). 
However the main purpose of uploading this to github was to get feedback from the comunity, especially with bugs. I feel that the code is weak and slow.

Characteristics of the code:

It is writen in python

In the encryption tool a basic key mapping is used
The decryption tool consist of three main functions: '__generate_frequency_of_c', which assigns a frequency to each letter in the cipher text; '__generate_key' which is the most important part of the decrypt tool as it creates the key based on te dictionary proportioned by the previous function and by a dictionaries (that i think took from evilpacket/letter_freq.json credits thanks to @evilpacket); and; 'decrypt', which just decrypts and checks if the text is coherent (just works for english right now, just add other dictionaries to get it to work, also the letter frequency ones should be subsituted in that case).
It also contains a function to clean a sample from unwanted characters, if anyone knows how to eliminate most utf values please post it, it is not a priority though so just do it if you think it is useful :)

I will also post my original samples and a copy of the code.

What you can do:
Have fun trying to break the code, use it if you want and please post reviews and corrections if you can, i will try to make as clear as possible so is redable.
Thanks for reading me
