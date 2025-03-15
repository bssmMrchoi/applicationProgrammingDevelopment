# from ch03.data import todo as data
from ch03.singleton import todo as data

if __name__ == '__main__':
    # data.insert_one('study fastapi4')
    print(data.find_all())
