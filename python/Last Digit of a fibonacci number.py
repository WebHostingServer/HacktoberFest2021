
def fastfib(n):
        
#     if n <= 1:
#         return n
#     elif n == 2:
#         return 1
#     else:
#         a = [0,1]
#         for i in range(2, n+1):
#             a.append((a[i-1] + a[i-2])%10)
#         return a[n]
    a, b = 0, 1
    for i in range(n % 60):
        a, b = b, (a + b) % 10
    return a

if __name__ == "__main__":
    n = int(input())
    print(fastfib(n))
