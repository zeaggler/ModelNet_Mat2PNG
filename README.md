# README

## how to convert .MAT with 3D structure, such as 60×60×60, to .PNG

this code is to generate multiview images from multiview mats, which can be converted from original ModelNet .OFF files. 

The multiview mat files can be obtained by:

https://github.com/zeaggler/ModelNet_OFF2MAT

## ATTENTION:

​    THIS IS CODE IS COMPLETED IN WIN10...

​    SO please change the path style '\\\\\' in Linux

## USAGE

* Modelnet_mat2png_singlefile.py

  For single .MAT file,  you can run it directly to convert XX.mat to XX.png. Also, I uploaded two .MAT files to let it pass.

  

* Modelnet_mat2png_Modelnet10.py

  For ModelNet10 dataset, you can convert the .MAT files to .PNG files at one time, but the file path should be changed for different OS. This code is written in win10, so the path has '\\\\', but for Ubuntu, you should change it to '/'.

  

  My dataset path is: 

  ```
  -ModelNet10_voxelized_mat
  
      |--bathtub
  
          |--- bathtub_0001
  
              |---- bathtub_0001_01.mat
  
              |---- bathtub_0001_02.mat
  
                          ...
  
              |---- bathtub_0001_32.mat
  
         |--- bathtub_0002
  
              |---- bathtub_0002_01.mat
  
              |---- bathtub_0002_02.mat
  
                          ...
  
              |---- bathtub_0002_32.mat
  
          .....
  
          |--- bathtub_0300
  
              |---- bathtub_0300_01.mat
  
              |---- bathtub_0300_02.mat
  
                          ...
  
              |---- bathtub_0300_32.mat
  
      |--bed
  
          |--- bed_0001
  
              |---- bed_0001_01.mat
  
              |---- bed_0001_02.mat
  
                          ...
  
              |---- bed_0001_32.mat
  
  ```



​    

\### Target path ###

```
- ModelNet10_voxel_32views

    |--bathtub

        |--- bathtub_0001

            |---- bathtub_0001_01.png

            |---- bathtub_0001_02.png

                        ...

            |---- bathtub_0001_32.png

        |--- bathtub_0002

            |---- bathtub_0002_01.png

            |---- bathtub_0002_02.png

                        ...

            |---- bathtub_0002_32.png

        .....

        |--- bathtub_0300

            |---- bathtub_0300_01.png

            |---- bathtub_0300_02.png

                        ...

            |---- bathtub_0300_32.png

    |--bed

        |--- bed_0001

            |---- bed_0001_01.png

            |---- bed_0001_02.png

                        ...

            |---- bed_0001_32.png

```



