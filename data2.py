#two polynomial functions
import numpy
while True:
    print('commands:')
    print('1-input')
    print('2-sum')
    print('3-multiply')
    print('4-print')
    print('5-exit')
    command=int(input('enter command number :'))
    if command==1:
       numco=int(input('enter number of coefficient :'))
       colist=[]
       for i in range(numco):
           coefficient=int(input('enter coefficient :'))
           colist.append(coefficient)
       p=numpy.poly1d(colist)
       colist1=[]
       for i in range(numco):
           coefficient1=int(input('enter new coefficient :'))
           colist1.append(coefficient1)
       p1=numpy.poly1d(colist1)
    if command==2:
        sump=[x+y for x,y in zip(colist,colist1)]
        psum=numpy.poly1d(sump)
        print('sum of two functions:',psum)
    if command==3:
        pmul=numpy.polymul(p,p1)
        print('multiply of two functions:',pmul)
    if command==4:
        print(p,p1)
    if command==5:
        break
