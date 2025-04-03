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
4. 화면 구현하기 전에 task로 조회했던거 task_id로 변경
   * task_id는 객체 변환 없이 그냥 넘기자
5. 화면 구현하기
   * 처음 jinja2로 랜더링 할때 get_all로 넘기자
   * create, delete, modify 함수 ajax 구현
6. 카테고리 분류 ai 추가