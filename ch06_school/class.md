## 수업구상
1. 1대 N 관계에 대한 설명
2. 각 모델을 판서로 정의한다.
3. pk, fk를 선정한다.
4. 패키지 나누기
    * web
    * service
    * data
    * model
5. department model 구현하기
6. department data 구현하기
4. department web 구현하기
   * 다중 라우팅
5. department service 구현하기
6. 예외 처리하기
    * 학과를 만들 때 같은 이름이 이미 존재하는지 확인 후 저장
    * 학과를 삭제할 때, 그 학과에 소속된 학생들도 함께 삭제해야 한다면?
7. student model 구현하기
8. student web 구현하기
9. student service 구현하기
    * 학과 등록할 때 학과 정원 초과면 예외
8. ml : 학과 자동 분류
9. 화면구현