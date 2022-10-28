# try :
#     代码块（可能出现错误的语句）
# except 异常类型 as 异常名 :
#     代码块（出现错误以后的处理方式）
# except 异常类型 as 异常名 :
#     代码块（出现错误以后的处理方式）
# else :
#     代码块（没出错要执行的语句）
# finally :
#     代码块（该代码总会执行）

# try必须要有，except和finally必须要有其一，else可有可没有

I = []
try :
    # print(c)
    # print(10/0)
    # I[10]
    'helo' + 123
except NameError :
    print('出现 NameError ')
except ZeroDivisionError :
    print('出现   ZeroDivisionError')
except  IndexError :
    print('出现   IndexError')
except Exception as e :
    print('未知异常' , e , type(e))
finally :
    print('无论是否出现异常，该子句都会出现')