import numpy as np
import matplotlib.pyplot as plt

def lam(alpha,beta,m,linespmm):
        return ((np.sin(alpha)-np.sin(beta))/(m*linespmm))


def blaze(alpha,beta,m,phi):
        beta_=beta+phi
        alpha_=-alpha+phi
        phi=phi
        #print(np.rad2deg(alpha_),np.rad2deg(beta_),np.rad2deg(phi))
        psi=(m*np.pi*np.cos(phi)*(np.sin(alpha_)+np.sin(beta_)))/(2*np.tan(phi)*np.cos(alpha_))
        blaze=(np.sin(psi)**2)/psi**2
        
        #blaze=(np.sin((m*np.pi*np.cos(phi)*(np.sin(alpha_)+np.sin(beta_)))/(2*np.tan(phi)*np.cos(alpha_)))**2)/(((m*np.pi*np.cos(phi)*(np.sin(alpha_)+np.sin(beta_)))/(2*np.tan(phi)*np.cos(alpha_)))**2)
        
        return blaze


alpha=np.deg2rad(41.5)#32.801
beta_arr=np.linspace(90*np.pi/180,-90*np.pi/180,1000)
beta_arr_plot=np.linspace(90,-90,1000)
linespmm=91.5*0.001#260
m_arr=[3,4,5,6]
c_arr=['red','orange','green','blue']
phi=np.deg2rad(19)#10.3

y_filter=[0.97,1.07]
j_filter=[1.17,1.33]
h_filter=[1.49,1.78]
k_filter=[2.03,2.37]
count=0
for m in m_arr:	
	lam_arr=[]
	blaze_arr=[]
	for beta in beta_arr:
	        l=lam(alpha,beta,m,linespmm)
	        lam_arr.append(l)
	        blaze_val=blaze(alpha,beta,m,phi)
	        blaze_arr.append(blaze_val)
	        
	lam_arr=np.array(lam_arr)
	blaze_arr=np.array(blaze_arr)   
	#plt.plot(-beta_arr_plot,lam_arr)
	#plt.plot(-beta_arr_plot,blaze_arr)
	plt.plot(lam_arr,blaze_arr,c=c_arr[count])
	count=count+1

plt.plot([y_filter[0],y_filter[0]],[0,1],'--',c='blue',label='Y band')
plt.plot([y_filter[1],y_filter[1]],[0,1],'--',c='blue')
plt.plot([j_filter[0],j_filter[0]],[0,1],'--',c='green',label='J band')
plt.plot([j_filter[1],j_filter[1]],[0,1],'--',c='green')
plt.plot([h_filter[0],h_filter[0]],[0,1],'--',c='orange',label='H band')
plt.plot([h_filter[1],h_filter[1]],[0,1],'--',c='orange')
plt.plot([k_filter[0],k_filter[0]],[0,1],'--',c='red',label='K band')
plt.plot([k_filter[1],k_filter[1]],[0,1],'--',c='red')

plt.xlim([0,3])
plt.legend()
plt.show()
