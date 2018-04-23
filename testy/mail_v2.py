from envelopes import Envelope, GMailSMTP

addr=['tito02@o2.pl', 'jablonski.norbert@gmail.com']

email= u"  On the same note, I would like to leave you with some useful resources for your future reference "

for i in range(len(addr)):
    envelope = Envelope(
        from_addr=( u'PYTHON CODE'),
        to_addr=(addr[i], addr[i]),
        subject=u'Wiadomosc {} dla {}'.format(i,addr[i]),
        text_body=email
    )
    envelope.add_attachment('/home/tito/Pulpit/Coldwind_G._-_Zrozumiec_programowanie.pdf')

# Send the envelope using an ad-hoc connection...
    envelope.send('smtp.googlemail.com', login='truecapehorn@gmail.com',password='diverse02', tls=True)
    print('email nr. {} wysłany.'.format(i+1))
# Or send the envelope using a shared GMail connection...
#    gmail = GMailSMTP('truecapehorn@gmail.com', 'diverse02')
#    gmail.send(envelope)
