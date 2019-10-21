from typing import Generic, TypeVar, Iterable, Union, Sequence, List

### -------- Typing for non-generated classes ---------  ###

class Factory:
    @staticmethod
    def produce(key: int) -> Message: ...
    @staticmethod
    def abbrev_from_id(id: int) -> str: ...
    @staticmethod
    def id_from_abbrev(name: str) -> int: ...


class Message:
    def clone(self) -> Message: ...
    def clear(self) -> None: ...
    def validate(self) -> int: ...
    def set_timestamp_now(self) -> float: ...
    @property
    def msg_name(self) -> str: ...
    @property
    def msg_id(self) -> int: ...
    def serialize(self) -> bytes: ...
    def serialize_fields(self) -> bytes: ...
    def fields_equal(self, other: Message) -> bool: ...
    def __init__(self):
        self.timestamp = None  # type: float
        self.src = None  # type: int
        self.src_ent = None  # type: int
        self.dst = None  # type: int
        self.dst_ent = None  # type: int
        self.sub_id = None  # type: int

T = TypeVar('T')
class MessageList(Sequence[T]):
    def set_parent(self, parent: Message) -> None: ...
    def clear(self) -> None: ...
    @property
    def size(self) -> int: ...
    def append(self, msg: T) -> None: ...
    def set_timestamp(self, value: float) -> None: ...
    def extend(self, iterable: Iterable[T]) -> None: ...
    def __len__(self) -> int: ...
    def __iter__(self) -> Iterable[T]: ...
    def __getitem__(self, item) -> Union[T, Iterable[T]]: ...
    def __contains__(self, item) -> bool: ...

class Parser:
    def reset(self) -> None: ...
    def parse(self, data: bytes) -> Union[None, Message]: ...



### -------- Typing for generated bindings ---------  ###

