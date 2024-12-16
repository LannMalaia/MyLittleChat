from datetime import datetime
from typing import List, Optional
import reflex as rx
import sqlmodel


class Changed_Character(rx.Model, table=True):
    # id는 pk로 자동생성
    user_id: int = sqlmodel.Field(foreign_key="user.id") # 만든 유저
    is_public: bool
    is_npc: bool
    name: str
    desc: str
    good_symbol: str
    good_symbol_aspect: str
    bad_symbol: str
    bad_symbol_aspect: str
    identity_aspect: str
    problem_aspect: str
    aspect: str
    stat: str
    skill: str

    user: Optional["User"] = sqlmodel.Relationship(
        back_populates="user"
    )

class Chat(rx.Model, table=True):
    # id는 pk로 자동생성
    session_id: int = sqlmodel.Field(foreign_key="session.id")
    character_id: int | None = sqlmodel.Field(foreign_key="character.id")
    user_id: int | None = sqlmodel.Field(foreign_key="user.id") # 채팅중인 유저
    cre_date: datetime

    session: Optional["Session"] = sqlmodel.Relationship(
        back_populates="session"
    )
    character: Optional["Character"] = sqlmodel.Relationship(
        back_populates="character"
    )
    user: Optional["User"] = sqlmodel.Relationship(
        back_populates="user"
    )

class Character(rx.Model, table=True):
    # id는 pk로 자동생성
    user_id: int = sqlmodel.Field(foreign_key="user.id") # 만든 유저
    is_public: bool
    is_npc: bool
    name: str
    desc: str
    good_symbol: str
    good_symbol_aspect: str
    bad_symbol: str
    bad_symbol_aspect: str
    identity_aspect: str
    problem_aspect: str
    aspect: str
    stat: str
    skill: str

    user: Optional["User"] = sqlmodel.Relationship(
        back_populates="user"
    )

class Session(rx.Model, table=True):
    # id는 pk로 자동생성
    scenario_id: int = sqlmodel.Field(foreign_key="scenario.id") # 만든 유저
    summary: str
    is_finished: bool
    
    scenario: Optional["Scenario"] = sqlmodel.Relationship(
        back_populates="scenario"
    )

class Scenario(rx.Model, table=True):
    # id는 pk로 자동생성
    room_id: int = sqlmodel.Field(foreign_key="room.id") # 만든 유저
    is_template: bool
    scale: str
    genre: str
    desc: str
    problems: str
    targets: str
    symbols: str
    characters: str
    aspects: str
    
    room: Optional["Room"] = sqlmodel.Relationship(
        back_populates="room"
    )
    sessions: Optional[List[Session]] = sqlmodel.Relationship(
        back_populates="scenario"
    )


class Room(rx.Model, table=True):
    # id는 pk로 자동생성
    user_id: int = sqlmodel.Field(foreign_key="user.id") # 만든 유저
    
    user: Optional["User"] = sqlmodel.Relationship(
        back_populates="user"
    )
    scenarios: Optional[List[Scenario]] = sqlmodel.Relationship(
        back_populates="room"
    )

class User(rx.Model, table=True):
    # id는 pk로 자동생성, -1은 슈퍼유저
    account_id: str
    password: str
    username: str

    characters: Optional[List[Character]] = sqlmodel.Relationship(
        back_populates="user"
    )
    rooms: Optional[List[Room]] = sqlmodel.Relationship(
        back_populates="user"
    )
    chats: Optional[List[Chat]] = sqlmodel.Relationship(
        back_populates="user"
    )