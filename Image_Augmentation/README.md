
## Image Augmentation Module (이미지 증강 모듈)
### 1. 구조
- image_augmentation_module_main.py
- data 폴더
- Aug_images 폴더

### 2. data 폴더
- 증강하고자 하는 데이터셋들어있음 (폴더 형태 든 , 이미지 파일 형태든 상관없음)

### 3. Aug_images 폴더
- Augmentation된 이미지 생성

## 명령어
    - python image_augmentation_module_main.py --path=data --multiple=3 --result_type='jpg' --image_size=32 --rotation_range=35 --width_shift_range=0.2 --height_shift_range=0.2 --shear_range=0.2 --zoom_range=0.2 --horizontal_flip=True --samplewise_center=True --samplewise_std_normalization=True

## 옵션 설명
- path=data // image path
- multiple=3 // 몇 배수 Augmentation 할건지 (3 => 3배)
- result_type='jpg' // 결과 이미지 파일 jpg, png 등
- image_size=32 // 대상 image 크기
- rotation_range=35 // 회전 정도 0~360
- width_shift_range, height_shift_range = 0.2,0.2 // shift 정도 (0.0 ~ 1.0)
- shear_range=0.2  // 도형 비틀기 정도 (ex-사각형 -> 평행사변형 느낌) (0.0 ~ 1.0)
- zoom_range=0.2 // 배율 (0.0 ~ 1.0)
- horizontal_flip=True // 좌우뒤집기 (상하뒤집기도 가능하지만 거의 안쓰므로 pass..)
- samplewise_center=True // 각각 이미지에 대해 zero centering
- samplewise_std_normalization=True // 각각 이미지에 대한 대비 표준화 (LCN, Local Contrast Normalization)
