x = int(input("Enter :"));
for i in range(3,x):
    flag =0;
    for j in range(2,i):
        if(i%j ==0):
            flag = 1;
    if(flag==0):
        print(i);


