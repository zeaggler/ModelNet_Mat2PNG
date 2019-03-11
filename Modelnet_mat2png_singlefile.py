'''#################################################
README:
	this code is to generate multiview images from
	multiview mats, which can be converted from
	original ModelNet .OFF files. 
	The multiview mat files can be obtained by:
	https://github.com/zeaggler/ModelNet_OFF2MAT

ATTENTION:
	THIS IS CODE IS COMPLETED IN WIN10...
	SO please change the path style '\\' in Linux

####Original file###
bathtub_0001_01.mat

####Target file###
bathtub_0001_01.png

#################################################'''

import numpy as np
import mayavi.mlab as mlab
from scipy.io import loadmat
import time, os

mat_filepath = 'bathtub_0107_16.mat'


# function: voxel mat 2 image(.png)
def voxel_mat2img(mat_filepath, png_filepath):
	mlab.clf()
	mlab.contour3d(mat_filepath)
	f = mlab.gcf()
	mlab.savefig(png_filepath)
	print(png_filepath, 'saved ##############')


if __name__ == '__main__':
	voxelmat_ = loadmat(mat_filepath)['instance']
	png_filepath = mat_filepath.split('.')[0] + '.png'
	voxel_mat2img(voxelmat_, png_filepath)
