import allantools
import numpy as np
import csv
import matplotlib.pyplot as plt
import math as ma

time=[]
gx=[]
csvFile=open("test.csv","r")
reader=csv.reader(csvFile)
sz=0
for item in reader:
    time.append(float(item[0])/1e9)
    gx.append(float(item[3]))
    sz+=1
csvFile.close()

tau=[]
div=[]
jump=0.005
while jump<900:
    ans=0.0
    now=0
    prev=0
    thre=jump
    sum=0.0
    psum=0.0
    all=0.0
    while now<sz:
        while now<sz and time[now]<thre:
            sum+=gx[now]
            now+=1
        if now>prev:
            sum/=(now-prev)
        diff=sum-psum
        if now==sz:
            pass
        else:
            all+=diff*diff
            ans+=1
        thre+=jump
        prev=now
        psum=sum
        sum=0
    if ans>0:
        all/=ans
    tau.append(jump)
    div.append(ma.sqrt(all))
    jump*=2
plt.plot(tau,div)
plt.yscale("log")
plt.xscale("log")
plt.show()