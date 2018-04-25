from envelopes import Envelope, GMailSMTP
import glob

pliki=glob.iglob("c:/tmp/**/*.pdf", recursive=True)



addr=['tito02@o2.pl', 'jablonski.norbert@gmail.com']



for atachment in pliki:
    email= u" To jest wiadomosc z następujacym załącznikiem {}".format(str(atachment))
    for i in range(len(addr)):
        print('Wysłanie wiadomosci do {} z {}'.format(addr[i],atachment))
        envelope = Envelope(
            from_addr=( u'PYTHON CODE v2 google '),
            to_addr=(addr[i]),
            subject=u'Wiadomosc {} dla {}'.format(i+1,addr[i]),
            text_body=email
        )
        #envelope.add_attachment(str(atachment))

    # Send the envelope using an ad-hoc connection...
        envelope.send('smtp.googlemail.com', login='truecapehorn@gmail.com',password='diverse02', tls=True)
        print('email do adresata. {} wysłany.'.format(addr[i]))
    # Or send the envelope using a shared GMail connection...
    #    gmail = GMailSMTP('truecapehorn@gmail.com', 'diverse02')
    #    gmail.send(envelope)
