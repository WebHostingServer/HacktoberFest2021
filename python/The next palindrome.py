def rev_item(p):
    rem=0
    num=0
    while p>0:
        rem=(rem*10)+(p%10)
        num=rem
        p=p//10
    return(num)

n=int(input("Number of test cases you want: "))
for i in range(n):
    t=int(input("Enter a number:"))
    if t==rev_item(t):
        print(f"{t} itself is a palindrome")
    else:
        for i in range(t+1,t+100):

            if (rev_item(i)==i):
                print(f"Next palindrome of {t} is {rev_item(i)}")
                break
exit()
