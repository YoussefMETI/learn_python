x = int(input("Enter :"));
a=0;
b=1;
print(a);
print(b);
for i in range(2,x):
    print(a+b);
    c=a+b;
    a=b;
    b=c;
