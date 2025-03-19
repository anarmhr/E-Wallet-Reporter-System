from pydantic import BaseModel, Field


class SqlRequest(BaseModel):
    request_id: str
    user_query: str


class SqlResponse(BaseModel):
    request_id: str = Field(default=None)
    sql: str
    info: str
    need_verification: bool


class DataResponse(BaseModel):
    request_id: str
    info: str
    data: dict
