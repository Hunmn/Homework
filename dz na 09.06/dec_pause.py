import time

def pause(n):
    def decorator(func):
        def wrapper(*args,**kwargs):
            time.sleep(n)
        return wrapper
    return decorator


