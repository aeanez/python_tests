"""
#Ejemplo de un tensor unidimensional

import numpy as np
import tensorflow as tf

arr = np.array([1, 5.5, 3, 15, 20])
tensor = tf.convert_to_tensor(arr,tf.float64)

print (tensor)

sess = tf.Session()
 
print(sess.run(tensor))
print(sess.run(tensor[1]))
"""
#definir un tensor multidimensional
# import numpy as np
# import tensorflow as tf

# arr = np.array([(1, 5.5, 3, 15, 20),(10, 20, 30, 40, 50), (60, 70, 80, 90, 100)])

# tensor = tf.convert_to_tensor(arr)

# sess = tf.Session()
# print(sess.run(tensor))


#Matematicas con tensores
# import numpy as np
# import tensorflow as tf

# arr1 = np.array([(1,2,3),(4,5,6)])
# arr2 = np.array([(7,8,9),(10,11,12)])
# arr3 = tf.add(arr1,arr2)

# sess = tf.Session()
# tensor = sess.run(arr3)
# print(tensor)

#multiplicar matrices
# import numpy as np
# import tensorflow as tf

# arr1 = np.array([(1,2,3),(4,5,6)])
# arr2 = np.array([(7,8,9),(10,11,12)])
# arr3 = tf.multiply(arr1,arr2)
 
# sess = tf.Session()
# tensor = sess.run(arr3)
# print(tensor)

#procesar imagenes con matplotlib
# import tensorflow as tf
# import matplotlib.image as img
# import matplotlib.pyplot as plot
 
# myfile = "imagen.png" 
# myimage = img.imread(myfile)

# slice = tf.placeholder("int32",[None,None,4])

# cropped = tf.slice(myimage,[10,0,0],[16,-1,-1])
 
# print(myimage.ndim)
# print(myimage.shape)

# sess = tf.Session()
# result = sess.run(cropped, feed_dict={slice: myimage})
# plot.imshow(result)
# plot.show()


#transponer imagenes usando tensorflow
import tensorflow as tf
import matplotlib.image as img
import matplotlib.pyplot as plot

myfile = "imagen.png"
myimage = img.imread(myfile)
 
image = tf.Variable(myimage,name='image')
vars = tf.global_variables_initializer()

sess = tf.Session()

flipped = tf.transpose(image, perm=[1,0,2])

sess.run(vars)
result=sess.run(flipped)

plot.imshow(result)

plot.show()



























