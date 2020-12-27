
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


### Image Augmentation 기법들
- Crop(잘라내기)
    - 이미지를 작게 잘라낸 부분을 보통 패치(patch)라고 함.
    - 제한된 데이터만으로 최고의 성능을 내야할 떄 많이 사용
    - 랜덤하게 패치를 잘라내는 것도 좋고, 어느 정도 규칙을 두고 잘라내는 것도 좋음

- Rotation
    - 많이하지는 않음. CNN의 크기가 어느정도 커지면 회전이 들어간 데이터도 잘 분류함. 하지만 넣어서 나쁠건 없음!

- Shifting(translate)
    - 상하좌우로 몇픽셀식 이동. (~10px~)
    - 발생하는 빈공간에 대해 (fill_mode 옵션)
        - 0으로 채우기(zero filling), 근접한 픽셀로 채우기(nearest neighbor), 밀려난 부분을 가져와 채우기 (rolling)

- flipping
    - horizontal_flip(가로뒤집기), vertical_flip(세로뒤집기)
    - 거의 좌우반전을 많이 사용

- shearing
    - 강제로 사진을 찌그러뜨리기 (사각형을 평행사변형으로 만드는 느낌) -20~20

- Color modification
    - 색감을 바꾸는 작업 (RGB값을 바꾸는 것)
    - RGB에 랜덤 노이즈를 무작위로 더해주기만 해도 이상한 색감이 됨
    - 각 이미지에 PCA를 통해 찾은 중요 성분들만큼 랜덤하게 더해주면 좀 더 좋음 (AlexNet에서 처음 사용)
    
- Image Preprocessing
    - Zero centering, Scailing
        - 훈련 데이터에 대해, 평균 이미지를 구하고 평균으로 다 빼줌.
        - 각 픽셀에 들어갈 값이 평균 0이 되도록 함 / [0,255]를 [0,1]이나 [-1,1]로 바꿈
        - 평균이 0이라 하더라도 입력의 범위(dynamic range)가 너무 넓으면 훈련이 안되기 때문
        - featurewise_center(전체 이미지에 대해 zero centering)
        - samplewise_center(각각 이미지에 대해 zero centering)
    
    - Contrast Normalization (대비 표준화)

        - 다양한 이미지로 학습하는 경우 이미지마다 밝기와 환경이 다름
        - 이것을 어느정도 통일해 주는 것이 대비 표준화
        - 표준화란 평균을 빼고 표준편차로 나눠주는 것이며 전체 픽셀들의 분포가 평균이 0이고 분산이 1인 정규분포로 바뀌게 됨
        - 전체 이미지에 대해서 하는것 (GCN, Global Contrast Normalization), feature-wise_std_normalization
        - 각각의 이미지에 대해서 하는 것(LCN, Local Contrast Normalization), sample-wise_std_normalization
    - Whitening(백색화)
        - 각 픽셀들의 상관관게를 거의 없애고 싶을 때 사용
        - 백색화중 가장 많이 사용되는 백색화는 ZCA Whitening
        - 과거 RGB값의 평균을 뺴주어 사실상 input의 전체 평균이 0이 되버리게 만드는 과거 방법 (VGG 제안) -> Batch Normalization이 나오고 나선 사라짐
        