import random
import PySimpleGUI as sg
import pyperclip

uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
digits = '0123456789'
symbols = '!@#$%^&*()_+-=[]{}|;:,.<>/?`~'

upper, lower, nums, syms = True, True, True, True

all = ""

if upper:
    all += uppercase_letters
if lower:
    all += lowercase_letters
if nums:
    all += digits
if syms:
    all += symbols

length = 20
amount = 1

for x in range(amount):
    password = ''.join(random.sample(all, length))

layout = [[sg.Text('Press OK to copy password')], [sg.OK(), sg.Cancel()], [sg.Text('Your Password: '), sg.InputText(password)]]


window = sg.Window('Bee Password Generator', layout)
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel':
        break
    if event == 'OK':
            pyperclip.copy(password)
            window.close()



