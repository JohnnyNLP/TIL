# 예시 1
# text = '200%'
# try:
#     number=int(text)
# except ValueError:
#     print('{}는 숫자가 아니잖아요'.format(text))

# 예시 2
def safe_pop_print(list, index):
    try:
        print(list.pop(index))
    except IndexError:
        print('index:{}인 값 없음'.format(index))
    
safe_pop_print([1, 2, 3], 5)