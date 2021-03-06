import grok

from raptus.mailcone.core import utils
from raptus.mailcone.rules import contents
from raptus.mailcone.rules.factories import BaseFactoryCondition

from raptus.mailcone.rules_writelog import interfaces
from raptus.mailcone.rules_writelog import _





class WriteLogItem(contents.BaseActionItem):
    grok.implements(interfaces.IWriteLogItem)

    path = ''
    message = ''

    @contents.process
    def process(self, charter):
        for mail in charter.mails:
            self.write(mail)

    def test(self, mail, factory):
        try:
            self.write(mail)
            mapping = dict(factory=factory.title, title=self.title, path=self.path, message=self.get_message(mail))
            msg = 'Rule <${factory}@${title}> successfully write a log at ${path} \nmessage: ${message}'
            return self.translate(_(msg, mapping=mapping))
        except Exception, e:
            return str(e)
    
    def write(self, mail):
        with open(self.path, 'a') as f:
            f.write(unicode(self.get_message(mail)).encode('utf8'))
            f.write('\r\n')
        f.close()







