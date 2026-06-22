"""Auth endpoints — register, login, token refresh, me"""
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_db
from app.models.user import User
from app.schemas.auth import RegisterRequest, LoginRequest
from app.utils.security import hash_password, verify_password, create_access_token, create_refresh_token, decode_token

router = APIRouter()
security = HTTPBearer()


def build_user_response(user: User) -> dict:
    return {
        "id": str(user.id),
        "email": user.email,
        "role": user.role,
        "company_name": user.company_name,
        "contact_name": user.contact_name,
        "verified": user.verified,
    }


async def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security),
    db: AsyncSession = Depends(get_db),
) -> User:
    """Extract and validate JWT, return User"""
    payload = decode_token(credentials.credentials)
    if not payload or payload.get("type") != "access":
        raise HTTPException(status_code=401, detail="Invalid or expired token")

    user_id = payload.get("sub")
    result = await db.execute(select(User).where(User.id == user_id))
    user = result.scalar_one_or_none()
    if not user:
        raise HTTPException(status_code=401, detail="User not found")
    return user


# ── POST /api/auth/register ────────────────────────────────────────────
@router.post("/register", status_code=status.HTTP_201_CREATED)
async def register(body: RegisterRequest, db: AsyncSession = Depends(get_db)):
    # Check duplicate email
    existing = await db.execute(select(User).where(User.email == body.email))
    if existing.scalar_one_or_none():
        raise HTTPException(status_code=400, detail="Email already registered")

    user = User(
        email=body.email,
        password_hash=hash_password(body.password),
        role=body.role,
        company_name=body.company_name,
        contact_name=body.contact_name,
    )
    db.add(user)
    await db.commit()
    await db.refresh(user)

    # TODO: Send verification email via SendGrid
    return {"data": build_user_response(user)}


# ── POST /api/auth/login ───────────────────────────────────────────────
@router.post("/login")
async def login(body: LoginRequest, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(User).where(User.email == body.email))
    user = result.scalar_one_or_none()
    if not user or not verify_password(body.password, user.password_hash):
        raise HTTPException(status_code=401, detail="Invalid email or password")

    # TODO: Check email verified — return 403 if not
    # if not user.verified:
    #     raise HTTPException(status_code=403, detail="Email not verified")

    user_id = str(user.id)
    return {"data": {
        "access_token": create_access_token(user_id),
        "refresh_token": create_refresh_token(user_id),
        "user": build_user_response(user),
    }}


# ── POST /api/auth/refresh ─────────────────────────────────────────────
@router.post("/refresh")
async def refresh(
    credentials: HTTPAuthorizationCredentials = Depends(security),
    db: AsyncSession = Depends(get_db),
):
    payload = decode_token(credentials.credentials)
    if not payload or payload.get("type") != "refresh":
        raise HTTPException(status_code=401, detail="Invalid or expired refresh token")

    user_id = payload.get("sub")
    result = await db.execute(select(User).where(User.id == user_id))
    if not result.scalar_one_or_none():
        raise HTTPException(status_code=401, detail="User not found")

    return {"data": {"access_token": create_access_token(user_id)}}


# ── GET /api/auth/me ───────────────────────────────────────────────────
@router.get("/me")
async def me(current_user: User = Depends(get_current_user)):
    return {"data": build_user_response(current_user)}


# ── PUT /api/auth/me ───────────────────────────────────────────────────
@router.put("/me")
async def update_me(
    body: dict,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    for field in ("contact_name", "phone", "company_name"):
        if field in body:
            setattr(current_user, field, body[field])
    await db.commit()
    await db.refresh(current_user)
    return {"data": build_user_response(current_user)}
