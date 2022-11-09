from mail_sender import Request, MailSender
from discount_applier import Request
class User:
    def __init__(self, name, email):
        self.email = email
        self.name = name

class HttpClient:
    def __init__(self, base_url):
        self.request = {}
    
    def post(self, base_url, request: Request):
        self.requests[str(base_url)] = request


def test_send_v1():
    # TODO: write a test that fails due to the bug in MailSender.send_v1
    user = User('pierre@example.com', 'Pierre')
    http_client= HttpClient()
    # mailSender = MailSender(http_client)
    # sendResponse = mailSender.send_v1(user, 'un message')
    # assert 


def test_send_v2():
    # TODO: write a test that fails due to the bug in MailSender.send_v2
    pass
