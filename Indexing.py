Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#indexing
a = 'vijaywada'
a[0]
'v'
a[5]
'w'
a[0, 6]
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    a[0, 6]
TypeError: string indices must be integers, not 'tuple'
a[0]+a[1]+a[2]+a[3]
'vija'
>>> a = "I am in class"
>>> a[2]+a[3]
'am'
>>> 
>>> a="simple is better than complex"
>>> a[10]+a[11]+a[12]+a[13]+a[14]+a[15]
'better'
>>> a[22]+a[23]+a[24]+a[25]+a[26]+a[27]
'comple'
>>> a[22]+a[23]+a[24]+a[25]+a[26]+a[27]+a[28]
'complex'
>>> a[0]+a[1]+a[2]+a[3]+a[4]+a[5]
'simple'
>>> a="codegnan it solutions"
>>> a[12]+a[13]+a[14]+a[15]+a[16]+a[17]+a[18]+a[19]+a[20]
'solutions'
>>> a[0]+a[1]+a[2]+a[3]+a[4]+a[5]+a[6]+a[7]
'codegnan'
>>> a[9]+a[10]
'it'
>>> 
>>> #negative indexing
>>> a="I am learning python"
>>> a[-6]+a[-5]+a[-4]+a[-3]+a[-2]+a[-1]
'python'
>>> a[-15]+a[-14]+a[-13]+a[-12]+a[-11]
'learn'
>>> a[-15]+a[-14]+a[-15]
'lel'
>>> b = "python fullstack"
>>> b[-5]+b[-4]+b[-3]+b[-2]+b[-1]
'stack'
>>> b[-9]+b[-8]+b[-7]+b[-6]
'full'
>>> b[-16]+b[-15]+b[-14]+b[-13]+b[-12]+b[-11]
'python'
>>> b[-1]+a[0]
'kI'
