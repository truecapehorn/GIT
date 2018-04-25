from envelopes import Envelope, GMailSMTP
import glob
import os, shutil,time
import random

newfolder=random.randint(0, 255)
src='c:/tmp'
dst='c:/tmp2/'+str(newfolder)

glob.iglob(src+"/**/*.pdf", recursive=True)
print('Zostaną wysłane meile z nastepujacymi załącznikami')
for lp, value in enumerate(glob.iglob("c:/tmp/**/*.pdf", recursive=True)):
    print(lp+1, value)

addr = ['jablonski.norbert@gmail.com']
for number, atachment in enumerate(glob.iglob("c:/tmp/**/*.pdf", recursive=True)):
    email = u"To jest wiadomosc z następujacym załącznikiem {}".format(str(atachment))
    for i in range(len(addr)):
        print('\nWysłanie wiadomosci do {} z {}'.format(addr[i], atachment))
        envelope = Envelope(
            from_addr=(u'ELAM'),
            to_addr=(addr[i]),
            subject=u'Wiadomosc {} dla {}'.format(i + 1, addr[i]),
            text_body=email
        )
        #envelope.add_attachment(str(atachment))
        # Send the envelope using an ad-hoc connection...
        envelope.send('smtp.googlemail.com', login='truecapehorn@gmail.com', password='diverse02', tls=True)
        print('email nr {} do adresata. {} WYSŁANY!!.'.format(number+1,addr[i]))


shutil.copytree(src,dst)
shutil.rmtree(src+'/')



