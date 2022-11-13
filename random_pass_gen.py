import random

alpha_up = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
alpha_low = 'abcdefghijklmnopqrstuvwxyz'
num = '1234567890'
symbols = '~!@#$%^&*()_+-=}{[]:;><?/'
pass_length = int(input('Password length: '))

for x in range(1, pass_length+1):
    print(random.choice(alpha_up+alpha_low+num+symbols), end='')
