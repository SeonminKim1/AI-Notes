## ■ 손실함수 (Loss Function)
- 신경망 학습에서는 현재의 상태를 '하나의 지표'로 표현하며 그 지표를 가장 좋게 만들어 주는 가중치 매개변수의 값을 탐색하는 것이다.
- **즉 신경망은 '하나의 지표'를 기준으로 최적의 매개변수의 값을 탐색한다.**
- 그 해당 지표를 '손실함수'라고 한다.
- 손실함수는 임의의 함수를 사용할 수도 있지만 일반적으로는 '평균 제곱 오차'와 '교차 엔트로피 오차'를 사용한다.
- **input이들어오고 모델함수를 지나서 output 이 나오면 y^ loss와 실제값 y를 loss 함수를 통해 비교하면서 그 차이를 이용해 w를 update한다.**
- loss 함수는 실제값과 예측값의 차이를 나타내줄수 있는 형태다.
- **loss 함수란 우리가 원하는 파라미터 최적화에 대한 목적함수이다.**
- loss function은 임의의 함수 사용도 가능하나, 일반적으로 모양이 아래로 볼록한(convex) 모양이면 좋다.

- **Loss Function을 추후에 만들게되면 (Convex 모양으로 만들것) ==> 경사하강법에 의한 최솟값을 찾기가 쉽고, 즉 쉽다는 건 최적화가 잘되다는 것 ==> 학습데이터에 편중된 파라미터로 최적화될 가능성이 있다 ==> 제약조건이 필요하다. (regularization penalty) 등장 ** 

### ■ 회귀 손실함수
- (1) Mean Squared Error (MSE)
    ![mse](img/mse.png)
    
    - 오차를 모두 제곱한 다음에 평균 낸 것이 MSE
    - MSE의 정의를 가만히 보면 분산과 똑같은데, 분산은 각 데이터와 평균의 차이를 제곱해서 평균낸 것이다. 
    - **즉 분산은 데이터가 평균으로부터 얼마나 퍼져 있는지를 나타내는 통계치이고, MSE도 데이터가 예측으로부터 얼마나 퍼져있는지를 나타낸다고 할 수 있다.**
    - MSE도 CONVEX 모양 Y=X^2 의 형태니까
    - **제곱을 하는 이유**
        - 두번씩 예측시 오차가 +1, -1인 경우와 / +3, -3가 있다. 이 경우 모두 오차의 평균이 0인데, 엄연히 1과 3의 크기가 다르다. 따라서 오차를 +로 바꿔줄 필요가 있어서 제곱을 하는 것이다. 
   
![mse_img](img/mse_img.png)

- (2) Mean Absolute Error (MAE)
    ![mae](img/mae.gif)

    - MSE 처럼 제곱하는 대신 MAE 처럼 절댓값으로도 가능하다.
    - MAE 도 절댓값이기 때문에 CONVEX 모양임
![mae_img](img/mae_img.png)

- (3) Huber 손실 (후버손실)
    ![huber](img/huber.png)
    - MSE 와 MAE의 절충안인 후버손실로 
    - **일정한 범위(델타라고 함)를 정하고 그 안에 있으면 오차를 제곱하고, 그 밖에 있으면 오차의 절댓값을 구하는 것**
![huber_img](img/huber_img.PNG)

- (4) 기타
    - MSLE (Mean Squared Logarithmic Error)
    - MAPE (Mean Absolute Percentage Error)
    - KLD
    - Poission
    - Lobcosh
    - Cosine Similarity
    
### ■ 분류 손실함수
- (1) Binary Cross Entropy 
    ![binarycrossentropy](img/binarycrossentropy.PNG)
    - 이진 분류기 훈련시 사용. 
    - 손실함수는 예측값과 실제값이 같으면 0이 되어야 한다. 
        - 여기서 말하는 0과 1은 확률임 (0과 1사이의 확률)
        - 위 식에서 예측값과 실제값이 1로 같을 때 loss는 0이 나온다
        - 반대로 예측값이 0 실제값이 1이면 양의 무한대가 나온다 (실제로는 0이 아닌 매우 작은 값이고 양의 무한대가 아닌 매우 큰 양수값)
        - **틀렸을 때 loss가 양의 무한대니까 아 이건 완전히 아니구나가 되는 것!!!**
        
- (2) Categorical cross-entropy
    ![categorical_crossentropy](img/categorical_crossentropy.PNG)
    - 멑티 클래스 분류 시 사용
    - **라벨이 [0,0,1], [1,0,0], [0,1,0] 처럼 one-hot 형태로 제공될때 사용**
    - Binary cross entropy 처럼 틀렸을 때 loss가 양의 무한대로 발산됨.
    
- (3) Sparse categorical cross-entropy
    - 멀티 클래스 분류 시 사용
    - **라벨이 one-hot이 아닌 0,1,2,3,4 와 같이 정수의 형태로 제공될 때 사용**

- categorical vs sparse categorical
    - 두개는 수학적으로는 차이가 없다. 무작위 데이터 많은 경우에서 돌렸을떄 차이x
![sparse_vs_categorical](img/sparse_vs_categorical.png)

- (4) 기타
    - Hinge
    - Squared Hinge
    - Categorical Hinge


### ■ 참고문헌
- https://www.youtube.com/watch?v=kuJROoa4kh8
- https://towardsdatascience.com/understanding-the-3-most-common-loss-functions-for-machine-learning-regression-23e0ef3e14d3
- http://doc.mindscale.kr/km/data_mining/dm02.html
- https://bskyvision.com/822