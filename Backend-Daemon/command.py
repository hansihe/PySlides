__author__ = 'HansiHE'


commands = dict()

def register_command(command):
    def decorator(func):
        commands[command] = func
        return func
    return decorator