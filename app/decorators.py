import json


def string(func):
    def wrapper(*args):
        return  json.dumps( { 'data': func(*args) })
    wrapper.__name__ = func.__name__
    return wrapper
