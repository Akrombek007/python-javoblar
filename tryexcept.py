# y = input('Yoshingizni kiritng')
# try:
#     yosh = int(y)
#     print(f'tuguilgan yilingiz = {2021 - yosh}')
# except ValueError:
#     print('siz  son kiritmadingiz')
# else:
#     print(f'tuguilgan yilingiz = {2021 - yosh}')
#
# print('dastur ishlamoqda')
# x = 10
# y = int(input('son kiritng = '))
# try:
#     s = x/y
#     #print(x/y)
# except ZeroDivisionError:
#     print('Nolga bolishni iloji yuq')
# else:
#     print('natija = ',s)

# a = ['banan','anor','anjir','gilos']
# x = int(input('indexni kiriting = '))
# try:
#     print(a[x])
# except IndexError:
#     print('bunaqa element yuq')

# a = {
#     'ism':'Olim',
#     'fam':'Dilshodov',
#     'tyil':2021
#     }
# kalit = input('kiriting')

# try:
#     print(f'Foydalanuvchi ismi{a[kalit]}')
# except KeyError:
#     print('Bunaqa kalit mavjud emas')

# x = (input())
# y = int(input())
# a = [131,23,21]
# try:
#    # print('x / y = ',x/y)
#     print(a[y])
# except ZeroDivisionError:
#     print("Nol sonini kiritdingiz")
# except IndexError:
#     print('Siz mavjud bo\'lmagan index kiritdingiz!!!')
# #    print(a[len(a)])
#     if isinstance(x ,str):
#         print('son kiriting!!!')
# print('davom etmoqda')
#
# if isinstance(x, int) or isinstance(x, float):
#     if len(a)<x:
#         print('Siz mavjud bo\'lmagan index kiritdingiz!!!')