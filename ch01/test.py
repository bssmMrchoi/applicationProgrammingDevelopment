from typing import List, Tuple, Dict, Optional, Union


def add(a: int, b: int) -> int:
    return a + b


def process_numbers(numbers: List[int]) -> List[int]:
    return [n * 2 for n in numbers]


def get_person_info() -> Tuple[str, int]:
    return ("Alice", 25)


def get_student_scores() -> Dict[str, float]:
    return {"Alice": 95.5, "Bob": 88.0}


def find_user(user_id: int) -> Optional[str]:
    users = {1: "Alice", 2: "Bob"}
    return users.get(user_id)  # 존재하지 않으면 None 반환


def square_or_length(value: Union[int, str]) -> int:
    if isinstance(value, int):
        return value ** 2
    return len(value)


if __name__ == "__main__":
    result1 = add(1, 2)
    result2 = add("1", "2")
    print(result1)
    print(result2)
    print(square_or_length(10))
    print(square_or_length("10"))