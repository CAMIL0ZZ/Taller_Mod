from sqlmodel import SQLModel, Field
from kind import Kind


class MascotaBase(SQLModel):
    name: str = Field(..., min_length=3, max_length=50)
    age: int = Field(..., ge=0)
    kind: Kind = Field(default=Kind.BIRD)


class MascotaResponse(MascotaBase):
    id: int | None = None


class MascotaUpdate(SQLModel):
    name: str | None = Field(default=None, min_length=3, max_length=50)
    age: int | None = Field(default=None, ge=0)
    kind: Kind | None = None


"""
from sqlmodel import SQLModel, Field
from kind import Kind


class MascotaBase(SQLModel):
    name: str = Field(..., min_length=3, max_length=50)
    age: int = Field(..., ge=0)
    kind: Kind = Field(default=Kind.BIRD)


class Mascota(MascotaBase, table=True):
    id: int | None = Field(default=None, primary_key=True)


class MascotaUpdate(SQLModel):
    name: str | None = Field(default=None, min_length=3, max_length=50)
    age: int | None = Field(default=None, ge=0)
    kind: Kind | None = None
"""