import phonenumbers 
from colorama import Fore, Back, Style 
from colorama import init 

from termcolor import colored 


import datetime

from termcolor import colored
from pyfiglet import Figlet

f=Figlet(font='standard')
print(colored(f.renderText('shanni'),'green'))
    
print('=================================================')
print('               create by shanni')
print('=================================================')
print(' ++++++++++++++++++++')
print('\n')
print('  _,.')
print( '')
print('')
print('            shanni')
print('       _,.                   ')
print( '     ,` -.)                  ')
print('    ( _/-\\-._               ')
print('   /,|`--._,-^|            , ')
print('   \_| |`-._/||          , | ')
print('     |  `-, / |         /  / ')
print( '     |     || |        /  /  ')
print( '      `r-._||/   __   /  /   ')
print('  __,-<_     )`-/  `./  /    ')
print('  \   `---    \   / /  /     ')
print('     |           |./  /      ')
print('     /           //  /       ')
print(' \_/  \         |/  /        ')
print( '  |    |   _,^- /  /         ')
print( '  |    , ``  (\/  /_         ')
print('   \,.->._    \X-=/^         ')
print( '   (  /   `-._//^`           ')
print( '    `Y-.____(__}             ')
print('     |     {__)              ')
print( '           ()   V.1.0        ')


  
from phonenumbers import carrier
from phonenumbers import geocoder
print("🥸😎😙🧐😎🤓🤓🤓👩🏼‍🦱🚎🚌📲📱🥳🤩")


print(Fore.GREEN+"enter phone number example +916785985432")
x=input(Fore.RED+"enter your number with country code +")
phone_number = phonenumbers.parse(x);
print(geocoder.description_for_number(phone_number,'en'));
service_provider = phonenumbers.parse(x);
print(carrier.name_for_number(service_provider,'en'));

