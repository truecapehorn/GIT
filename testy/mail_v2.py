from envelopes import Envelope, GMailSMTP
import glob

pliki=glob.glob("/home/tito/Pulpit/*.pdf")

for i in pliki:
    print(i)



addr=['tito02@o2.pl', 'jablonski.norbert@gmail.com']


for atachment in pliki:
    email= u" To jest wiadomosc z następujacym załącznikiem {} dla twojej wiadomosci ".format(str(atachment))
    for i in range(len(addr)):
        print('Wysłanie wiadomosci do {} z {}'.format(addr[i],atachment))
        envelope = Envelope(
            from_addr=( u'PYTHON CODE'),
            to_addr=(addr[i]),
            subject=u'Wiadomosc {} dla {}'.format(i,addr[i]),
            text_body=email
        )
        envelope.add_attachment(str(atachment))

    # Send the envelope using an ad-hoc connection...
        envelope.send('smtp.googlemail.com', login='truecapehorn@gmail.com',password='diverse02', tls=True)
        print('email nr. {} wysłany.'.format(i+1))
    # Or send the envelope using a shared GMail connection...
    #    gmail = GMailSMTP('truecapehorn@gmail.com', 'diverse02')
    #    gmail.send(envelope)
