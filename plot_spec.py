import numpy as np

alpha=26*np.pi/180.
beta=-24*np.pi/180.
phi=0*np.pi/180

linespmm=100
m=3

beta_arr=np.linspace(0*np.pi/180,30*np.pi/180,100)

def lam(alpha,beta,m,linespmm):
        return ((np.sin(alpha)-np.sin(beta))/(m*linespmm))*1000

def blaze(alpha,beta,m,phi):
        beta_=beta-phi
        alpha_=alpha-phi
        blaze=(np.sin(m*np.pi*np.cos(phi)*(np.sin(alpha_)+np.sin(beta_))/2*np.tan(phi)*np.cos(alpha_)))**2/(m*np.pi*np.cos(phi)*(np.sin(alpha_)+np.sin(beta_))/2*np.tan(phi)*np.cos(alpha_))**2
        
        return blaze
     

v=np.pi*np.cos(phi)

lam_arr=[]
blaze_arr=[]
for beta in beta_arr:
        l=lam(alpha,beta,m,linespmm)
        lam_arr.append(l)
        blaze_val=blaze(alpha,beta,m,phi)
        blaze_arr.append(blaze_val)
lam_arr=np.array(lam_arr)
blaze_arr=np.array(blaze_arr)   

# beta_=beta-phi
# alpha_=alpha-phi

# blaze=np.sin(m*np.pi*np.cos(phi)*(np.sin(alpha_)+np.sin(beta_))/2*np.tan(phi)*np.cos(alpha_))**2\
# /(m*np.pi*np.cos(phi)*(np.sin(alpha_)+np.sin(beta_))/2*np.tan(phi)*np.cos(alpha_))
