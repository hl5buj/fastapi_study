# main.py
from fastapi import FastAPI

# FastAPI 애플리케이션 인스턴스 생성
# 이 객체가 전체 애플리케이션의 중심이 됩니다
app = FastAPI(
    title="My First FastAPI",  # API 문서에 표시될 제목
    description="FastAPI 학습을 위한 첫 프로젝트",
    version="1.0.0"
)


# 루트 경로 엔드포인트
# @app.get("/")은 데코레이터로, "GET 요청이 / 경로로 오면 이 함수 실행"을 의미
@app.get("/")
def read_root():
    """
    루트 경로 핸들러
    
    반환값은 자동으로 JSON으로 변환됩니다.
    Content-Type 헤더도 자동으로 설정됩니다.
    """
    return {
        "message": "Hello, FastAPI! 탁본",
        "docs": "/docs",  # Swagger UI 위치 안내
        "redoc": "/redoc"  # ReDoc 위치 안내
    }


# 경로 파라미터 예제
@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    """
    경로 파라미터와 쿼리 파라미터 예제
    
    Args:
        item_id (int): URL 경로에서 추출되는 항목 ID
                       타입 힌트(int)로 자동 검증 및 변환
        q (str, optional): 쿼리 파라미터 (선택적)
                          기본값 None
    
    Returns:
        dict: 항목 정보를 담은 딕셔너리
    
    예시 요청:
        GET /items/5
        → item_id=5, q=None
        
        GET /items/5?q=test
        → item_id=5, q="test"
        
        GET /items/abc
        → 422 에러 (item_id는 정수여야 함)
    """
    return {
        "item_id": item_id,
        "query": q,
        "type_of_item_id": type(item_id).__name__  # 타입 확인용
    }


# 쿼리 파라미터 여러 개 사용
@app.get("/search")
def search_items(
    keyword: str,  # 필수 파라미터
    skip: int = 0,  # 선택적, 기본값 0
    limit: int = 10  # 선택적, 기본값 10
):
    """
    검색 API 예제
    
    Args:
        keyword: 검색 키워드 (필수)
        skip: 건너뛸 항목 수 (페이지네이션)
        limit: 가져올 최대 항목 수
    
    예시:
        GET /search?keyword=python
        → keyword="python", skip=0, limit=10
        
        GET /search?keyword=python&skip=10&limit=20
        → keyword="python", skip=10, limit=20
    """
    return {
        "keyword": keyword,
        "skip": skip,
        "limit": limit,
        "results": []  # 실제로는 DB 조회 결과
    }
    
    