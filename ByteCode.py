from importlib.resources import path
import os
path = input("请输入完整class路径：")
result = os.popen("hexdump"+" "+path)
line = result.readline()
special = line[7]
flag=1
str1=""
while(line):
    line = line[8:-1].split(special)
    for i in line:
        if i==special :
            pass
        if str(i)=="ca" and flag==1:
            str1=str1+"new byte[]{-54,"
        elif str(i)=="fe" and flag==1:
            str1=str1+"-2,"
        elif str(i)=="ba" and flag==1:
            str1=str1+"-70,"
        elif str(i)=="be" and flag==1:
            str1=str1+"-66,"
        else:
            try:
                flag=2
                if int(i,16)>=128:
                    str1=str1+str((int(i,16)-256))+","
                else:
                    str1=str1+str(int(i,16))+","
            except Exception as e:
                pass
    line=result.readline()

str1=str1[:-1]+"}"
print(str1)
