print('''   
    _   __                   _       __               __
   / | / /_  ______ ___     | |     / /___  _________/ /
  /  |/ / / / / __ `__ \    | | /| / / __ \/ ___/ __  / 
 / /|  / /_/ / / / / / /    | |/ |/ / /_/ / /  / /_/ /  
/_/ |_/\__,_/_/ /_/ /_/     |__/|__/\____/_/   \__,_/   
                                                       

By Natnael Kedir
''')


with open('word.txt','r') as wordlist:
    word = wordlist.readlines()
with open('translated.txt','r',encoding='utf-8') as amharic:
    amharic_lines = amharic.readlines()
   
selected = int(input('Enter your number: '))
def english_output():
    try:
        text = word[selected].replace('\n','')
        print('[+] Your number is: ' + str(text))
    except IndexError:
        print('[-] Sorry number out of range in English')

def amharic_output():
    try:
        inamharic = amharic_lines[selected].replace('\n','')
        print('[+] Your number is: ' + str(inamharic)) 
    except IndexError:
        print('[-] Sorry number out of range in Amharic')  

english_output()
amharic_output()