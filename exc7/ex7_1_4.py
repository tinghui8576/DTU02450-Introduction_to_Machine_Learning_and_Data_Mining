from toolbox_02450 import mcnemar
from ex7_1_1 import *

# Compute the Jeffreys interval
alpha = 0.05
[thetahat, CI, p] = mcnemar(y_true,  yhat[:,1], yhat[:,0],alpha=alpha)

print("theta = theta_A-theta_B point estimate", thetahat, " CI: ", CI, "p-value", p)

alpha = 0.05
[thetahat, CI, p] = mcnemar(y_true, yhat[:,2],  yhat[:,0],alpha=alpha)

print("theta = theta_A-theta_C point estimate", thetahat, " CI: ", CI, "p-value", p)