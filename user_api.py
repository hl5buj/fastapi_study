# user_api.py
from fastapi import FastAPI

# FastAPI 애플리케이션 인스턴스 생성
# 이 객체가 전체 애플리케이션의 중심이 됩니다
app = FastAPI(
    title="My First FastAPI",  # API 문서에 표시될 제목
    description="FastAPI 학습을 위한 첫 프로젝트",
    version="1.0.0"
)


# 더미 데이터베이스 (나중에 실제 DB로 교체)
USERS_DB = {
    1: {"name": "김철수", "email": "kim@example.com", "role": "admin"},
    2: {"name": "이영희", "email": "lee@example.com", "role": "user"},
    3: {"name": "박민수", "email": "park@example.com", "role": "user"},
}


@app.get("/users/{user_id}")
def get_user(user_id: int):
    """
    사용자 ID로 정보 조회
    
    Args:
        user_id: 조회할 사용자 ID
    
    Returns:
        사용자 정보 또는 에러 메시지
    
    예시:
        GET /users/1 → 김철수 정보
        GET /users/99 → {"error": "User not found"}
    """
    # DB에서 사용자 찾기
    user = USERS_DB.get(user_id)
    
    if user is None:
        # 사용자가 없으면 에러 응답
        return {
            "error": "User not found",
            "user_id": user_id
        }
    
    # 사용자 정보 반환
    return {
        "user_id": user_id,
        **user  # dict unpacking으로 name, email, role 펼침
    }


@app.get("/users")
def list_users(role: str = None):
    """
    모든 사용자 목록 조회 (역할별 필터링 가능)
    
    Args:
        role: 필터링할 역할 (admin, user 등)
    
    예시:
        GET /users → 전체 사용자
        GET /users?role=admin → 관리자만
    """
    # 역할 필터링 - list comprehension 사용
    if role:
        filtered_users = {
            user_id: user
            for user_id, user in USERS_DB.items()
            if user["role"] == role
        }
        return {
            "total": len(filtered_users),
            "filter": role,
            "users": filtered_users
        }
    
    # 전체 사용자
    return {
        "total": len(USERS_DB),
        "users": USERS_DB
    }