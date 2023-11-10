import numpy
from llm import embed


def test_embed():
    res = embed.embed(['one', 'two', 'three'])
    assert len(res) == 3
    assert len(res[0]) == 384
    assert isinstance(res[0][0], numpy.float32)
