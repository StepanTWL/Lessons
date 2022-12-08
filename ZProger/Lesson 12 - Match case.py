import requests

command = ['rm', '1', '2']

#в 3.8 не поддерживается
match command:
    case ['make']:
        print('make')
    case ['make', cmd]:
        print(f'make: {cmd}')
    case ['restart']:
        print('restart')
    case ['rm', *files]:
        print(f'rm files: {files}')

value = 0

match value:
    case 0:
        print(f'result: {value}')
    case _:
        print(f'default: {value}')

args = ['start', '-h', '-k']

match args:
    case ['start']:
        print("Добавьте аргументы")
    case ['start', *arg]:
        print(f"Аргументы: {arg}")
    case ['start', ('-h' | '--help' | 'help') as hlp]:
        print(f'Аргументы: {hlp}')
    case ['stop', *_]:
        print("Stop")
    case _:
        print('Error')

args1 = ['start', 'alex1998']
black_list = ['1441', 'alex1998']

match args:
    case ['start', nickname] if nickname not in black_list:
        print(f"Доступ {nickname} разрешен")
    case _:
        print(f"Доступ {nickname} запрещен")


def http_status(status: int):
    match status:
        case 400:
            return 'Bad request'
        case 401:
            return 'Unauthorized'
        case 403:
            return "Forbidden"
        case 404:
            return "Non found"

class switch:
    on = 1
    off = 0

status = 0

match status:
    case switch.on:
        print('ON')
    case switch.off:
        print('OFF')
