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

def info(text):
    ''' green
    '''
    return '💁 {c[greenBold]} INFO :{c[green]} {text} {c[clear]}'.format(c=colors, text=text)

def warn(text):
    ''' yellow
    '''
    return '⚠️ {c[yellowBold]} WARN :{c[yellow]} {text} {c[clear]}'.format(c=colors, text=text)

def error(text):
    ''' red
    '''
    return '🤦🏽 {c[redBold]} ERROR :{c[red]} {text} {c[clear]}'.format(c=colors, text=text)

def wait(text):
    ''' blue
    '''
    return '🙄 {c[blueBold]} WAIT :{c[blue]} {text} {c[clear]}'.format(c=colors, text=text)

def critical(text):
    ''' critical
    '''
    return '🚨 {c[megentaBold]} CRITICAL :{c[megenta]} {text} {c[clear]}'.format(c=colors, text=text)

def command(text):
    ''' cyan
    '''
    return '⚡ {c[cyanBold]}{text}{c[clear]}'.format(c=colors, text=text)

def link(text):
    ''' blue
    '''
    return '🔗 {c[blueUnderline]}{text}{c[clear]}'.format(c=colors, text=text)

def ignore(text):
    ''' grey
    '''
    return '😴 {c[greyLight]}{text}{c[clear]}'.format(c=colors, text=text)
