## 수업구상
1. 지난 시간에 했던 service, data, model 가져오기
    * insert, select all 에 대한 내용
2. endpoint 만들기
   * main 파일 만들어 app과 router 분리
   * 전체 조회(get), 할일 입력(post) 구현
   * 단건 조회(get-{task}) 기능 구현
   * 단건 수정(patch-{task}) 기능 구현: completed 값 반전
   * 단건 삭제(delete) 기능 구현
3. 예외 처리 관리 하기
   * 기본 Exception as e로 처리하기
   * error 파일을 만들어 따로 관리하기