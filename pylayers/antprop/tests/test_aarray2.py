from pylayers.antprop.aarray import *
import matplotlib.pyplot as plt 
print('--------------')
print('antprop/test_aarray2.py')
print('--------------')
#
# This is a uniform array (10 x 10)
#
fGHz = 6
lamda = 0.3/6
A1 = AntArray(tarr='UA',N=[10,1,1],dm=[0.04,0.0,0],fGHz=fGHz)
A2 = AntArray(tarr='UA',N=[1,1,10],dm=[0,0.0,0.04],fGHz=fGHz)
A1.eval()
f1,a1 = A1.plotG()
f1.savefig('ArrayDiag.png')
f2,a2 = A1.show()
f2.savefig('ArrayConfig.png')

Nrays = 100
theta = np.pi*np.random.rand(Nrays)
phi = 2*np.pi*np.random.rand(Nrays)
A1.eval(grid=False,th=theta,ph=phi)
plt.figure()
plt.imshow(np.angle(A1.Ft[:,:,0]),cmap='jet',interpolation='nearest')
plt.colorbar()
plt.figure()
plt.imshow(np.angle(A1.Fp[:,:,0]),cmap='jet',interpolation='nearest')
plt.colorbar()
#plt.axis('auto')