#Create more training data by rotating, cropping and flipping images in the dataset
def training_generation(img):
  img = tf.image.random_crop(value=img, size=(2,2,3))
  img = tf.keras.preprocessing.image.random_rotation(img.numpy(), 90, row_axis=0, col_axis=1,channelaxis=2)
  img = tf.image.random_flip_left_right(img)
  img = tf.image.random_flip_up_down(img)
