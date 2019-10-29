from subprocess import Popen, PIPE, call

X1 = call('python hello_out.py')     # удобно
print('Close code:', X1)
#############################################################
pipe2 = Popen('python hello_out.py', stdout=PIPE)
X2 = pipe2.communicate()[0]          # (stdout, stderr)
print(X2)
X2_return = pipe2.returncode         # код завершения
print('Close code:', X2_return)

#############################################################
pipe3 = Popen('python hello_out.py', stdout=PIPE)
X3 = pipe3.stdout.read()
print(X3)
X3_return = pipe3.wait()             # код завершения
print('Close code:', X3_return)

#############################################################
pipe4 = Popen('python hello_in.py', stdin=PIPE)
X4 = pipe4.stdin.write(b'Pokey\n')
print(X4)
pipe4.stdin.close()
X4_result = pipe4.wait()
print(X4_result)
open('hello_in.txt').read()         # вывод был отправлен в файл

#############################################################
pipe5 = Popen('python reader.py', stdin=PIPE, stdout=PIPE)
X5 = pipe5.stdin.write(b'Lumberjack\n')
print(X5)
pipe5.stdin.write(b'12\n')
pipe5.stdin.close()
output = pipe5.stdout.read()
X5_result = pipe5.wait()
print('Close code:', X5_result)
print(output)
