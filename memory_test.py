import psutil

MEMORY_TRESHOLD = 90


def check_memory_usage():
    memory_percent = psutil.virtual_memory().percent
    return memory_percent


def send_alarm():
    memory_percent = check_memory_usage()
    if memory_percent > MEMORY_TRESHOLD:
        return {'message': f'Memory usage exceeded threshold: {MEMORY_TRESHOLD}'}
    else:
        return {'message': 'No problem with memory'}
