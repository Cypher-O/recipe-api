from typing import Optional, Dict
from app.schema.api_response import APIResponse

def create_response(
    code: int,
    status: str,
    message: str,
    data: Optional[Dict] = None,
    token: Optional[str] = None
) -> APIResponse:
    return APIResponse(
        code=code,
        status=status,
        message=message,
        data=data,
        token=token
    )
    