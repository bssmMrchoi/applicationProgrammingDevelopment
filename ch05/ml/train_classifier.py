import pandas as pd
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.metrics import classification_report

# 📥 CSV 불러오기
df = pd.read_csv("todo_data.csv")

# 🎯 텍스트와 레이블 분리
texts = df["content"]
labels = df["category"]

# ✂️ 학습/테스트 분할
X_train, X_test, y_train, y_test = train_test_split(texts, labels, test_size=0.2, random_state=42)

# 🧪 파이프라인 (벡터화 + 분류기)
pipeline = Pipeline([
    ("tfidf", TfidfVectorizer()),
    ("clf", MultinomialNB())
])

# 🧠 학습
pipeline.fit(X_train, y_train)

# 🔍 평가
y_pred = pipeline.predict(X_test)
print(classification_report(y_test, y_pred))

# 💾 모델과 벡터 저장
joblib.dump(pipeline.named_steps['tfidf'], "vectorizer.joblib")
joblib.dump(pipeline.named_steps['clf'], "todo_classifier.joblib")
