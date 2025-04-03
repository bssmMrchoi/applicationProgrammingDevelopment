from transformers import pipeline

classifier = pipeline("zero-shot-classification", model="typeform/distilbert-base-uncased-mnli")
# 미리 정의한 카테고리
CATEGORIES = ["공부", "운동", "업무", "개인", "쇼핑"]

def predict_category(text: str) -> dict:
    """
    주어진 텍스트를 기반으로 가장 적절한 카테고리를 예측한다.
    :param text: 사용자의 할 일 텍스트
    :return: 예측된 카테고리와 전체 점수 딕셔너리
    """
    result = classifier(text, CATEGORIES)
    top_label = result["labels"][0]
    score_map = dict(zip(result["labels"], result["scores"]))
    return {
        "predicted_category": top_label,
        "scores": score_map
    }