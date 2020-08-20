# Type your code here
def my_func(a,b):
    if a>b:
        greater=a
    else:
        greater=b
    while(True):
        if (greater%a==0) and (greater%b==0):
            LCM=greater
            break
        greater=greater+1
    return LCM
