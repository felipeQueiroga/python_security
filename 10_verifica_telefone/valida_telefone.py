import phonenumbers 
from phonenumbers import geocoder

phone = input('Digite o numero do telefone no formato +556733577000: ')

phone_numbers = phonenumbers.parse(phone)

print(geocoder.description_for_number(phone_numbers, 'pt'))