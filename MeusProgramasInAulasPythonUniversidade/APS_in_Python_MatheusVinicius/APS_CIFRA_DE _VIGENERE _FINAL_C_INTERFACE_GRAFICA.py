#print("O PROJETO DE DESENVOLVIMENTO DESTA CRIPTOGRAFIA FOI PARA RESTRIÇÃO DE ACESSO \n"
#      "         A UMA ÁREA CONTAMINADA AMBIENTALMENTE E QUE APRESENTA \n"
#      "                RISCOS A SAÚDE PÚBLICA!!! \n\n")
#print("**DESENVOLVIDO POR ALUNOS DE CIÊNCIA DA COMPUTAÇÃO UNIP**")

import re
import string
import time
import PySimpleGUI as sg

alfabeto = "abcdefghijklmnopqrstuvwxyz"
def Criptografar (b, k):
    r = ""
    kpos = [] 
    for z in k:
        kpos.append(alfabeto.find(z))
    i=0
    for z in b:
        if i == len(kpos):
            i=0
        pos = alfabeto.find(z) + kpos [i] 
        if pos >= 25:
            pos = pos-26 
        r += alfabeto[pos].capitalize ()
        i +=1
    return r

def Descriptografar (r, k):
    b= ""
    kpos= []
    for z in k:
        kpos.append(alfabeto.find(z))
    i= 0
    for z in r:
        if i == len(kpos):
            i = 0
        pos = alfabeto.find(z.lower()) -kpos[i]
        if pos <0:
            pos = pos + 26
        b += alfabeto[pos].lower()
        i +=1
    return b
 
sg.theme('SystemDefault')

def janela_inicial():
    layout = [  
                [sg.Text('O PROJETO DE DESENVOLVIMENTO DESTA CRIPTOGRAFIA FOI PARA RESTRIÇÃO DE ACESSO A UMA ÁREA CONTAMINADA AMBIENTALMENTE E QUE APRESENTA RISCOS A SAÚDE PÚBLICA!!!', size=(40,5), justification='center')],
                [sg.Text('**DESENVOLVIDO POR ALUNOS DE CIÊNCIA DA COMPUTAÇÃO UNIP**',size=(55,2), justification='center')],
                [sg.Button('Continuar')]
            ]
    return sg.Window('Início', layout=layout, finalize=True, element_justification='c')

def janela_menu():
    layout = [  
                [sg.Text('O que você deseja fazer?',size=(30,2), justification='center')],
                [sg.Button('Criptografar')],
                [sg.Button('Descriptografar')],
                [sg.Button('Voltar')],
        ]
    return sg.Window('Opções', layout=layout, finalize=True, element_justification='c')

def janela_criptografar():
    layout = [  
                [sg.Text('Escreva a Frase ou Mensagem:')],
                [sg.Input(key='b')],
                [sg.Text(size=(1,1))],
                [sg.Text('Escreva a Chave:')],
                [sg.Input(key='k')],
                [sg.Text(size=(1,1))],
                [sg.Button('Voltar'),sg.Button('Criptografar')],
        ]
    return sg.Window('Criptografar', layout=layout, finalize=True)

def janela_descriptografar():
    layout = [  
                [sg.Text('Escreva a Frase ou Mensagem:')],
                [sg.Input(key='r')],
                [sg.Text(size=(1,1))],
                [sg.Text('Escreva a Chave:')],
                [sg.Input(key='k')],
                [sg.Text(size=(1,1))],
                [sg.Button('Voltar'),sg.Button('Descriptografar')],
        ]
    return sg.Window('Descriptografar', layout=layout, finalize=True)

janela1, janela2, janela3, janela4 = janela_inicial(), None, None, None

while True:
    window, event, values = sg.read_all_windows()
    if window == janela1 and event == sg.WIN_CLOSED:
        break
    if window == janela1 and event == 'Continuar':
        janela2 = janela_menu()
        janela1.hide()

    if window == janela2 and event == 'Criptografar':
        janela3 = janela_criptografar()
        janela2.hide()

    if window == janela2 and event == 'Descriptografar':
        janela4 = janela_descriptografar()
        janela2.hide()

    if window == janela2 and event == 'Voltar':
        janela2.hide()
        janela1.un_hide()
    
    if window == janela3 and event == 'Voltar':
        janela3.hide()
        janela2.un_hide()

    if window == janela4 and event == 'Voltar':
        janela4.hide()
        janela2.un_hide()

    if window == janela3 and event == 'Criptografar':
        b = values['b']
        b = b.replace(' ', '')
        
        if b.isalpha():
            k = values['k']
            k = k.strip()
            if k.isalpha():
                r = Criptografar(b,k)
                sg.Popup('Você digitou:' + b, 'A frase codificada é:', r)
            else:
                sg.Popup('Digitado:' + k, 'Somente Letras do Alfabeto são permitidas!!')
        else: 
            sg.Popup('Digitado:' + b, 'Escreva uma Chave Válida,a chave contendo apenas uma palavra!')

    if window == janela4 and event == 'Descriptografar':
        r = values['r']
        r = r.replace(' ', '')

        if r.isalpha():
            k = values['k']
            if not k.isalpha():
                sg.Popup('Digitado:' + k, 'Escreva uma Chave Válida,a chave contendo apenas uma palavra!')
            else:
                b = Descriptografar(r, k)
                sg.Popup('Você digitou:' + r, 'A frase decodificada é:', b)
        else:
             sg.Popup('Digitado:' + r, 'Somente Letras do Alfabeto são permitidas!!')