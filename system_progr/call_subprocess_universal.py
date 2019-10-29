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
