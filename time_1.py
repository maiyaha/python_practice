import time

a1= time.time()
a2=time.localtime()

print(a1)
print(a2)
print(a2.tm_wday, a2.tm_yday) #월0화1수2목3금4토5일6, 1월1일=0