import joblib
from transformers import pipeline

# model = joblib.load("todo_classifier.joblib")
# vectorizer = joblib.load("vectorizer.joblib")

classifier = pipeline("zero-shot-classification", model="typeform/distilbert-base-uncased-mnli")
# 미리 정의한 카테고리
CATEGORIES = ["공부", "운동", "업무", "개인", "쇼핑"]

if __name__ == '__main__':
    # X = vectorizer.transform(['시험 공부하기'])
    # category = model.predict(X)[0]
    # print(category)
    # X = vectorizer.transform(['은행 계좌 개설'])
    # category = model.predict(X)[0]
    # print(category)
    # X = vectorizer.transform(['fastapi 수업 복습하기'])
    # category = model.predict(X)[0]
    # print(category)
    result = classifier('시험 공부', CATEGORIES)
    top_label = result["labels"][0]
    print(top_label)
    print(dict(zip(result["labels"], result["scores"])))
    result = classifier('은행 계좌 개설', CATEGORIES)
    top_label = result["labels"][0]
    print(top_label)
    print(dict(zip(result["labels"], result["scores"])))
    result = classifier('fastapi 수업 복습', CATEGORIES)
    top_label = result["labels"][0]
    print(top_label)
    print(dict(zip(result["labels"], result["scores"])))
