file = open('data.txt', 'w')
file.write('Hello, world!\n')
file.writelines(['Hello, world number 2\n', 'Bye world number 2'])
file.close()

open('somefile.txt', 'w').write('Hello G\'day Bruce\n')     # записать во временный файл
open('somefile.txt', 'r').read()                            # прочитать временный файл
