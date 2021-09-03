import string 
import random
import time  

x = "y"
DecryptCode = 'DecryptCode'
EncryptedMessage = 'EncryptedMessage'


while x == 'y':
    First = 1

    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    num = string.digits
    symbols = string.punctuation

    ASample = random.sample(upper, First)
    First1 = "".join(ASample)

    BSample = random.sample(upper, First)
    First2 = "".join(BSample)

    CSample = random.sample(upper, First)
    First3 = "".join(CSample)

    DSample = random.sample(upper, First)
    First4 = "".join(DSample)

    ESample = random.sample(upper, First)
    First5 = "".join(ESample)

    FSample = random.sample(upper, First)
    First6 = "".join(FSample)

    GSample = random.sample(upper, First) 
    First7 = "".join(GSample)

    HSample = random.sample(upper, First)
    First8 = "".join(HSample)

    ISample = random.sample(num, First)
    First9 = "".join(ISample)

    JSample = random.sample(num, First)
    First10 = "".join(JSample)

    KSample = random.sample(num, First)
    First11 = "".join(KSample)

    LSample = random.sample(num, First)
    First12 = "".join(LSample)

    MSample = random.sample(num, First)
    First13 = "".join(MSample)

    NSample = random.sample(num, First)
    First14 = "".join(NSample)

    OSample = random.sample(num, First)
    First15 = "".join(OSample)

    PSample = random.sample(num, First)
    First16 = "".join(PSample)

    QSample = random.sample(symbols, First)
    First17 = "".join(QSample)

    RSample = random.sample(num, First)
    First18 = "".join(RSample)

    SSample = random.sample(num, First)
    First19 = "".join(SSample)

    TSample = random.sample(num, First)
    First20 = "".join(TSample)

    USample = random.sample(num, First)
    First21 = "".join(USample)

    VSample = random.sample(num, First)
    First22 = "".join(VSample)

    WSample = random.sample(num, First)
    First23 = "".join(WSample)

    XSample = random.sample(num, First)
    First24 = "".join(XSample)

    YSample = random.sample(num, First)
    First25 = "".join(YSample)

    ZSample = random.sample(num, First)
    First26 = "".join(ZSample)

    a = First1
    b = First2
    c = First3
    d = First4
    e = First5
    f = First6
    g = First7
    h = First8
    i = First9
    j = First10
    k = First11
    l = First12
    m = First13
    n = First14
    o = First15
    p = First16
    q = First17
    r = First18
    s = First19
    t = First20
    u = First21
    v = First22
    w = First23
    x = First24
    y = First25
    z = First26

    time.sleep(3)
    all = a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z,
    print(all)

    file = open(DecryptCode+".txt", "w")
    file.write('------------')
    file.write('\na = \'' + First1 + '\'')
    file.write('\nb = \'' + First2 + '\'')
    file.write('\nc = \'' + First3 + '\'')
    file.write('\nd = \'' + First4 + '\'')
    file.write('\ne = \'' + First5 + '\'')
    file.write('\nf = \'' + First6 + '\'')
    file.write('\ng = \'' + First7 + '\'')
    file.write('\nh = \'' + First8 + '\'')
    file.write('\ni = \'' + First9 + '\'')
    file.write('\nj = \'' + First10 + '\'')
    file.write('\nk = \'' + First11 + '\'')
    file.write('\nl = \'' + First12 + '\'')
    file.write('\nm = \'' + First13 + '\'')
    file.write('\nn = \'' + First14 + '\'')
    file.write('\no = \'' + First15 + '\'')
    file.write('\np = \'' + First16 + '\'')
    file.write('\nq = \'' + First17 + '\'')
    file.write('\nr = \'' + First18 + '\'')
    file.write('\ns = \'' + First19 + '\'')
    file.write('\nt = \'' + First20 + '\'')
    file.write('\nu = \'' + First21 + '\'')
    file.write('\nv = \'' + First22 + '\'')
    file.write('\nw = \'' + First23 + '\'')
    file.write('\nx = \'' + First24 + '\'')
    file.write('\ny = \'' + First25 + '\'')
    file.write('\nz = \'' + First26 + '\'')
    file.close

    time.sleep(5)
    print('Each letters is before a Uppercase letter or a number/symbol EG : aD bZ cM dH eK fM gO hV i8 j2 k5 l7 m0 n3 o8 p1 . . . . . . .')

    GetMessageToEncode = input('Type the message you want to encode, Do not put \' + - * , ! ? % ¨ $ ^ ù < > :')

    EncodedText0 = GetMessageToEncode.replace('a', First1 ).replace('b', First2).replace('c', First3).replace('d', First4).replace('e', First5).replace('f', First6).replace('g', First7).replace('h', First8).replace('i', First9).replace('j', First10).replace('k', First11).replace('l', First12).replace('m', First13).replace('n', First14).replace('o', First15).replace('p', First16).replace('q', First17).replace('r', First18).replace('s', First19).replace('t', First20).replace('u', First21).replace('v', First22).replace('w', First23).replace('x', First24).replace('y', First25).replace('z', First26)          
    print(EncodedText0)

    StoreMessage = input('Do you want to Store the message ? y/n :')
    if StoreMessage == ('no'):
        file = open(DecryptCode+".txt", "a")
        file.write('\n------------')
    elif StoreMessage == ('n'):
        file = open(DecryptCode+".txt", "a")
        file.write('\n------------')
    if StoreMessage == ('yes'):
        file = open(DecryptCode+'.txt', 'a')
        file.write('\n' + EncodedText0)
        file.write('\n------------')
    elif StoreMessage == ('y'):
        file = open(DecryptCode+'.txt', 'a')
        file.write('\n' + EncodedText0)
        file.write('\n------------')
    elif StoreMessage == ('ye'):
        file = open(DecryptCode+'.txt', 'a')
        file.write('\n' + EncodedText0)
        file.write('\n------------')
    time.sleep(3)
    x = input('Do you wanna encode another message ? y/n :')
else:
    quit() 
           
