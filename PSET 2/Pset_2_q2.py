# -*- coding: utf-8 -*-
"""
Created on Sun Jan 21 11:03:21 2018

@author: Riddhima Mishra
"""


import numpy as np
import pandas as pd
import sklearn

sick=pd.read_csv('sick.txt')
sick.shape
sick=pd.DataFrame(sick)

y = sick['sick'] 




#   define a function to calculate the log likelihood
def Log_Likelihood(guess, true, n):
    error = true-guess
    sigma = np.std(error)
    f = ((1.0/(2.0*math.pi*sigma*sigma))**(n/2))* \
        np.exp(-1*((np.dot(error.T,error))/(2*sigma*sigma)))
    return np.log(f)


#   define criteria function
def crit(var,*args):
    #   load my  data
    yGuess = var[0] + var[1]*sick['age'] + var[2]*sick['children'] + var[3]*sick['avgtemp_winter']
    f = Log_Likelihood(yGuess, y, float(len(yGuess)))
    return (-1*f)

#  Let's pick some random starting points for the optimization    
nvar = 4
var = np.zeros(nvar)
var[0] = -15.5
var[1] = 19.5
var[2] = -1.0
var[3] = 2
mle_args=(y)
#  maximize the likelihood (minimize -1*max(likelihood)
from scipy.optimize import minimize
res = minimize(crit, var, method='BFGS',
                options={'disp': True})

print(res)


#Log liklihood value and estimates

yGuess = var[0] + var[1]*sick['age'] + var[2]*sick['children'] + var[3]*sick['avgtemp_winter']

Log_Likelihood(yGuess, y, float(len(yGuess)))

error = y - yGuess
sigma = np.std(error)
print(sigma)

## ques 2

var[0] = 1
var[1] = 0
var[2] = 0
var[3] = 0

yGuess_n= var[0] + var[1]*sick['age'] + var[2]*sick['children'] + var[3]*sick['avgtemp_winter']

log_lik_h0 = Log_Likelihood(yGuess_n,y,float(len(yGuess_n)))
log_lik_mle = Log_Likelihood(yGuess, y, float(len(yGuess)))
LR_val = 2 * (log_lik_mle - log_lik_h0)
pval_h0 = 1.0 - sts.chi2.cdf(LR_val, 2)
print('chi squared of H0 with 2 degrees of freedom p-value = ', pval_h0)




