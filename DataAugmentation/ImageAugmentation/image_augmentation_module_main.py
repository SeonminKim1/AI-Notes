from tensorflow.keras.preprocessing.image import ImageDataGenerator
from PIL import Image
import numpy as np
import argparse
import os

# Parser 인자
def init_parser():
    parser = argparse.ArgumentParser(description='Augmentation options' +
                                                 'featurewise_center, samplewise_center, featurewise_std_normalization, samplewise_std_normalization' +
                                                 'rotation_range, width_shift_range, height_shift_range' +
                                                 'brightness_range, shear_range, zoom_range, channel_shift_range' +
                                                 'fill_mode, cval, validation_split, horizontal_flip, vertical_flip' +
                                                 'rescale, data_format')
    parser.add_argument('--path', type=str, required=True, help='path is required option')
    parser.add_argument('--multiple', type=int, required=True, help='Mutiple Information is required option')
    parser.add_argument('--result_type', type=str, required=True, help='Results png or npy?')
    parser.add_argument('--image_size', type=int, required=True, help='image width, hegith are required')

    parser.add_argument('--featurewise_center', type=bool, default=False)
    parser.add_argument('--samplewise_center', type=bool, default=False)
    parser.add_argument('--featurewise_std_normalization', type=bool, default=False)
    parser.add_argument('--samplewise_std_normalization', type=bool, default=False)

    parser.add_argument('--rotation_range', type=int, default=0)
    parser.add_argument('--width_shift_range', type=float, default=0.0)
    parser.add_argument('--height_shift_range', type=float, default=0.0)

    parser.add_argument('--brightness_range', type=tuple, default=None)
    parser.add_argument('--shear_range', type=float, default=0.0)
    parser.add_argument('--zoom_range', type=float, default=0.0)
    parser.add_argument('--channel_shift_range', type=float, default=0.0)
    parser.add_argument('--fill_mode', type=str, help='constant, nearest, reflect, wrap', default='nearest')
    parser.add_argument('--cval', type=float, default=0.0)
    parser.add_argument('--validation_split', type=float, default=0.0)

    parser.add_argument('--horizontal_flip', type=bool, default=False)
    parser.add_argument('--vertical_flip', type=bool, default=False)
    parser.add_argument('--rescale', type=float, default=0.0)
    parser.add_argument('--data_format', type=str, help='channels_last, channels_first', default=None)

    args = parser.parse_args()
    return args

# 증강 데이터 Augmentation Module
class ImageAugmentation:
    def __init__(self, args):
        self.make_datagen(args)

    def make_datagen(self, args):
        print(args)
        if not os.path.isdir(os.getcwd()+'\Aug_images'):
            print('폴더 생성완료')
            os.mkdir(os.getcwd()+'\Aug_images')

        # data generator 정의
        datagen = ImageDataGenerator(
            featurewise_center=args.featurewise_center, samplewise_center=args.samplewise_center,
            featurewise_std_normalization=args.featurewise_std_normalization, samplewise_std_normalization=args.samplewise_std_normalization,
            rotation_range=args.rotation_range, zoom_range=args.zoom_range,
            width_shift_range=args.width_shift_range, height_shift_range=args.height_shift_range,
            brightness_range=args.brightness_range, shear_range=args.shear_range,
            channel_shift_range=args.channel_shift_range, fill_mode=args.fill_mode,
            cval=args.cval, horizontal_flip=args.horizontal_flip,
            vertical_flip=args.vertical_flip, rescale=args.rescale, data_format=args.data_format,
            validation_split=args.validation_split
        )

        # datagen 객체 및 플로우 생성 / 자동으로 라벨링도 해줌
        obj = datagen.flow_from_directory(
            directory=args.path,
            save_to_dir='Aug_images',
            save_prefix='aug_',
            save_format='jpg',  # args.result_type,
            target_size=(args.image_size, args.image_size))

        # 이미지 생성완료
        for i in range(args.multiple):
            img, label = obj.next()
        print(args.multiple,'배 이미지 증강완료')

if __name__ == "__main__":
    print('------Image Augment System------\n')
    args = init_parser() # parser 객체 반환
    ia = ImageAugmentation(args)

# 명령어
# python image_augmentation_module_main.py --path=data --multiple=3 --result_type='.jpg' --image_size=32 --rotation_range=35 --width_shift_range=0.2 --height_shift_range=0.2 --shear_range=0.2 --zoom_range=0.2 --vertical_flip=True --samplewise_center=True --samplewise_std_normalization=True

# 사용법
# 1. 구조
#   - image_augmentation_module_main.py
#   - data 폴더
#   - Aug_images 폴더

# 2. data 폴더 안에 데이터셋이 존재
# 3. Aug_images 폴더에 증강 이미지 생성


