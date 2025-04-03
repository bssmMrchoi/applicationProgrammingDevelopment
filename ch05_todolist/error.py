class Missing(Exception):
    def __init__(self, msg):
        super().__init__(msg)
        self.msg = msg


class Duplicate(Exception):
    def __init__(self, msg):
        super().__init__(msg)
        self.msg = msg
# def get_one(task):
#     if task != "todo":
#         raise Missing(msg=f"Creature {task} not found")
#     return "정상 결과"
#
# def web():
#     try:
#         result = get_one("dragon")  # 예외 발생
#         print("이 코드는 실행되지 않음")
#     except Missing as e:
#         print(f"[web] 예외 잡음: {e.msg}")
#
# if __name__ == '__main__':
#     web()