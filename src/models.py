import datetime
from typing import Annotated, Optional


from sqlalchemy import ForeignKey, text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database import Base


intpk = Annotated[int, mapped_column(primary_key=True)]
created_at = Annotated[datetime.datetime, mapped_column(server_default=text("TIMEZONE('utc', now())"))]
updated_at = Annotated[datetime.datetime, mapped_column(
    server_default=text("TIMEZONE('utc', now())"),
    onupdate=datetime.datetime.utcnow,
)]


class Object(Base):
    __tablename__ = "object"

    id: Mapped[intpk]
    name: Mapped[str]

    category: mapped_column(ForeignKey("category.id", ondelete="CASCADE"))

    tags: Mapped[list["TagObject"]] = relationship(
        back_populates="objects",
    )


class CategoryObject(Base):
    __tablename__ = "category"

    id: Mapped[intpk]
    name: Mapped[str]

    objects: Mapped[list["Object"]] = relationship(
        back_populates="objects",
    )


class TagObject(Base):
    __tablename__ = "tag"

    id: Mapped[intpk]
    name: Mapped[str]

    objects: Mapped[list["Object"]] = relationship(
        back_populates="objects",
    )
