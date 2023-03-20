import random
passlen=int(input('enter the lengh of password : '))
s=('abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?')

p="".join(random.sample(s,passlen))
print(p)
