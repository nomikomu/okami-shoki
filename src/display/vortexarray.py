import time
import numpy as np

startTime=time.time()
array= np.zeros((512,512,512),dtype=np.uint8)
print('Time: %s' % (time.time() - startTime))
print('Bytes: %s' % str(array.nbytes))

