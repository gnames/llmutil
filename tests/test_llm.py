import numpy
from llm import embed


def test_embed():
    res = embed.embed(['one', 'two', 'three'])
    assert len(res) == 3
    assert len(res[0]) == 768
    assert isinstance(res[0][0], numpy.float32)


def test_cross_embed():
    tests = [
        ("Dogs are cute", "Dogs are beautiful"),
        ("Dogs are cute", "Kats are lazy"),
        ("Do Bald eagles migrate?", """d may
move nomadically, presumably because they are
not tied to the defense of a nest site. Adult birds, in
contrast, migrate when food becomes unavailable.
Bald Eagles generally migrate alone but
occasionally join other migrants on the wing, but
not in kettles or flocks (Buehler 2000).
Bald Eagle migration is quite varied between
geographic areas and appears to be influenced by
availability of food and severity of climate. Young
tend to migrate before adults (Buehler 2000).
Migrants from non-breeding populations that
frequent Texas, like those from Saskatchewan,
winter in a broad region of the southwestern U. S.,
ranging from California to Texas (Gerrard et al.
1974, Gerrard et al. 1978, Griffin et al. 1980). Some
adults from these northern populations might not
migrate but instead move locally to seasonal food
sources. Bald Eagles that su mm er around the Great
Lakes and adjacent areas in Canada migrate south
along major river systems from Augu"""),

    ]
    res = embed.cross_embed(tests)
    assert res[0] > 0.7
    assert res[1] < 0.2
    assert res[2] > 0.5
