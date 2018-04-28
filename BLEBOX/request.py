import requests


def response_status(action, r):
    '''Wydrukowanie wynikow'''
    # Response, status etc
    print('\n' + 140 * '-' + '\n')
    print('* {0} dla URL: {1}\n  Kodowanie znaków: {2}\n'.format(action, r.url, r.encoding))
    print('* ODPOWIEDZ SERWERA:\n{0}'.format(r.text))  # TEXT/HTML
    # HTTP
    print(
        '* KOD STATUSU I STATUS:\n[{0} --> {1}]\n'.format(r.status_code, r.reason))
    print('* NAGLOWEK ODPOWIEDZI:\n{0}\n'.format(r.headers))
    print('<!---------koniec-----------!>')


def req1():
    action = 'Test 1'
    payload = {'key1': 'value1', 'key2': 'value2'}
    r = requests.get("http://httpbin.org/get", params=payload)
    response_status(action, r)


def req2():
    action = 'Test 2'
    r = requests.get('https://github.com/timeline.json')
    response_status(action, r)


def req3():
    action = 'Test 3'
    payload = {'key1': 'value1', 'key2': 'value2'}
    r = requests.post("http://httpbin.org/post", data=payload)
    response_status(action, r)


def req4(url):
    action = 'Test 4'
    r = requests.get(url)
    response_status(action, r)


def req5(url):
    action = 'Test 5'
    r = requests.post(url)
    response_status(action, r)


req4('http://www.elam.pl/instalatorstwo/index.html')
req1()
req2()
req3()
req5('http://www.filmweb.pl/')
