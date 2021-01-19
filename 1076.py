color = ["black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white"]
value = [0,1,2,3,4,5,6,7,8,9]
s1 = str(input())
s2 = str(input())
s3 = str(input())
print((value[color.index(s1)]*10+value[color.index(s2)])*(10**color.index(s3)))