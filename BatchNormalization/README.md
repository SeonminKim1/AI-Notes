## Batch 학습

- 데이터가 많게 되면 당연히 모든 데이터를 학습 할 수는 없으므로 배치 학습을 진행해야 함.
- 미니 배치를 사용하여 데이터에 포함된 오류에 대해 둔감한 학습 가능  -> 과적합 문제 완화에 도움 
- **근데 배치 학습을 하게되면 배치마다 서로 Output 분포가 다른현상이 발생**
- internal corvariate shift(내부 공변량 이동문제) 현상 발생함 -> 따라서 Batch Nomralization이 필요
- 이전 층들의 학습에 의해 이들 층의 가중치가 바뀌게 되면, 현재 층에 전달되는 데이터의 분포가 현재 층이 학습했던 시점의 분포와 차이가 발생(이전층 현재층 둘다 100단위였는데 갑자기 이전층이 바뀌면서 10단위가 되어버려서 그러면 차이가 발생하니까 애초에 둘다 정규화하여 낮춰놓는 것)

![batch학습문제점](img/batch학습문제점.png)

- 모든 Batch 간에 정규화를 진행함

## Batch Normalization
- 모든 Batch 간에 Normalization을 적용함
- 평균과 분산을 동일하게 함

![Batch_normalization](img/Batch_normalization.png)

## Batch Normalization의 학습
- 정규화
    - 정규화는 데이터의 범위를 0과 1로 변환하여 데이터 분포를 조정하는 방법이다. 
    - (값 - 평균) / 표준편차 작업을 하게 되면 전체가 동일한 스케일이 됨
- 만약 Relu 후에 Batch Normalization을 쓰면 가중치에 대해 Relu는 음수면 없애는 거니까 구한 가중치의 음수 즉 절반이 날라감 -> 추가적인 Scale과 Bias를 학습하여 Activation에 적합한 분포로 변환함 (역전파 알고리즘시 반영됨)
- 정규화를 하게 되면 모두가 동일한 Scaling 으로 학습되기 때문에
    - 학습률이 클시 발산되는 경우나
    - 학습률이 작을때 학습이 안되는 경우등 방지 가능
    
![학습단계_BatchNormalization](img/학습단계_BatchNormalization.png)


## 추론단계
- 추론과정시에는 평균과 분산을 이동 평균하여 고정 ( 아마 Batch 전체 에 대한 평균과 분산) -> 추론시에는 1장씩 할 수 도 있으니까
- 추론단계에서는 정규화와 추가 Scale, Bias를 결합하여 단일 곱, 더하기 연산으로 줄일 수 있음

![추론단계_BatchNormalization](img/추론단계_BatchNormalization.png)

## Batch Normalization 순서
- 배치 정규화 사용시 가중치 초기값에 크게 영향을 받지 않아서, 초깃값 설정에 크게 신경쓸 필요가 없어지고, 학습률을 아주 작게 설정할 필요도 없어, 학습이 빨리 진행되는 경향을 보인다. 또한 과적합을 억제하는 특성이 있어서, 드롭아웃을 사용하지 않아도 성능이 좋은 신경망 모델이 학습될 수도 있음.

![batch_normalization_순서](img/batch_normalization_순서.png)

