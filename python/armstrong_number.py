import math as m
def secy(x,y):
    a = m.log(x,y)
    print(a)
    return a
def main():
    print('Format: y**ans = x')
    x = int(input('x: '))
    y = int(input('y: '))
    s = int(secy(x,y))
    print(y,'**',s,'=',x)
if __name__ =='__main__':
    main()
