Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#slicing
a = "time is very precious"
a[8:11]
'ver'
a[8:12]
'very'
a[0:4]
'time'
a[13:20]
'preciou'
a[13:21]
'precious'
>>> a[:7]
'time is'
>>> a[8:]
'very precious'
>>> a[0:4:2]
'tm'
>>> a[13:20:2]
'peiu'
>>> a[13:21:2]
'peiu'
>>> a[13:21:3]
'pcu'
>>> a[13:21:1]
'precious'
>>> a[-1:-9]
''
>>> a[-8:-1]
'preciou'
>>> a[-8:0]
''
>>> 
>>> #negative slicing example
>>> a="vizag is a city of destiny"
>>> a[-7:-1]
'destin'
>>> a[-7:]
'destiny'
>>> a[-15:-11]
'city'
>>> a[-24]+a[-19]
'zs'
>>> a[-24:-19]
'zag i'
>>> a[-26:-21]
'vizag'
>>> a[-7::2]
'dsiy'
>>> a[-26:-21:2]
'vzg'
