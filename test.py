# -*- coding: utf-8 -*-

# test 1 #

# def log(func):
#     def wrapper():
#         print 'before calling',func.__name__
#         func()
#         print 'end calling',func.__name__
#     return wrapper
#
# @log#装饰器，函数指针
# def hello():
#     print 'hello'
#
# if __name__ == '__main__':
#     hello()
#     #log(hello())

# test 2 #

# def log(func):
#     def wrapper(name):
#         print 'before calling',func.__name__
#         func(name)
#         print 'end calling',func.__name__
#     return wrapper
#
# @log#装饰器，函数指针
# def hello(name):
#     print 'hello',name
#
# if __name__ == '__main__':
#     hello('nowcoder')

# test 3
# 可变参数，无名字参数
'''
before calling hello
args ('nowcoder', 2) kvargs {}
hello nowcoder 2
end calling hello
'''
#
# def log(func):
#     '''
#     *：无名字参数
#     **：有名字参数
#     '''
#     def wrapper(*args,**kvargs):
#         print 'before calling',func.__name__
#         print 'args',args,'kvargs',kvargs
#         func(*args,**kvargs)
#         print 'end calling',func.__name__
#     return wrapper
#
# @log#装饰器，函数指针
# def hello(name,age):
#     print 'hello',name,age
#
# if __name__ == '__main__':
#     hello('nowcoder',2)


# test 4 #
# 有名字参数
'''
before calling hello
args () kvargs {'age': 2, 'name': 'nowcoder'}
hello nowcoder 2
end calling hello
'''
# def log(func):
#     def wrapper(*args,**kvargs):
#         print 'before calling',func.__name__
#         print 'args',args,'kvargs',kvargs
#         func(*args,**kvargs)
#         print 'end calling',func.__name__
#     return wrapper
#
# @log#装饰器，函数指针
# def hello(name,age):
#     print 'hello',name,age
#
# if __name__ == '__main__':
#     hello(name = 'nowcoder',age = 2)


# test 5 #
# 装饰器有参数
# 批量缩进：tab，反向缩进shift+tab
'''
INFO before calling hello
INFO args () kvargs {'age': 2, 'name': 'nowcoder'}
hello nowcoder 2
INFO end calling hello
'''

def log(level, *args, **kvargs):
    def inner(func):
        def wrapper(*args, **kvargs):
            print level,'before calling', func.__name__
            print level,'args', args, 'kvargs', kvargs
            func(*args, **kvargs)
            print level,'end calling', func.__name__

        return wrapper

    return inner


@log(level='INFO')
def hello(name, age):
    print 'hello', name, age


if __name__ == '__main__':
    hello(name='nowcoder', age=2)
