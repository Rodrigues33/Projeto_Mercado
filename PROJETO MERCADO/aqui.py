from PySimpleGUI import PySimpleGUI as sg

sg.theme('Renddit')
layout=[
    [sg.Text('usuario')],
    [sg.Input(key='usuario')],
    [sg.Text('senha')],
    [sg.Input(key='senha')],
    [sg.Checkbox('salvar o longin')],
    [sg.Button('login')],
    [sg.Text('',key='mensagem')],

    
]
window = sg.Window('login', layout=layout)

while True:
    Event,Values= window.read()
    if Event==sg.WINDOW_CLOSED:
        break
    elif Event=='login':
        senha_correta='123456'
        usuario_correto='maycon'
        usuario=Values['usuario']
        senha=Values['senha']
        if senha == senha_correta and usuario== usuario_correto:
            window['mesagem'].update ('login feito com sucesso')
        elif senha != senha_correta or usuario != usuario_correto:

            window['mensagem'].update('senha ou susuario incorreto')