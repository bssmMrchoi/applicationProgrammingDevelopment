import json
from datetime import datetime

import pymysql
import redis
from fastapi import FastAPI, Body, Path, Request, Query
from fastapi.responses import JSONResponse

app = FastAPI()

redis_client = redis.Redis(host="127.0.0.1", port=6379, db=0)


def get_connection():
    return pymysql.connect(
        host='127.0.0.1',
        user='root',
        password='q1w2e3',
        database='study',
        port=3306
    )


@app.get("/posts")
def get_posts(page: int = Query(1, ge=1), size: int = Query(10, le=100)):
    cache_key = f"posts:page:{page}:size:{size}"
    # 캐시 확인
    cached = redis_client.get(cache_key)
    if cached:
        print("Redis 캐시에서 가져옴")
        # print(cached)
        return {
            "page": page,
            "size": size,
            "total": int(redis_client.get('posts:total')),
            "posts": json.loads(cached)
        }

    # page의 기본값 1, 1 이상(음수 불가)
    # size의 기본값 10, 100 이하
    offset = (page - 1) * size

    conn = get_connection()
    cursor = conn.cursor()

    # 1. 전체 게시글 수 조회 (총 페이지 계산용)
    cursor.execute("SELECT COUNT(*) AS total FROM posts")
    total = cursor.fetchone()
    total = total[0]

    # 2. 페이징된 게시글 가져오기
    cursor.execute(
        "SELECT id, title, created_at FROM posts ORDER BY created_at DESC LIMIT %s OFFSET %s",
        (size, offset)
    )
    posts = cursor.fetchall()

    cursor.close()
    conn.close()

    redis_client.setex('posts:total', 600, total)
    redis_client.setex(cache_key, 600, json.dumps(posts, default=serialize_datetime))

    return {
        "page": page,
        "size": size,
        "total": total,
        "posts": posts
    }

def serialize_datetime(obj):
    if isinstance(obj, datetime):
        return obj.isoformat()
    return obj

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("post_web:app", reload=True)
