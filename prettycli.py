# -*- coding: utf-8 -*-

colors = {
    'red': '\033[31m',
    'redBold': '\033[1;31m',
    'green': '\033[32m',
    'greenBold': '\033[1;32m',
    'yellow': '\033[33m',
    'yellowBold': '\033[1;33m',
    'blue': '\033[34m',
    'blueBold': '\033[1;34m',
    'blueUnderline': '\033[4;34m',
    'megenta': '\033[35m',
    'megentaBold': '\033[1;35m',
    'cyan': '\033[1;36m',
    'cyanBold': '\033[1;36m',
    'greyLight': '\033[2;37m',
    'clear': '\033[0m',
    'hidden': ''
}

def info(text, label='INFO'):
    ''' green
    '''
    return '\n{c[greenBold]} {label} 💁 {c[green]} {text} {c[clear]}'.format(c=colors, label=label, text=text)

def warn(text, label='WARN'):
    ''' yellow
    '''
    return '\n{c[yellowBold]} {label} ⚠️ {c[yellow]} {text} {c[clear]}'.format(c=colors, label=label, text=text)

def error(text, label='ERROR'):
    ''' red
    '''
    return '\n{c[redBold]} {label} 🤦 {c[red]} {text} {c[clear]}'.format(c=colors, label=label, text=text)

def wait(text, label='WAIT'):
    ''' blue
    '''
    return '\n{c[blueBold]} {label} 🙄 {c[blue]} {text} {c[clear]}'.format(c=colors, label=label, text=text)

def critical(text, label='CRITICAL'):
    ''' critical
    '''
    return '\n{c[megentaBold]} {label} 🚨 {c[megenta]} {text} {c[clear]}'.format(c=colors, label=label, text=text)

def command(text):
    ''' cyan
    '''
    return '\n⚡  {c[cyanBold]}{text}{c[clear]}'.format(c=colors, text=text)

def link(text):
    ''' blue
    '''
    return '\n🔗  {c[blueUnderline]}{text}{c[clear]}'.format(c=colors, text=text)

def ignore(text):
    ''' grey
    '''
    return '\n😴  {c[greyLight]}{text}{c[clear]}'.format(c=colors, text=text)
