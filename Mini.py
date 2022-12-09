
import numpy as np
import math
x=[0.1,0.5,0.2]
x=[[0.1,0.5,0.2],
[.2,.3,.1],
[.7,.4,.2],
[.1,.4,.3]
]



weight= [.4,.2,.6]

y=[0,1,0,1]
bias=.5

learning=.1

def sigmoid(w_sum):
 w=1/(1+np.exp(-w_sum))
 return round(w,3)
  
  
def Perceptron(i):
 w_sum=0
 for i,j in zip(x[i],weight):
  w_sum += (i*j)
 w_sum+=bias
 w=sigmoid(w_sum)
 return sigmoid(w)
  

def Loss(p,i):
 a=y[i]*math.log10(p)
 b=(1-y[i])*math.log10(1-p)
 loss= -(
  
 a+ b
  
 )
 return round(loss,2)

def Gridian(weight,bias,x,y,i):
 p=Perceptron(i)
 loss=Loss(p,i)
 w=0
 bias=bias+learning * (y[i]-p)
 for i in range(len(weight)):
  w= weight[i]+learning *(y[i]-p)*x[i]
  weight[i]=round(w,3)
 return weight,round(bias,3),loss

def result():
  for j in range(0,30):
    l=0
    for i in range(4):
      a,b,c=Gridian(weight,bias,x[i],y,i)
      l+=c
      #print(c,end="\n")
    print(f"epoche : {j} ,loss = {(l/4)}")
    l=0

r= result()
