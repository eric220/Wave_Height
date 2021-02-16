import keras
from keras.layers import Dense, LSTM, Flatten, TimeDistributed, Conv2D, Dropout, MaxPooling2D
from keras import Sequential
from keras.applications.mobilenet import MobileNet
import keras.metrics as metrics

def get_cnn():
    mn = MobileNet(include_top=False, weights='imagenet', input_shape=(224, 224, 3))
    model = Sequential()
    model.add(TimeDistributed(mn, input_shape=(6, 224, 224, 3)))
    model.add(TimeDistributed(MaxPooling2D(pool_size=(2, 2), strides=(2, 2))))
    model.add(TimeDistributed(MaxPooling2D()))
    model.add(TimeDistributed(Flatten()))
    return model

def get_lstm():
    lstm = Sequential()
    lstm.add(LSTM(128, return_sequences = True, input_shape = (6, 1024), dropout = .4))
    lstm.add(LSTM(128, dropout = .2))
    lstm.add(Dense(1))
    lstm.compile(loss='mse', optimizer='adam', metrics = [metrics.mean_squared_error])
    lstm.load_weights('base_model.hdf5')
    return lstm