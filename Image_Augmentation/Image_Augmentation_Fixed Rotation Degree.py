import os
from glob import glob
from PIL import Image

dir_path = 'dataset/dirty_mnist_2nd/'
glob_path = dir_path + '*.png'

rotate_path = 'dataset/rotation_image/'

rotate_degree = 90 # 270

# glob - file dir list
data_paths = glob(glob_path)
print(len(data_paths))

# file name list
fname_ls = os.listdir(dir_path)
print(len(fname_ls))

for i, path in enumerate(data_paths):
    img = Image.open(path)
    rotated = img.rotate(rotate_degree)
    # ../data/dirty_mnist_2nd/00037_rotated90.png
    rotated.save(rotate_path + str(os.path.splitext(fname_ls[i])[0]) \
                 + '_rotated' + str(rotate_degree) + '.png')

    if i % 5000 == 0:
        print(i, '완료', end=' ')
