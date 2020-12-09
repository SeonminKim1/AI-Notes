from tensorflow.keras import models, Input,Model
from tensorflow.keras.layers import Conv2D, ZeroPadding2D, BatchNormalization, \
    MaxPooling2D, Activation, Dense, Add, GlobalAveragePooling2D
import numpy as np

# 일반적인 CBACBAC 구조
# 1x1 dimension으로 차원축소 => 3x3 conv => 1x1 dimension으로 차원확대
def resnetConv2D(x, filters=64, strides=(1,1), filters_scale=1):
    filters = filters*filters_scale
    x = Conv2D(filters, (1,1), strides=strides, padding='valid')(x)
    x = BatchNormalization()(x)
    x = Activation('relu')(x)

    x = Conv2D(filters, (3,3), strides=(1,1), padding='same')(x)
    x = BatchNormalization()(x)
    x = Activation('relu')(x)

    x = Conv2D(4*filters, kernel_size=(1,1), strides=(1,1), padding='valid')(x)
    return x

# 3x3 패딩을 한 이유는 7x7로 kernel로 씌우기 위함
# stride 2x2가 되면, 이미지가 절반크기로 감소
# batch normalization paramter는 전단계의 output featuremap수 *4 = [gamma weights, beta weights, moving_mean(non-trainable), moving_variance(non-trainable)]
def resnetConv1(x):
    x = ZeroPadding2D(padding=(3, 3))(x) # 230,230 이미지
    x = Conv2D(64, (7, 7), strides=(2, 2), padding='valid')(x) #
    x = BatchNormalization()(x)
    x = Activation('relu')(x)
    x = ZeroPadding2D(padding=(1, 1))(x)
    return x

# maxpooling으로 이미지 크기 56으로 만들고 시작
# resnetConv2D는 filter scale 이 즉 feature map 갯수가 배수증가 관련배수
# block 2
def resnetConv2(x):
    x = MaxPooling2D((3,3),2)(x) # 56,56

    shortcut = x # shortcut 생성
    for i in range(3):
        if i==0:
            # x는 CCC 3개가 반영된것, SC는 반영되기 전
            x = resnetConv2D(x, strides=(1,1), filters_scale=1) # 64 필터
            x = BatchNormalization()(x)

            # Skip connection 4배로했을 떄의 결과를 구함 ------------------------------------
            shortcut = Conv2D(256, kernel_size=(1,1), strides=(1,1), padding='valid')(shortcut)
            shortcut = BatchNormalization()(shortcut)
            # ----------------------------------------------------------------------------

            # 둘을 더하고 Activation relu 입힘.
            x = Add()([x, shortcut])
            x = Activation('relu')(x)

            shortcut = x

        else: # shortcut 초기화 굳이 안한 것
            x = resnetConv2D(x, strides=(1,1), filters_scale=1)
            x = BatchNormalization()(x)

            # 둘을 더하고 Activation relu 입힘.
            x = Add()([x, shortcut])
            x = Activation('relu')(x)

            shortcut = x
    return x

# block 3
def resnetConv3(x):
    shortcut = x

    for i in range(4):
        # 초기 shortcut 정의 및 resnet 기본
        if i == 0:
            x = resnetConv2D(x, strides=(2, 2), filters_scale=2) # 128 feature map
            x = BatchNormalization()(x)

            # shortcut 정의
            shortcut = Conv2D(512, kernel_size=(1, 1), strides=(2, 2), padding='valid')(shortcut)
            shortcut = BatchNormalization()(shortcut)

            # 둘 합연산
            x = Add()([x, shortcut])
            x = Activation('relu')(x)
            shortcut = x

        else:
            x = resnetConv2D(x, strides=(1, 1), filters_scale=2)
            x = BatchNormalization()(x)

            x = Add()([x, shortcut])
            x = Activation('relu')(x)

            shortcut = x
    return x

# block 4
def resnetConv4(x):
    shortcut = x

    for i in range(6):
        if i == 0:
            x = resnetConv2D(x, strides=(2, 2), filters_scale=4) # 256
            x = BatchNormalization()(x)

            shortcut = Conv2D(filters=1024, kernel_size=(1, 1), strides=(2, 2), padding='valid')(shortcut)
            shortcut = BatchNormalization()(shortcut)

            # x + shortcut 더하기
            x = Add()([x, shortcut])
            Activation('relu')(x)
            shortcut = x

        else:
            x = resnetConv2D(x, strides=(1, 1), filters_scale=4) # 256
            x = BatchNormalization()(x)

            x = Add()([x, shortcut])
            x = Activation('relu')(x)

            sc = x

    return x

# block5
def resnetConv5(x) :
    shortcut = x

    for i in range(3) :
        if i == 0 :
            x = resnetConv2D(x,strides = (2,2),filters_scale = 8) # 512
            x = BatchNormalization()(x)

            shortcut = Conv2D(filters = 2048, kernel_size = (1,1), strides = (2,2),padding = 'valid')(shortcut)
            shortcut = BatchNormalization()(shortcut)

            # x + shortcut
            x = Add()([x,shortcut])
            x = Activation('relu')(x)
            shortcut = x
        else :
            x = resnetConv2D(x, strides = (1,1),filters_scale = 8)
            x = BatchNormalization()(x)

            x = Add()([x, shortcut])
            x = Activation('relu')(x)

            shortcut = x
    return x
# main
if __name__ == "__main__":
    _input = Input(shape=(224,224,3))
    x = resnetConv1(_input)
    x = resnetConv2(x)
    x = resnetConv3(x)
    x = resnetConv4(x)
    x = resnetConv5(x)
    x = GlobalAveragePooling2D()(x)

    # K => Number of Classes
    K=10
    _output = Dense(K, activation='softmax')(x)

    model = Model(_input, _output)
    model.summary()