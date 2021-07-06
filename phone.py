import phonenumbers 
from colorama import Fore, Back, Style 
from colorama import init 

from termcolor import colored 


import datetime

  
from phonenumbers import carrier
from phonenumbers import geocoder
print("🥸😎😙🧐😎🤓🤓🤓👩🏼‍🦱🚎🚌📲📱🥳🤩")


print(Fore.GREEN+"enter phone number example +916785985432")
x=input(Fore.RED+"enter your number with country code +")
phone_number = phonenumbers.parse(x);
print(geocoder.description_for_number(phone_number,'en'));
service_provider = phonenumbers.parse(x);
print(carrier.name_for_number(service_provider,'en'));

