import numpy as np
import glob
from keras.preprocessing import image

#input string img_path, returns tensors list of 6 slices of image
def get_tensors(file_name):
    tensor_stack = []
    img = image.load_img(file_name[0], target_size=(260, 1344))
    img_arr = np.array(img)
    list_of_tensors = []
    for i in range(0,6):
        slice_show = i
        slice_size = 1344/6
        img_slice = img_arr[:224, slice_size * slice_show:slice_size * (slice_show + 1), :]
        list_of_tensors.append(np.expand_dims(img_slice, axis=0).astype('float32')/255)
    tensor_stack.append(np.vstack(list_of_tensors))
    tensor_stack = np.array(tensor_stack).reshape(1,6,224,224,3)
    return tensor_stack
