# from ch03.data import todo as data
from ch04.data import todo as data
from ch04.model import Todo

if __name__ == '__main__':
    data.insert_one(Todo(task='study fastapi3'))
    print(data.find_all())
