from subprocess import Popen, PIPE, call

X1 = call('python hello_out.py')     # удобно

#############################################################
pipe2 = Popen('python hello_out.py', stdout=PIPE)
X2 = pipe2.communicate()[0]          # (stdout, stderr)
X2_return = pipe2.returncode         # код завершения

#############################################################
pipe3 = Popen('python hello_out.py', stdout=PIPE)
X3 = pipe3.stdout.read()
X3_return = pipe3.wait()             # код завершения
