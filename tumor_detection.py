import tensorflow as tf
from tensorflow.keras.preprocessing import image
import numpy as np
def names(number):
    if number==0:
        return 'Its a Tumor'
    else:
        return 'No, Its not a Tumor'
def detect(img_path):
    model=tf.keras.models.load_model('models/model.h5')
    test_image=image.load_img(img_path,target_size=(128,128))
    test_image=image.img_to_array(test_image)
    test_image=np.expand_dims(test_image,axis=0)
    result=model.predict(test_image)
    classification = np.where(result == np.amax(result))[1][0]
    return str(result[0][classification]*100) + '% Chance ' + names(classification)