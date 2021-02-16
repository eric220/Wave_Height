import networking as nt
import image_work as img
import split_model as mdl
import threading
import datetime
import time
import os

if __name__ == "__main__":
    now = datetime.datetime.now().time()
    if now.hour > 6 and now.hour < 16:
        try:
            station_id = 44008
            x = threading.Thread(target=nt.retrieve_image, args=(station_id,))
            x.start()
            cnn = mdl.get_cnn()
            lstm = mdl.get_lstm()
            x.join()
            file_path = [img.glob.glob('Temp_Img/*.jpg').pop(-1)]
            tensor_stack = img.get_tensors(file_path)
            os.remove(file_path[0])
            cnn_pred = cnn.predict(tensor_stack)
            print(lstm.predict(cnn_pred) + 2)  #experimentally derived addition???model needs work
        except:
            print(err)
    else:
        print('Check camera operation. May be dark at this time')