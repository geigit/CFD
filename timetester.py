import numpy
#from oned_nonlinear import *
from gpu_cavity import *

#nx = numpy.linspace(15,17,3)
#nx = 2**nx*1000
nx = numpy.array([41, 64, 128, 256])

for i in nx:
    main(i)
    print 'Completed run of %d elements' % (int(i))
