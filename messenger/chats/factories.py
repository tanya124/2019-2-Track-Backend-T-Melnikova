import factory
from chats.models import Chat, Message
from users.models import Member

class ChatsFactory(factory.Factory):
    class Meta:
        model = Chat

    topic = factory.Sequence(lambda n: 'Test_Chat_{0}'.format(n))


class MessageFactory(factory.Factory):
    class Meta:
        model = Message

    content = factory.Sequence(lambda n: 'Test_Message_{0}'.format(n))


class MemberFactory(factory.Factory):
    class Meta:
        model = Member