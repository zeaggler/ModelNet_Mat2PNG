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

####Original path###
- ModelNet10_voxelized_mat
	--bathtub
		--- bathtub_0001
			---- bathtub_0001_01.mat
			---- bathtub_0001_02.mat
						...
			---- bathtub_0001_32.mat
		--- bathtub_0002
			---- bathtub_0002_01.mat
			---- bathtub_0002_02.mat
						...
			---- bathtub_0002_32.mat
		.....
		--- bathtub_0300
			---- bathtub_0300_01.mat
			---- bathtub_0300_02.mat
						...
			---- bathtub_0300_32.mat
	--bed
		--- bed_0001
			---- bed_0001_01.mat
			---- bed_0001_02.mat
						...
			---- bed_0001_32.mat
			
####Target path###
- ModelNet10_voxel_32views
	--bathtub
		--- bathtub_0001
			---- bathtub_0001_01.png
			---- bathtub_0001_02.png
						...
			---- bathtub_0001_32.png
		--- bathtub_0002
			---- bathtub_0002_01.png
			---- bathtub_0002_02.png
						...
			---- bathtub_0002_32.png
		.....
		--- bathtub_0300
			---- bathtub_0300_01.png
			---- bathtub_0300_02.png
						...
			---- bathtub_0300_32.png
	--bed
		--- bed_0001
			---- bed_0001_01.png
			---- bed_0001_02.png
						...
			---- bed_0001_32.png
#################################################'''

import numpy as np
import mayavi.mlab as mlab
from scipy.io import loadmat
import time, os

ModelNet_filepath = 'F:\DATA3D\ModelNet10_voxelized_mat'
ModelNet_voxel_32 = 'F:\DATA3D\ModelNet10_voxel_32views'

# classpath for ModelNet10, change for your own dataset
inclass = ['bathtub', 'bed', 'chair', 'desk', 'dresser', 'monitor',
           'sofa', 'table', 'toilet', 'night_stand']

# function: voxel mat 2 image(.png)
def voxel_mat2img(voxel_mat, voxel_img_savepath, voxelmat_name):
	if not os.path.exists(voxel_img_savepath):
		os.makedirs(voxel_img_savepath)
		print('voxel_image save path has been created')
	else:
		# print('voxel_image save path exists')
		pass
	
	voxel_savename = voxelmat_name.split('.')[0]
	voxel_savepath = voxel_img_savepath + '\\' + voxel_savename + '.png'


	if os.path.exists(voxel_savepath):
		print(voxel_savepath, '********exist******')
	else:
		mlab.clf()
		mlab.contour3d(voxel_mat)
		f = mlab.gcf()
		mlab.savefig(voxel_savepath)
		print(voxel_savepath, 'saved##############')


# convert modelnet10_voxelized_mat to modelnet10_voxel_32views
def main():
	ModelNet_classpath = os.listdir(ModelNet_filepath)
	for classpath_index in ModelNet_classpath:
		if classpath_index in inclass:
			# 'F:\DATA3D\ModelNet10_voxelized_mat\bathtub'
			voxelmat_class_ = ModelNet_filepath + '\\' + classpath_index	
			voxelmat_class_list = os.listdir(voxelmat_class_)
			# bathtub_0001.off bathtub_0002.off bathtub_0003.off ....
			for voxelmat_list_index in voxelmat_class_list:
					# 'F:\DATA3D\ModelNet10_voxelized_mat\bathtub\\bathtub_0001.off\\bathtub_0001'
					voxelmat_list_ = voxelmat_class_ + '\\' + voxelmat_list_index
					# bathtub_0001_01.mat bathtub_0001_02.mat bathtub_0001_03.mat ...
					voxelmat_list_mats = os.listdir(voxelmat_list_)
					for lists_ in voxelmat_list_mats:
						# 'F:\DATA3D\ModelNet10_voxelized_mat\bathtub\\bathtub_0001.off\\bathtub_0001\\bathtub_0001_01.mat'
						voxelmat_lists_ = voxelmat_list_ + '\\' + lists_
						voxelmat_ = loadmat(voxelmat_lists_)['instance']

						# convert each voxelmat_ to voxel_png
						voxel_img_savepath = ModelNet_voxel_32 + '\\' + classpath_index + '\\' + voxelmat_list_index
						voxel_mat2img(voxelmat_, voxel_img_savepath, lists_)
						time.sleep(0.01)


if __name__ == '__main__':
	main()
