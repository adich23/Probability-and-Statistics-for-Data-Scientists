import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
from scipy import special
from scipy.stats import norm

def get_data():
  true_dis = np.random.uniform(0,1,size=800)
  pr_dis = []
  for num in true_dis:
    if num <= 0.25:
      pr = np.random.normal(0,1)
    elif num <= 0.5:
      pr = np.random.normal(3,1)
    elif num <= 0.75:
      pr = np.random.normal(6,1)
    else:
      pr = np.random.normal(9,1)

    pr_dis.append(pr)
  return pr_dis

def get_prazen(data,h,pr_dis):
  n = len(pr_dis)
  y = []
  # print (n)
  for num in data:
    # summ = 0.0
    diff = [1 if np.abs(num-pr) <= h/2.0 else 0 for pr in pr_dis ]
    summ = sum(diff)
    # print ("SUM - ",summ)
    summ/=(n*h*1.0)
    y.append(summ)
  
  # print ("Prazen " - y)
  return y


#Q-7-a
# getting alphas
X = np.arange(-5,10,0.1)
alpha = X
pr_dis = get_data()
# True distribution
Y0 = 0.25*(norm.pdf(alpha,0,1) + norm.pdf(alpha,3,1) + norm.pdf(alpha,6,1) + norm.pdf(alpha,9,1))
# get kernel density estimator
Y = get_prazen(alpha,0.1,pr_dis)
Y2 = get_prazen(alpha,1,pr_dis)
Y3 = get_prazen(alpha,7,pr_dis)

# plotting the graphs
plt.figure('Kernel Density Estimation',figsize=(15,10))
plt.plot(X, Y0 ,label='True pdf')
plt.plot(X, Y ,label='h = 0.1')
plt.plot(X, Y2 ,label='h = 1')
plt.plot(X, Y3 ,label='h = 7')

plt.xlabel('x', fontsize=18)
plt.ylabel('Pr[X<=x]', fontsize=18)
plt.legend(loc="upper left", prop={'size': 16})
plt.grid()
plt.show()
plt.savefig("PDF.png")

def get_bias(kd_matrix, true_matrix):
  # pr = np.mean(diff, axis=0)
  avg_kd_matrix = np.mean(kd_matrix,axis=0)
  pr = np.subtract(avg_kd_matrix, true_matrix)
  return pr

def get_var(kde_matrix, estimation):
  diff = np.subtract(kd_matrix, estimation)
  print (diff.shape)
  sqr = np.power(diff,2)
  pr = np.mean(sqr, axis=0)
  return pr

#Q-7-b
h_s = [0.01,0.1,0.3,0.6,1,3,7]
mse_list = []
var_list = []
bias_list = []
alpha = np.arange(-5,10,0.1)
y_0 = 0.25*(norm.pdf(alpha,0,1) + norm.pdf(alpha,3,1) + norm.pdf(alpha,6,1) + norm.pdf(alpha,9,1))

# generate 150 samples of 800 data points 
raw_matrix = []
for i in range(150):
    b = get_data()
    raw_matrix.append(b)


for h in h_s:
  print ("h - ",h)
  kd_matrix = []
  true_matrix = []

  for i in range(150):
    b = raw_matrix[i]
    kde_0 = get_prazen(alpha,h,b)
    kd_matrix.append(kde_0)

  kd_matrix = np.array(kd_matrix)
  estimation = kd_matrix.mean(axis=0)

  bias = get_bias(kd_matrix, y_0)
  
  total_bias = [i**2 for i in bias]
  total_bias_2 = np.mean(total_bias)

  var = get_var(kd_matrix, estimation)
  var_total = np.mean(var)

  mse = var + bias**2
  mse_total = total_bias_2 + var_total

  mse_list.append(mse_total)
  bias_list.append(total_bias_2)
  var_list.append(var_total)


print ("Minimum value of MSE = {} at h = {}".format(min(mse_list),h_s[np.argmin(mse_list)]))

plt.figure('Bias Square vs h',figsize=(10,8))
plt.plot(h_s, bias_list)
plt.xlabel('h',fontsize=16)
plt.ylabel('bias-square',fontsize=18)
plt.grid()
plt.show()
plt.savefig("bias-square.png")

plt.figure('Variance vs h', figsize=(10,8))
plt.plot(h_s, var_list)
plt.xlabel('h',fontsize=16)
plt.ylabel('Variance',fontsize=16)
plt.grid()
plt.show()
plt.savefig("variance.png")