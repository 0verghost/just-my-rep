alf = {'А':0, 'Б':1, 'В':2, 'Г':3, 'Д':4, 'Е':5, 'Ё':6, 'Ж':7, 'З':8, 'И':9, 'Й':10, 'К':11, 'Л':12, 'М':13, 'Н':14, 'О':15
       , 'П':16, 'Р':17, 'С':18, 'Т':19, 'У':20, 'Ф':21, 'Х':22, 'Ц':23, 'Ч':24, 'Ш':25, 'Щ':26, 'Ъ':27, 'Ы':28, 'Ь':29, 'Э':30, 'Ю':31
       , 'Я':32}
alf_ret = {0:'А', 1:'Б', 2:'В', 3:'Г', 4:'Д', 5:'Е', 6:'Ё', 7:'Ж', 8:'З', 9:'И', 10:'Й', 11:'К', 12:'Л', 13:'М', 14:'Н', 15:'О',
           16:'П', 17:'Р', 18:'С', 19:'Т', 20:'У', 21:'Ф', 22:'Х', 23:'Ц', 24:'Ч', 25:'Ш', 26:'Щ', 27:'Ъ', 28:'Ы',
           29:'Ь', 30:'Э', 31:'Ю', 32:'Я'}
proverka = input('Доброго времени суток, дорогой пользователь!\n'
                 'Добро пожаловать в шифровальную машину,\n'
                 'работающую на алгоритме Alan v.1.0\n'
                 'Она может зашифровать любую фразу или слово, написанную на русском языке заглавными буквами.\n'
                 'А так же может расшифровать любую фразу или слово, защифрованное алгоритмом Alan v.1.0\n'
                 'Достаточно написать "зашифровать" или "расшифровать"\n'
                 'Приятного пользования!!!\n'
                 '                                                                              OVE Computer Programs©\n'
                 'Что хотите сделать?:')
if proverka == "ЗАШИФРОВАТЬ" or proverka=='зашифровать' or proverka == 'Зашифровать':
    vxod = input('Введите строчку для шифровки:').split()
    dyrti = []
    for word in vxod:
        shifword = ''
        for lit in word:
            numlit = alf.get(lit)
            numshiflit = numlit + len(word)
            if numshiflit > 32:
                numshiflit = numshiflit - 33
            shifword += alf_ret.get(numshiflit)
        dyrti += [shifword]
    secretfraze = ' '.join(dyrti)
    print(secretfraze)
if proverka == 'расшифровать' or proverka == 'Расшифровать ' or proverka == 'РАСШИФРОВАТЬ':
    secretfraze = input('Введите строчку для расшифровки:').split()
    rasshif = []
    for rasword in secretfraze:
        rasras = ''
        for raslit in rasword:
            numraslit = alf.get(raslit)
            numrasraslit = numraslit - len(rasword)
            if numrasraslit < 0:
                numrasraslit = numrasraslit + 33
            rasras += alf_ret.get(numrasraslit)
        rasshif += [rasras]
    rasshiffraze = ' '.join(rasshif)
    print(rasshiffraze)