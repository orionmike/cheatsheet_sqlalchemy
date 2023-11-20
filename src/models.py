import datetime
from typing import Annotated, List, Optional

from sqlalchemy import ForeignKey, text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database import Base

intpk = Annotated[int, mapped_column(primary_key=True)]
created_at = Annotated[datetime.datetime, mapped_column(
    server_default=text("TIMEZONE('utc', now())"))]
updated_at = Annotated[datetime.datetime, mapped_column(
    server_default=text("TIMEZONE('utc', now())"),
    onupdate=datetime.datetime.utcnow
)]


class Object(Base):
    __tablename__ = "object"

    id: Mapped[intpk]
    name: Mapped[str]

    category_id: Mapped[int] = mapped_column(ForeignKey("category.id", ondelete="CASCADE"))

    category: Mapped["CategoryObject"] = relationship(
        back_populates="object",
    )

    tags: Mapped[List["TagObject"]] = relationship(
        back_populates="object",
    )

    created_at: Mapped[created_at]
    updated_at: Mapped[updated_at]


class CategoryObject(Base):
    __tablename__ = "category"

    id: Mapped[intpk]
    name: Mapped[str]

    # objects: Mapped[list["Object"]] = relationship(
    #     back_populates="objects",
    # )

    created_at: Mapped[created_at]
    updated_at: Mapped[updated_at]


class TagObject(Base):
    __tablename__ = "tag"

    id: Mapped[intpk]
    name: Mapped[str]

    # objects: Mapped[list["Object"]] = relationship(
    #     back_populates="objects",
    # )
    created_at: Mapped[created_at]
    updated_at: Mapped[updated_at]
