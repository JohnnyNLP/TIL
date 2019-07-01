# 예시 1
# text = '200%'
# try:
#     number=int(text)
# except ValueError:
#     print('{}는 숫자가 아니잖아요'.format(text))

# 예시 2
# def safe_pop_print(list, index):
#     try:
#         print(list.pop(index))
#     except IndexError:
#         print('index:{}인 값 없음'.format(index))
    
# safe_pop_print([1, 2, 3], 5)

# 예시 3
# try:
#     list=[]
#     print(list[0]) #IndexError
#     text='abc'
#     number=int(text) #invalid literal
# except Exception as ex:
#     print('오류가 발생했습니다.', ex)

# 예시 4
# def rsp(mine, yours):
#     allowed=['가위','바위','보']
#     if mine not in allowed :
#         raise ValueError
#     if yours not in allowed :
#         raise ValueError
# rsp('가위', '바')

# 예시 5
# try:
#     rsp('가위', '바')
# except ValueError:
#     print('잘못된 값을 넣었습니다.')

# 예시 6
# classrooms = {'1반':[162, 175, 198, 137, 145, 199], '2반':[165, 177, 157, 160, 191]}
# for class_id, heights in classrooms.items():
#     for height in heights:
#         if height>190:
#             print(class_id, '에 190이 넘는 학생이 있습니다')
#             raise StopIteration

# 예시 7
value = input('입력>') or '입력값 없음'
print('입력받은 값:', value)


