from cleverman.authent import Authenticator


_test_auth = Authenticator()
_test_auth.Authenticate("XXXX5874", "superpass")


def test_Authenticator():
    assert _test_auth.__class__ != ""


def test_is_authenticated():
    assert _test_auth.is_authenticated() is True

