# -*- coding: utf-8 -*-
"""
Created on Sun Jan 21 14:00:41 2018

@author: Riddhima Mishra
"""
#ques 1: 

cd C:\cygwin64\home\Riddhima Mishra\persp-model_W18\ProblemSets\PS2

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


##Ques 2


mu, sigma = 11.0, 0.5 # mean and standard deviation


#Display the histogram of the samples, along with the probability density function:


import matplotlib.pyplot as plt
#count, bins, ignored = plt.hist(s, 30, normed=True, align='mid')

x = np.linspace(0, 150000,200 )

#Log normal function

def log_normal_pdf(x,mu,sigma):
    pdf = (np.exp(-(np.log(x) - mu)**2 / (2 * sigma**2))
       /( x * sigma * np.sqrt(2 * np.pi)))
    return pdf

plt.plot(x, log_normal_pdf(x,mu,sigma), linewidth=2, color='r')
plt.axis('tight')
plt.savefig('logpdf')

#log likelihood value

def log_lik(x, mu, sigma):
    
    log_pdf_vals= log_normal_pdf(x,mu,sigma)
    ln_pdf_vals=np.log(log_pdf_vals)
    log_lik_val= ln_pdf_vals.sum()
    
    return log_lik_val


print('Log Likelihood: ', log_lik(pts,mu, sigma))

#Ques 3

def crit(params, *args):
    mu, sigma = params
    xvals = args
    log_lik_val = log_lik(x, mu, sigma)
    neg_log_lik_val = -log_lik_val
    
    return neg_log_lik_val


import scipy.optimize as opt


mu_init = 11.0  
sig_init = 0.5
params_init = np.array([mu_init, sig_init])
mle_args = (pts)
results = opt.minimize(crit, params_init, args=(mle_args))
mu_MLE, sig_MLE = results.x
print('mu_MLE=', mu_MLE, ' sig_MLE=', sig_MLE)


count, bins, ignored = plt.hist(pts, 30, edgecolor='black', normed=True)
plt.title('Income distribution', fontsize=20)
plt.xlabel('Income')
plt.ylabel('Percent of income')


#plt.plot(x, log_normal_pdf(x,mu,sigma), linewidth=2, color='r')
#plt.axis('tight')

plt.plot(x, log_normal_pdf(x, mu, sigma),
         linewidth=2, color='r', label='1: $\mu$=11.0,$\sigma$=0.5')
plt.legend(loc='upper left')



plt.plot(x, log_normal_pdf(x, mu_MLE, sig_MLE),
         linewidth=2, color='k', label='MLE: $\mu$=mu_MLE,$\sigma$=sig_MLE')
plt.legend(loc='upper left')
plt.savefig('MLEplots.png')



print('MLE Log Likelihood: ', log_lik(pts,mu_MLE, sig_MLE))


results
OffDiagNeg = np.array([[1, -1], [-1, 1]])
vcv_mle = results.hess_inv * OffDiagNeg
stderr_mu_mle = np.sqrt(vcv_mle[0,0])
stderr_sig_mle = np.sqrt(vcv_mle[1,1])
print('VCV(MLE) = ', vcv_mle)
print('Standard error for mu estimate = ', stderr_mu_mle)
print('Standard error for sigma estimate = ', stderr_sig_mle)



##Ques 4: Likelihood ratio test

log_lik_h0 = log_lik(pts,11, 0.5)
log_lik_mle = log_lik(pts, mu_MLE, sig_MLE)
LR_val = 2 * (log_lik_mle - log_lik_h0)
pval_h0 = 1.0 - sts.chi2.cdf(LR_val, 2)
print('chi squared of H0 with 2 degrees of freedom p-value = ', pval_h0)

#chi squared of H0 with 2 degrees of freedom p-value =  0.0

##Ques 5:









































