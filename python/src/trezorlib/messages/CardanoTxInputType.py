# Automatically generated by pb2py
# fmt: off
from .. import protobuf as p

if __debug__:
    try:
        from typing import Dict, List  # noqa: F401
        from typing_extensions import Literal  # noqa: F401
    except ImportError:
        pass


class CardanoTxInputType(p.MessageType):

    def __init__(
        self,
        *,
        prev_hash: bytes,
        prev_index: int,
        address_n: List[int] = None,
    ) -> None:
        self.address_n = address_n if address_n is not None else []
        self.prev_hash = prev_hash
        self.prev_index = prev_index

    @classmethod
    def get_fields(cls) -> Dict:
        return {
            1: ('address_n', p.UVarintType, p.FLAG_REPEATED),
            2: ('prev_hash', p.BytesType, p.FLAG_REQUIRED),
            3: ('prev_index', p.UVarintType, p.FLAG_REQUIRED),
        }
