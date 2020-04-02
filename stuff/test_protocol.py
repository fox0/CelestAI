# pylint: skip-file
import pytest

from protocol_pb2 import MessagePingRequest, MessagePingResponse
from protocol import pack, unpack_header, unpack, LEN_HEADER


@pytest.fixture()
def message1():
    m = MessagePingRequest()
    m.message = 'hello'
    return m


def test_pack(message1):
    src = 0x0001
    dest = 0x0002
    packet = pack(src, dest, message1)
    assert packet == b'\x01\x00\x01\x00\x02\x00\x07\n\x05hello'


def test_pack0():
    src = 0x0001
    dest = 0x0002
    m = MessagePingResponse()
    m.message = 'hello'
    packet = pack(src, dest, m)
    assert packet == b'\x02\x00\x01\x00\x02\x00\x07\n\x05hello'


def test_pack1():
    src = 0x0001
    dest = 0x0002
    timestamp = 1562486355.882235
    m = MessagePingRequest()
    m.message = str(timestamp)
    packet = pack(src, dest, m)
    assert packet == b'\x01\x00\x01\x00\x02\x00\x13\n\x111562486355.882235'


def test_pack2():
    src = 0x0001
    dest = 0x0002
    timestamp = 1562486355.882235
    m = MessagePingResponse()
    m.message = str(timestamp)
    packet = pack(src, dest, m)
    assert packet == b'\x02\x00\x01\x00\x02\x00\x13\n\x111562486355.882235'


def test_pack_fail1(message1):
    with pytest.raises(ValueError):
        pack(9999999, 0, message1)


def test_pack_fail2(message1):
    with pytest.raises(ValueError):
        pack(0, 9999999, message1)


def test_pack_fail31():
    m = MessagePingRequest()
    with pytest.raises(ValueError):
        pack(0, 0, m)


def test_pack_fail32():
    m = object()
    with pytest.raises(ValueError):
        # noinspection PyTypeChecker
        pack(0, 0, m)


def test_unpack_header():
    type_, src, dest, len_ = unpack_header(b'\x01\x00\x01\x00\x02\x00\x07')
    assert type_ == 1
    assert src == 1
    assert dest == 2
    assert len_ == 7


def test_unpack_header_fail():
    with pytest.raises(ValueError):
        unpack_header(b'12345')


def test_unpack1():
    r = unpack(1, b'\n\x05hello')
    assert isinstance(r, MessagePingRequest)
    assert r.message == 'hello'


def test_unpack2():
    r = unpack(2, b'\n\x05hello')
    assert isinstance(r, MessagePingResponse)
    assert r.message == 'hello'


def test_unpack_fail1():
    with pytest.raises(ValueError):
        unpack(254, b'\n\x05hello')


def test_unpack_fail21():
    with pytest.raises(ValueError):
        unpack(1, b'12345')


def test_unpack_fail22():
    # пришли левые данные в payload
    with pytest.raises(ValueError):
        unpack(1, b'\x08\xf7\x94\x83\xe9\x05\x10\xed\xf9M')


def test_pack_unpack():
    src = 0x0001
    dest = 0x0002
    message = 'hello'
    m = MessagePingRequest()
    m.message = message
    package = pack(src, dest, m)

    header = package[:LEN_HEADER]
    payload = package[LEN_HEADER:]

    type_, src2, dest2, len_ = unpack_header(header)
    assert type_ == 1
    assert src2 == src
    assert dest2 == dest
    assert len_ == len(payload)

    m2 = unpack(type_, payload)
    assert m2.message == message
