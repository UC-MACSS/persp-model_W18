# -*- coding: utf-8 -*-
"""
Created on Mon Jan 22 18:46:42 2018

@author: Riddhima Mishra
"""

cd C:\cygwin64\home\Riddhima Mishra\persp-model_W18\ProblemSets\PS3

Ques 1

import numpy as np
import scipy.stats as sts

pts = np.loadtxt('incomes.txt')

pts


#Ques 1 
import matplotlib.pyplot as plt
%matplotlib inline
count, bins, ignored = plt.hist(pts, 30, edgecolor='black', normed=True)
plt.title('Income distribution', fontsize=20)
plt.xlabel('Income')
plt.ylabel('Percent of income')
plt.savefig('Income distribution')


# Defining function for pdf

def log_norm_pdf(xvals, mu, sigma):
    pdf_vals    = (1/(xvals * sigma * np.sqrt(2 * np.pi))) *\
					np.exp( - (np.log(xvals) - mu)**2 / (2 * sigma**2))
    return pdf_vals


    

# Data moments

def data_moments(xvals):
    mean_data = xvals.mean()
    std_data = xvals.std()
    return mean_data, std_data

# Model moments
    
def model_moments(mu, sigma):
    xfx = lambda x: x * log_norm_pdf(x, mu, sigma)
    (mean_model, m_m_err) = intgr.quad(xfx, 0, 150000)
    x2fx = lambda x: ((x - mean_model) ** 2) * log_norm_pdf(x, mu, sigma)
    (var_model, v_m_err) = intgr.quad(x2fx, 0, 150000)
    std_model = np.sqrt(var_model)
    return mean_model, std_model



# Error Vector
    
def err_vec(xvals, mu, sigma, simple):
    mean_data, var_data = data_moments(xvals)
    moms_data = np.array([[mean_data], [var_data]])
    mean_model, var_model = model_moments(mu, sigma)
    moms_model = np.array([[mean_model], [var_model]])
    if simple:
        err_vec = moms_model - moms_data
    else:
        err_vec = (moms_model - moms_data) / moms_data
    return err_vec

# Criteria function

def criterion(params, *args):
    mu, sigma = params
    xvals,  W = args
    err = err_vec(xvals, mu, sigma, simple=False)
    crit_val = np.dot(np.dot(err.T, W), err)
    return crit_val

 

## using initial mu and sigma values from PSet 2 to estimate the parameters of the lognormal
# distribution using GMM
     
mu_1 = 11
sig_1 = 0.5


params_1 = np.array([mu_1, sig_1])
W_hat = np.eye(2)
gmm_args = (pts, W_hat)
results = opt.minimize(criterion, params_1, args=(gmm_args),
                       method='L-BFGS-B', bounds=((1e-10, None), (1e-10, None)))
mu_GMM1, sig_GMM1 = results.x
print('mu_GMM1=', mu_GMM1, ' sig_GMM1=', sig_GMM1)

# Plotting the graph

count, bins, ignored = plt.hist(pts, 30, edgecolor='black', normed=True)
plt.title('Income distribution', fontsize=20)
plt.xlabel('Income')
plt.ylabel('Percent of income')
    
    
dist_pts= np.linspace(0, 150000, 200)
plt.plot(dist_pts, log_norm_pdf(dist_pts, mu_GMM1, sig_GMM1),
         linewidth=2, color='m', label='$\mu$= mu_GMM' '$\sigma$ = sig_GMM' )
plt.legend(loc='upper left')
plt.show()

#Value of the criterion function

mu = mu_GMM1
sig = sig_GMM1

params = np.array([mu, sig])
w = np.eye(2)
args = (pts, w)

crt_fun_val = criterion(params, *args)
print(crt_fun_val)

#Data moments and model moments at the estimated parameter values

#Data moments

datamom= np.array(data_moments(pts))
print('Data momemnt:', datamom)

#model moments

modmom= np.array(model_moments(mu_GMM1, sig_GMM1))
print('Model moments:', modmom)

#comparing data and model moments

err= err_vec(pts, mu_GMM1, sig_GMM1, False)
print("Comparing data and model moments by error term:", err)


##c

#Estimator for the variance covariance matrix

vcv= np.dot(err, err.T) / pts.shape[0]
print(vcv)


#two step estimator for the optimal matrix

W_hat2 = lin.pinv(vcv)  
print(W_hat2)

#estimates 

params_1 = np.array([mu_GMM1, sig_GMM1])
W_hat3 = np.array([[1. / vcv[0, 0], 0.], [0., 1. / vcv[1, 1]]])
gmm_args = (pts, W_hat3)
results = opt.minimize(criterion, params_1, args=(gmm_args),
                       method='L-BFGS-B', bounds=((1e-10, None), (1e-10, None)))
mu_GMM2, sig_GMM2 = results.x
print('mu_GMM2=', mu_GMM2, ' sig_GMM2=', sig_GMM2)

#criterion value

mu = mu_GMM2
sig = sig_GMM2

params = np.array([mu, sig])
w = np.eye(2)
args = (pts, w)

crt_fun_val = criterion(params, *args)
print(crt_fun_val)



# Plots

count, bins, ignored = plt.hist(pts, 30, edgecolor='black', normed=True)
plt.title('Income distribution', fontsize=20)
plt.xlabel('Income')
plt.ylabel('Percent of income')
    
    
dist_pts= np.linspace(0, 150000, 200)
plt.plot(dist_pts, log_norm_pdf(dist_pts, mu_GMM1, sig_GMM1),
         linewidth=2, color='m', label='$\mu$= mu_GMM1' '$\sigma$ = sig_GMM1' )
plt.legend(loc='upper left')
plt.show()

dist_pts= np.linspace(0, 150000, 200)
plt.plot(dist_pts, log_norm_pdf(dist_pts, mu_GMM2, sig_GMM2),
         linewidth=2, color='r', label='$\mu$= mu_GMM2' '$\sigma$ = sig_GMM2' )
plt.legend(loc='upper left')
plt.show()

#Data moments and model moments comparision


#Data moments

datamom= np.array(data_moments(pts))
print('Data momemnt:', datamom)

#model moments

modmom2= np.array(model_moments(mu_GMM2, sig_GMM2))
print('Model moments 2:', modmom2)

#comparing data and model moments

err2= err_vec(pts, mu_GMM2, sig_GMM2, False)
print("Comparing data and model moments by error term 2:", err2)

# D

#Defining new datamoments

def data_moments3(xvals):
    bpct_1_dat = xvals[xvals < 75000].shape[0] / xvals.shape[0]
    bpct_2_dat = (xvals[(xvals >=75000) & (xvals < 100000)].shape[0] /
                  xvals.shape[0])
    bpct_3_dat = (xvals[xvals >=100000].shape[0] /
                  xvals.shape[0])

    return bpct_1_dat, bpct_2_dat, bpct_3_dat


#Model moments

def model_moments3(mu, sigma):
    xfx = lambda x: x *log_norm_pdf(x, mu, sigma)
    (bpct_1_mod, bp_1_err) = intgr.quad(xfx, 0, 75000)
    (bpct_2_mod, bp_2_err) = intgr.quad(xfx, 75000, 100000)
    (bpct_3_mod, bp_3_err) = intgr.quad(xfx, 100000, 150000)
    
    return bpct_1_mod, bpct_2_mod, bpct_3_mod
    

#err vector
    
def err_vec3(xvals, mu, sigma, simple):
    
    bpct_1_dat, bpct_2_dat, bpct_3_dat = \
        data_moments3(xvals)
    moms_data = np.array([[bpct_1_dat], [bpct_2_dat], [bpct_3_dat]])
    bpct_1_mod, bpct_2_mod, bpct_3_mod = \
        model_moments3(mu, sigma)
    moms_model = np.array([[bpct_1_mod], [bpct_2_mod], [bpct_3_mod]])
    if simple:
        err_vec = moms_model - moms_data
    else:
        err_vec = 100 * ((moms_model - moms_data) / moms_data)
    
    return err_vec


def criterion3(params, *args):
    mu, sigma = params
    xvals, W = args
    err = err_vec3(xvals, mu, sigma, simple=False)
    crit_val = np.dot(np.dot(err.T, W), err) 
    
    return crit_val


##GMM estimator
    
w = np.eye(3)
params_1 = np.array([mu_1, sig_1])

gmm_args = (pts,w)
results = opt.minimize(criterion3, params_1, args=(gmm_args),
                       method='L-BFGS-B', bounds=((1e-10, None), (1e-10, None)))
mu_GMM1_3, sig_GMM1_3 = results.x
print('mu_GMM1_3=', mu_GMM1_3, ' sig_GMM1_3=', sig_GMM1_3)

# Plotting the graph

count, bins, ignored = plt.hist(pts, 30, edgecolor='black', normed=True)
plt.title('Income distribution', fontsize=20)
plt.xlabel('Income')
plt.ylabel('Percent of income')
    
    
dist_pts= np.linspace(0, 150000, 200)
plt.plot(dist_pts, log_norm_pdf(dist_pts, mu_GMM1_3, sig_GMM1_3),
         linewidth=2, color='m', label='$\mu$= mu_GMM' '$\sigma$ = sig_GMM' )
plt.legend(loc='upper left')
plt.show()

#Value of the criterion function

params = np.array([mu_GMM1_3, sig_GMM1_3])
print('Value of criterion function: ', criterion3(params, pts, np.eye(3)))

#Data moments and model moments at the estimated parameter values

#Data moments

datamom= np.array(data_moments3(pts))
print('Data momemnt:', datamom)

#model moments

modmom= np.array(model_moments3(mu_GMM1_3, sig_GMM1_3))
print('Model moments:', modmom)

#comparing data and model moments

err3= err_vec3(pts, mu_GMM1_3, sig_GMM1_3, False)
print("Comparing data and model moments by error term:", err3)



#e

#variance co-variance matrix

VCV2_3 = np.dot(err3, err3.T) / pts.shape[0]
print(VCV2_3)

#two-step estimator for optimal weighting matrix

W_hat2_3 = lin.pinv(VCV2_3)  
print(W_hat2_3)


#Estimates from optimal matrix

params_init = np.array([mu_GMM1_3, sig_GMM1_3])
gmm_args = (pts, W_hat2_3)
results2_3 = opt.minimize(criterion3, params_init, args=(gmm_args),
                       method='L-BFGS-B', bounds=((1e-10, None), (1e-10, None)))
mu_GMM2_3, sig_GMM2_3 = results2_3.x
print('mu_GMM2_3=', mu_GMM2_3, ' sig_GMM2_3=', sig_GMM2_3)
results2_3


#Criterion value 

params = np.array([mu_GMM2_3, sig_GMM2_3])
print('Value of criterion function: ', criterion3(params, pts, np.eye(3)))

#Plotting the graph

count, bins, ignored = plt.hist(pts, 30, edgecolor='black', normed=True)
plt.title('Income distribution', fontsize=20)
plt.xlabel('Income')
plt.ylabel('Percent of income')
    
    
dist_pts= np.linspace(0, 150000, 500)
plt.plot(dist_pts, log_norm_pdf(dist_pts, mu_GMM1_3, sig_GMM1_3),
         linewidth=2, color='m', label='$\mu$= mu_GMM' '$\sigma$ = sig_GMM' )
plt.legend(loc='upper left')
plt.show()



dist_pts= np.linspace(0, 150000, 500)
plt.plot(dist_pts, log_norm_pdf(dist_pts, mu_GMM2_3, sig_GMM2_3),
         linewidth=2, color='r', label='$\mu$= mu_GMM' '$\sigma$ = sig_GMM' )
plt.legend(loc='upper left')
plt.show()

#Data moments

datamom= np.array(data_moments3(pts))
print('Data momemnt:', datamom)

#model moments

modmom= np.array(model_moments3(mu_GMM2_3, sig_GMM2_3))
print('Model moments:', modmom)

#comparing data and model moments

err3= err_vec3(pts, mu_GMM2_3, sig_GMM2_3, False)
print("Comparing data and model moments by error term:", err3)


##Ques 2

#Loading the data

import numpy as np
import pandas as pd
import sklearn

sick=pd.read_csv('sick.txt')

def err_lin(xvals, params, simple):
    moms_data= np.array(sick['sick'])
    
    b0, b1, b2, b3 = params
    yGuess = b0 + b1*sick['age'] + b2* sick['children'] + b3 * sick['avgtemp_winter']
    #moms_model = np.array([yGuess])
    moms_model= yGuess
    
    if simple:
        err_vec = moms_model - moms_data
    else:
        err_vec = 100 * ((moms_model - moms_data) / moms_data)
    
    return err_vec
    
  
    
def criterion_lin(params, *args):
    b0, b1, b2, b3 = params
    xvals, W = args
    err = err_lin(xvals, params, simple=False)
    crit_val = np.dot(np.dot(err.T, W), err) 
    
    return crit_val



    

init_params= np.array([0,1,-1,-1])

w = np.eye(200)

gmm_args = (sick,w)
results = opt.minimize(criterion_lin, init_params, args=(gmm_args),
                       method='L-BFGS-B')
b0_GMM, b1_GMM, b2_GMM, b3_GMM = results.x

print('b0_GMM=', b0_GMM, ' b1_GMM=', b1_GMM, ' b2_GMM=', b2_GMM, ' b3_GMM=', b3_GMM)



#Value of the criterion function

params = np.array([b0_GMM, b1_GMM, b2_GMM, b3_GMM])
print('Value of criterion function: ', criterion_lin(params, sick, np.eye(200)))






















































































































































































































