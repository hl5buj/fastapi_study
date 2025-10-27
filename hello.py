# hello.py
from fastapi import FastAPI

# FastAPI 애플리케이션 인스턴스 생성
# 이 객체가 전체 애플리케이션의 중심이 됩니다
app = FastAPI(
    title="My First FastAPI",  # API 문서에 표시될 제목
    description="FastAPI 학습을 위한 첫 프로젝트",
    version="1.0.0"
)

@app.get("/add")
def add_numbers(a: int, b: int):
    """
    두 수를 더하는 계산기 API
    
    Args:
        a: 첫 번째 숫자
        b: 두 번째 숫자
    
    Returns:
        계산 결과와 입력값
    
    예시:
        GET /add?a=5&b=3
        → {"a": 5, "b": 3, "result": 8}
    """
    return {
        "a": a,
        "b": b,
        "result": a + b,
        "operation": "addition"
    }


@app.get("/multiply")
def multiply_numbers(a: float, b: float):
    """
    두 수를 곱하는 API (실수 지원)
    
    Args:
        a: 첫 번째 숫자 (실수 가능)
        b: 두 번째 숫자 (실수 가능)
    
    예시:
        GET /multiply?a=3.5&b=2
        → {"result": 7.0}
    """
    return {
        "a": a,
        "b": b,
        "result": a * b,
        "operation": "multiplication"
    }
    
# import uvicorn

# if __name__ == "__main__":
#     uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)