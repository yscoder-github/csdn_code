import tensorflow as tf 
tf.enable_eager_execution()

input = tf.random_normal(shape=(2, 3, 4)) # shape [2, 3, 4]
slice1 = tf.slice(input, [0, 0, 0], [-1, 1, -1]) # shape [2, 1, 4] 切取第二个维度下的第一组数据
slice2 = tf.slice(input, [0, 1, 0], [-1, 1, -1]) # shape [2, 1, 4] 切取第二个维度下的第二组数据
slice3 = tf.slice(input, [0, 2, 0], [-1, 1, -1]) # shape [2, 1, 4] 切取第二个维度下的第三组数据
slice5 = tf.slice(input, [0, 0, 0], [-1, 2, -1]) # shape [2, 2, 4] 切取第二个维度下的前两组数据
slice6 = tf.slice(input, [0, 0, 0], [-1, 3, -1]) # shape [2, 3, 4] 切取第二个维度下的前三组数据
print("\ninput is: \n{}".format(input))
print("\nslice1 is:\n {}".format(slice1))
print("\nslice2 is:\n {}".format(slice2))
print("\nslice3 is:\n {}".format(slice3))
print("\nslice5 is:\n {}".format(slice5))
print("\nslice6 is:\n {}".format(slice6))


'''
input is: 
[[[-1.1159433   1.1852196  -1.02887    -1.6216067 ]
  [ 0.37896946 -1.1322068  -0.34731     0.4213005 ]
  [-0.8697083   0.83150536  0.33464772 -1.1267416 ]]

 [[ 0.88379246  1.090028    0.23926906  0.854103  ]
  [ 0.26111332  1.2733405   0.63280314 -0.8038424 ]
  [ 1.0581269  -0.6792132   0.72982126 -1.4329162 ]]]

slice1 is:
 [[[-1.1159433   1.1852196  -1.02887    -1.6216067 ]]

 [[ 0.88379246  1.090028    0.23926906  0.854103  ]]]

slice2 is:
 [[[ 0.37896946 -1.1322068  -0.34731     0.4213005 ]]

 [[ 0.26111332  1.2733405   0.63280314 -0.8038424 ]]]

slice3 is:
 [[[-0.8697083   0.83150536  0.33464772 -1.1267416 ]]

 [[ 1.0581269  -0.6792132   0.72982126 -1.4329162 ]]]

slice5 is:
 [[[-1.1159433   1.1852196  -1.02887    -1.6216067 ]
  [ 0.37896946 -1.1322068  -0.34731     0.4213005 ]]

 [[ 0.88379246  1.090028    0.23926906  0.854103  ]
  [ 0.26111332  1.2733405   0.63280314 -0.8038424 ]]]

slice6 is:
 [[[-1.1159433   1.1852196  -1.02887    -1.6216067 ]
  [ 0.37896946 -1.1322068  -0.34731     0.4213005 ]
  [-0.8697083   0.83150536  0.33464772 -1.1267416 ]]

 [[ 0.88379246  1.090028    0.23926906  0.854103  ]
  [ 0.26111332  1.2733405   0.63280314 -0.8038424 ]
  [ 1.0581269  -0.6792132   0.72982126 -1.4329162 ]]]

'''