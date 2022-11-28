import io
import requests
import sys
import pikepdf
from pikepdf import Pdf
from PyPDF2 import PdfFileReader
import subprocess

val = 0
e_array = ["https://www.lttc.ntu.edu.tw/academics/e_wordlist/A.pdf", "https://www.lttc.ntu.edu.tw/academics/e_wordlist/B.pdf", "https://www.lttc.ntu.edu.tw/academics/e_wordlist/C.pdf", "https://www.lttc.ntu.edu.tw/academics/e_wordlist/D.pdf", "https://www.lttc.ntu.edu.tw/academics/e_wordlist/E.pdf", "https://www.lttc.ntu.edu.tw/academics/e_wordlist/F.pdf", "https://www.lttc.ntu.edu.tw/academics/e_wordlist/G.pdf", "https://www.lttc.ntu.edu.tw/academics/e_wordlist/H.pdf", "https://www.lttc.ntu.edu.tw/academics/e_wordlist/I.pdf", "https://www.lttc.ntu.edu.tw/academics/e_wordlist/J.pdf", "https://www.lttc.ntu.edu.tw/academics/e_wordlist/K.pdf", "https://www.lttc.ntu.edu.tw/academics/e_wordlist/L.pdf", "https://www.lttc.ntu.edu.tw/academics/e_wordlist/M.pdf", "https://www.lttc.ntu.edu.tw/academics/e_wordlist/N.pdf", "https://www.lttc.ntu.edu.tw/academics/e_wordlist/O.pdf", "https://www.lttc.ntu.edu.tw/academics/e_wordlist/P.pdf", "https://www.lttc.ntu.edu.tw/academics/e_wordlist/Q.pdf", "https://www.lttc.ntu.edu.tw/academics/e_wordlist/R.pdf", "https://www.lttc.ntu.edu.tw/academics/e_wordlist/S.pdf", "https://www.lttc.ntu.edu.tw/academics/e_wordlist/T.pdf", "https://www.lttc.ntu.edu.tw/academics/e_wordlist/U.pdf", "https://www.lttc.ntu.edu.tw/academics/e_wordlist/V.pdf", "https://www.lttc.ntu.edu.tw/academics/e_wordlist/W.pdf", "https://www.lttc.ntu.edu.tw/academics/e_wordlist/Y.pdf", "https://www.lttc.ntu.edu.tw/academics/e_wordlist/Z.pdf"]
i_array = ["https://www.lttc.ntu.edu.tw/academics/i_wordlist/simple/A.pdf", "https://www.lttc.ntu.edu.tw/academics/i_wordlist/simple/B.pdf", "https://www.lttc.ntu.edu.tw/academics/i_wordlist/simple/C.pdf", "https://www.lttc.ntu.edu.tw/academics/i_wordlist/simple/D.pdf", "https://www.lttc.ntu.edu.tw/academics/i_wordlist/simple/E.pdf", "https://www.lttc.ntu.edu.tw/academics/i_wordlist/simple/F.pdf", "https://www.lttc.ntu.edu.tw/academics/i_wordlist/simple/G.pdf", "https://www.lttc.ntu.edu.tw/academics/i_wordlist/simple/H.pdf", "https://www.lttc.ntu.edu.tw/academics/i_wordlist/simple/I.pdf", "https://www.lttc.ntu.edu.tw/academics/i_wordlist/simple/J.pdf", "https://www.lttc.ntu.edu.tw/academics/i_wordlist/simple/K.pdf", "https://www.lttc.ntu.edu.tw/academics/i_wordlist/simple/L.pdf", "https://www.lttc.ntu.edu.tw/academics/i_wordlist/simple/M.pdf", "https://www.lttc.ntu.edu.tw/academics/i_wordlist/simple/N.pdf", "https://www.lttc.ntu.edu.tw/academics/i_wordlist/simple/O.pdf", "https://www.lttc.ntu.edu.tw/academics/i_wordlist/simple/P.pdf", "https://www.lttc.ntu.edu.tw/academics/i_wordlist/simple/Q.pdf", "https://www.lttc.ntu.edu.tw/academics/i_wordlist/simple/R.pdf", "https://www.lttc.ntu.edu.tw/academics/i_wordlist/simple/S.pdf", "https://www.lttc.ntu.edu.tw/academics/i_wordlist/simple/T.pdf", "https://www.lttc.ntu.edu.tw/academics/i_wordlist/simple/U.pdf", "https://www.lttc.ntu.edu.tw/academics/i_wordlist/simple/V.pdf", "https://www.lttc.ntu.edu.tw/academics/i_wordlist/simple/W.pdf", "https://www.lttc.ntu.edu.tw/academics/i_wordlist/simple/X.pdf", "https://www.lttc.ntu.edu.tw/academics/i_wordlist/simple/Y.pdf", "https://www.lttc.ntu.edu.tw/academics/i_wordlist/simple/Z.pdf"]
hi_array = ["https://www.lttc.ntu.edu.tw/academics/hi_wordlist/simple/A.pdf", "https://www.lttc.ntu.edu.tw/academics/hi_wordlist/simple/B.pdf", "https://www.lttc.ntu.edu.tw/academics/hi_wordlist/simple/C.pdf", "https://www.lttc.ntu.edu.tw/academics/hi_wordlist/simple/D.pdf", "https://www.lttc.ntu.edu.tw/academics/hi_wordlist/simple/E.pdf", "https://www.lttc.ntu.edu.tw/academics/hi_wordlist/simple/F.pdf", "https://www.lttc.ntu.edu.tw/academics/hi_wordlist/simple/G.pdf", "https://www.lttc.ntu.edu.tw/academics/hi_wordlist/simple/H.pdf", "https://www.lttc.ntu.edu.tw/academics/hi_wordlist/simple/I.pdf", "https://www.lttc.ntu.edu.tw/academics/hi_wordlist/simple/J.pdf", "https://www.lttc.ntu.edu.tw/academics/hi_wordlist/simple/K.pdf", "https://www.lttc.ntu.edu.tw/academics/hi_wordlist/simple/L.pdf", "https://www.lttc.ntu.edu.tw/academics/hi_wordlist/simple/M.pdf", "https://www.lttc.ntu.edu.tw/academics/hi_wordlist/simple/N.pdf", "https://www.lttc.ntu.edu.tw/academics/hi_wordlist/simple/O.pdf", "https://www.lttc.ntu.edu.tw/academics/hi_wordlist/simple/P.pdf", "https://www.lttc.ntu.edu.tw/academics/hi_wordlist/simple/Q.pdf", "https://www.lttc.ntu.edu.tw/academics/hi_wordlist/simple/R.pdf", "https://www.lttc.ntu.edu.tw/academics/hi_wordlist/simple/S.pdf", "https://www.lttc.ntu.edu.tw/academics/hi_wordlist/simple/T.pdf", "https://www.lttc.ntu.edu.tw/academics/hi_wordlist/simple/U.pdf", "https://www.lttc.ntu.edu.tw/academics/hi_wordlist/simple/V.pdf", "https://www.lttc.ntu.edu.tw/academics/hi_wordlist/simple/W.pdf", "https://www.lttc.ntu.edu.tw/academics/hi_wordlist/simple/X.pdf", "https://www.lttc.ntu.edu.tw/academics/hi_wordlist/simple/Y.pdf", "https://www.lttc.ntu.edu.tw/academics/hi_wordlist/simple/Z.pdf"]
# alpha_upper = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

e_unique_list = ['（British', 'English）', '(British', 'English)', '字彙', '詞類', '英式拼法', '註解']
i_unique_list = ['字彙', '詞類', '註解', 'ADn', 'AY', 'pAdxF', 'Q~', 'adj', ';', ']', ';p', '[', ';CH', 'q,q|', 'rPV', ']I', 'Gy', 'zAG', '~k', '[jy', 'Wl']
hi_unique_list = ['字彙', '詞類', '註解', '賠償', '晃動；束髮', '半身像', '突擊', '免職', '貨物或乘客名單', '鑄造', '薄荷', '浸泡', '靜止；蒸餾器；電影之靜態畫面', '吞嚥', '明白', '增加；起身離開', '渴望']

alpha_upper = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
alpha_lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

categories = ['art.', 'adv.', 'noun', 'adj.', 'prep./adv.', 'prep./adv./adj.', 'verb', 'noun/verb', 'prep./conj.', 'prep.', 'verb/noun',
'adv./adj.', 'adj./pron./adv.', 'conj.', 'adj./noun', 'pron./adj.', 'pron./adv./adj.', 'pron.', 'conj./prep./adv.', 'noun/adj.',
'adv./noun/verb/adj.', 'prep./conj./adv.', 'adv./prep.', 'adv./adj./pron.', 'conj./prep.', 'adj./verb', 'aux.',
'adj./adv.', 'verb/adj.',  'adj./int./noun', 'noun/verb/adj.', 'adj./verb/noun', 'adv./prep./noun/adj.', 'adv./adj./noun', 'pron./adj./adv.',
'noun/adv./adj.', 'number/pron./noun/adj.', 'pron./adj./conj.', 'verb/noun/adj.', 'adj./adv./pron.', 'adj./prep./pron./noun', 'noun/adj./verb',
'pron./adj./noun/adv.', 'noun/interj.', 'determiner', 'interj.', 'adv./conj.', 'number/noun/pron.', 'prep./adv./noun',
'adj./pron./noun', 'adv./adj./pron./noun', 'adj./noun/adv.', 'adv./pron.', 'noun/pron./adv.', 'adj./noun.', 'adj./pron.',
'number/pron./noun', 'pron./conj./adj./noun', 'adj./adv./noun', 'adv./pron./adj.', 'prep./adj./adv./verb',
'verb/noun/aux.', 'adv./pron./adj./conj.', 'pron./noun', 'pron./adv.', 'noun/adj./adv.', 'adv./noun/pron.', 'adv./prep./adj.',
'adj./adv./noun/verb', 'adv./conj./pron.', 'adv./adj./conj.', 'adv./adj./prep.', 'prep./adv./adj./noun', 'pron./verb/adj.', 'prep./conj./adj./noun',
'adj./verb/adv.', 'pron./determiner', 'conj./pron./adj./adv.', 'conj./adv.', 'prep./inf.', 'adv./noun', 'adj./noun/verb', 'verb/adj./noun',
'conj./adv./pron.', 'pron./conj./adj.', 'pron./conj.', 'determiner/conj.', 'prep./noun', 'interj./adv.', 'number/noun/adj.']

with_equals = ['=a.m.=AM', '=plane',
'=flat (British',
'=apoligise', '=anyone', '=anybody', '=anyplace', '=Apr.', '=Aug.', '=auntie=aunty', '=fall',
'adv.=backwards', '=Bar-B-Q',
'=beside(prep.)',
'=bike', '=pail',
'=sweet (British',
'=centre (British',
'=centimetre', '=compact disk',
'=Xmas',
'=colour (British',
'=colourful', '=roach', '=cooky', '=daddy=papa=pa=pop', '=Dec.',
'=Dr (British',
'=doc.=physician', '=buck',
'=donut', '=emphasise', '=everybody', '=examination', '=favour', '=favourite', '=autumn', '=Feb.', '=flash', '=apartment', 'adv.=forwards',
'=Fri.', '=gas=petrol', '=gramme', '= goodbye, bye', '=g=gm', '=grandpa', '=grandma', '=grey', '=burger', '=hippo', '=humour',
'=Jan.','=Jul.', '=Jun.', '=kilometre', '=catsup', '=kg', '=km', '=kitty',
'=litre (British',
'=Mar.', '=postman',
'English)=mail',
'=marvellous', '=metre',
'English)=m',
'=mathematics', '=Mon.', '= mommy=mom=momma=mamma', '=motorbike', '=film=cinema=picture',
'=Mr', '=Mrs', '=mass rapid', 'transit=subway=underground=metro', '=Ms', '=neighbour', '=nope', '=Nov.', '=organisation',
'=Oct.', '=O.K.=ok=o.k.', '=organise', '=pyjamas', '=trousers', '=p.m.=PM', '=physical education', '=telephone', '=photograph',
'=photo', '=cop', '=mail', '=practise(verb,', '=programme', '=fridge=icebox',
'=railway (British',
'=realise (British',
'=ROC', '=rest room',
'=Sat.', '=Sept.', '=pavement', '=store', '=skilful', '=someone', '=somebody', '=tummy',
'=underground=tube (British',
'English)=MRT=metro',
'=Sun.', '=dinner', 'noun=candy', '=taxicab=cab', '=phone', '=TV', '=theatre', '=Thanksgiving Day', '=Thurs./Thur.', '=until',
'=bean curd', '=towards',
'=pants (American English)',
'=tee-shirt', '=Tues./Tue.', '=stomach', '=television', '=till',
'=United States (of America)',
'=video cassette recorder', '=Wed., Weds.', '=yes', '=yeah']

with_parens_only = ['English)', '(British', 'datum (singular form)', 'mediums/media (plural form)', '(British English)', '(American', 'British English)', '(P)']

words = ['advertisement  noun', 'congratulation  noun', 'environment  noun', 'granddaughter  noun', 'hippopotamus  noun', 'machine  noun',
'magazine  noun', 'magician  noun', 'mailman  noun', 'maintain  verb', 'manager  noun', 'Mandarin  noun', 'marriage  noun',
'maximum  adj./noun/adv.', 'meaning  noun', 'mechanic  noun', 'medicine  noun', 'message  noun', 'microwave noun/verb',
'midnight  noun/adj.', 'morning  noun', 'mosquito  noun', 'motorcycle noun', 'mountain  noun', 'movement  noun', 'museum  noun',
'musician  noun', 'organization  noun', 'photographer  noun', 'Republic of China  noun', 'stomachache  noun', 'supermarket  noun',
"Teacher's Day  noun", 'Thanksgiving  noun', "Valentine's Day  noun"]

grandee = categories + with_equals + with_parens_only + alpha_upper + alpha_lower + e_unique_list + ['^k', 'rJ', '爭吵(P)', '詞類', '註解', '字彙', '@};(f)o@', 'yl', '英式拼法', "fP"]

categories_i = ['verb/noun', 'adj.', 'prep./adv.', 'noun', 'adj./noun', 'adv.', 'verb', 'noun/verb', 'noun/adj.', 'adjective', 'verb/adj./noun', 'prep.', 'adv./adj.', 'auxiliary', 'noun/adj', 'adj./noun/verb', 'adj./verb', 'adj./verb/noun', 'noun/adj./verb', 'conjunction', 'verb/verb(aux.)', 'adj./adv.', 'adj./adv', 'verb/adj.', 'noun/adv./adj.', 'interj.', 'pron.', 'adj./noun/adv.', 'aux.', 'adj./adv./noun', 'noun/verb/adj.', 'pron./adv', 'verb/noun/adj.', 'adj./adv./verb', 'conj.', 'adv./conj.', 'det./pron.', 'pron./conj.', 'interj./verb']

with_equals_i = ['= adj.', '= advertize', '= advisor', '= pocket money', '= analyse (British English)', '= auto', '= aux.', '= axe (British English)', '= Before Christ', '= baby-sit', '= baby-sitter', '= behaviour (British English)', '= bookshop (British English)', '= brassiere', '= groom', '= café', '= catalogue (British English)', '= cheque (British English)', '= cooperate', '= defence (British English)', '= dependant', '= dialogue (British English)', '= discotheque', '= disc', '= dorm', '= enrol (British English)', '= et cetera', '= exam', 'noun= facsimile', '= flavour (British English)', '= brow (British English)', '= motorway (British English)', '= refrigerator', '= fulfil (British English)', '= honour (British English)', '= enquire', '= enquiry', '= judgement', '= labour (British English)', '= lab', '= ladybird (British English)', '= toilet', '= licence (British English)', '= spirits (British English)', 'noun=  U', '= truck (American English)', '= litchi  K', '= Metro', '= mike', '= mustache', '= offence (British English)', '= father', '= per cent', '= gas, gasoline (American English)', '= table tennis', '= cock (British English)', '= rumor (American English)', '= gull', '= story (American English)  h', '= tyre (British English)  L', '= traveller (British English)', '= travelling (British English)', '= underground railway', '= vapour (British English)', '= vigour (British English)', '=whomever', '= sweet potato (American English)', '= yoghurt']

with_parens_only_i = ['bacterium (singular form)', '(P)', 'verb/verb(aux.)', '@};(f)o@', 'phenomena (plural form)', 'e   (P)', 'U   (P)', '(used mainly in British English)', 'be supposed to (P)'] +['soya bean/soy',]



grandei = categories_i + with_equals_i + with_parens_only_i + i_unique_list + ['^k', 'rJ', '爭吵(P)', '詞類', '註解', '字彙', '@};(f)o@', 'yl', '英式拼法', "fP", '跳躍，反彈', '渴望，日本貨幣單位￥', '包圍，裝邊', '抽象的，摘要', 'v ,Aq ;', 'd ,p}n', ']l^', 'Dn ;', '} ,', 'Z ,', 'eA usually in plural form', "usually in plural form"] + alpha_upper + alpha_lower

categories_hi = ['adj.', 'adj', 'noun', 'verb', 'adj./noun', 'noun/adj.', 'verb/noun', 'adv.', 'noun/adj./verb', 'adverb', 'noun/verb',
'adj./noun/verb', 'verb/adj.', 'adj./verb', 'conj./adj.', 'adv./adj.', 'adj./adv.', 'prep./conj./adv.', 'verb/adj./noun', 'noun/adj./adv.',
'adj./adv./noun', 'verb/noun/adj.', 'adj./verb/noun', 'adj./prep.', 'noun/verb/adj.', 'adv./noun', 'conj.', 'noun/prep.', 'adj./verb/noun/adv.',
'prep./adv.', 'preposition', 'prep.', 'pronoun', 'adj/noun', 'noun/adv./verb', 'adj./adv./verb', 'verb/noun/adv.',  'noun/pron./adj./adv.',
'prep./adv./adj./noun', 'noun/adv./adj./verb']

with_equals_hi = ['= advertisement', '= ad, advertisement', 'noun = antenna (American English)', '= esthetic', '= esthetics', '= ageing',
'= artificial intelligence', '= air conditioner', '= analytic', '= antarctic,  南極', '= appal (British English)', '= archeology', '= arctic,  北極',
'= armour (British English)', '= armoured (British English)', '= automatic teller machine', '= authorise (British English)',
'= British Standard; Bachelor of Science', '女性為 blonde，男性為  blond', '= botanic', '= bra', '= grill', '= buildup, build up',
'= cease-fire', '= cellphone/cellular phone/mobile', '= Centigrade/centigrade', '= centred (British English)', '= chair/chairman/chairwoman',
'= characterise (British English)', '= chili', '= cleanup', '= Coke', '= comedown', '= coordinate', '= corporation', '= councillor (British English)',
'= counselling (British English)', '= counsellor (British English)', '= cosy (British English)', '= pedestrian crossing, zebra crossing,', '= dawn',
'= despatch (British English)', 'noun= draft', '= drive (road)', '= digital video disk/digital versatile disk', '= endeavour (British English)',
'= emotional quotient/emotional', '= lash', '未婚夫為 fianc?，未婚妻為 fianc?e', '= fibre (British English)', '= fireman', '= first class', '= geographic',
'= glamour (British English)', '= genetically modified organism', '= guerilla', '= gym', '= hard-line', '= high fidelity', '= homogenous',
'= instalment (British English)', '= inwards (British English)', '= intelligence quotient', '= jeopardise (British English)', '= liquid crystal display',
'= limo', '= lineup (American English)', 'noun = loco', '= manoeuvre (British English)', '= millimetre (British English), mm',
'= mobilise (British English)', '= mould (British English)', '= short-sighted (American English)', '= neighbouring (British English)',
'= odour (British English)', '= onetime', '= optimal', '= organised (British English)', '= orientate', '= East', '= eastern',
'= paralyse (British English)', '= parlour', '= personal digital assistant', '= plough (British English)', '= china  瓷器', '= postwar',
'provided that= providing that', 'adj.= psychical', 'noun= earthquake', '= quartette', '= realisation (British English)', '= reorganise (British English)',
'= rhino', '= right wing', '= rigour', '蟑螂= cockroach', '= rotatory', '= sculpt', '= sceptical (British English), skeptic,',
'包圍，裝邊', '= sledge (British English)', '= socialise', '= specialise (British English)', '= especially', '= speciality (British English)',
'= splendour (British English)', '跳躍，反彈', '= stewardess/attendant', '= sulphur (British English)', '= symbolical', '= carryout, takeout',
'= 1,000 kilograms', '= transitory', '= tram, tramcar, streetcar', '= TB', '= tumour (British English)', '= two thirds', '= up to date', '= vs.',
'= vet', '= whisky', '女性為 widow，男性為 widower', '= xerox', '渴望，日本貨幣單位￥', '= ZIP/zone improvement plan/zip code']

grandehi = categories_hi + with_equals_hi + hi_unique_list + ['^k', 'rJ', '爭吵(P)', '詞類', '註解', '字彙', '@};(f)o@', 'yl', '英式拼法', "fP", '跳躍，反彈', '渴望，日本貨幣單位￥', '包圍，裝邊', '抽象的，摘要', 'v ,Aq ;', 'd ,p}n', ']l^', 'Dn ;', '} ,', 'Z ,', 'eA usually in plural form', "usually in plural form", 'adj.  傲慢的', '農產品  (P)', '(P)', '爭吵(P)', 'servicewoman (女性)', 'phone/mobile/cell', '女性為  congresswoman','noun/pron./adj./adv. = two thirds'] + alpha_upper + alpha_lower
empty_for_now = []

for url in e_array:

    r = requests.get(url)
    f = io.BytesIO(r.content)

    with pikepdf.open(f) as pdf:
        num_pages = len(pdf.pages)
        # del pdf.pages[-1]
        pdf.save("decrypted.pdf")


    def text_extractor(path):
        with open(path, 'rb') as f:
            pdf = PdfFileReader(f)
            numPages = pdf.getNumPages()
            for n in range(numPages):
                page = pdf.getPage(n)
                # print('Page type: {}'.format(str(type(page))))
                text = page.extractText().strip()
                # print(pdf)

    text_extractor('decrypted.pdf')

    # word_process = subprocess.run("cat /usr/share/dict/words > words.txt", shell=True, universal_newlines=True)

    file = "decrypted.pdf"
    process = subprocess.run("pdf2txt.py {}".format(file) + " >> filename.txt", shell=True, universal_newlines=True)
    # output = process.stdout

    # def get_dict(text_file):
    #         with open(text_file, "r") as words:
    #             dictionary = words.readlines()
    #         dictionary = [words.strip() for words in dictionary]
    #         return dictionary

    # dict_words = get_dict("words.txt")

    def clean_word_list(text_file):
        global val
        arr = []
        new_words = []
        import re
        with open(text_file, "r") as pdf:
            word_list = pdf.readlines()
        word_list = [words.strip() for words in word_list]
        while("" in word_list): 
            word_list.remove("")
        print(word_list)
        # for words in word_list:
        #     if "=" in words:
                # print(words)
                # words = words.split()
                # new_words = ",".join(words)
                # if words.find("(British") > -1:
                #     words = words + " English)"
                # elif words.find("English)") > -1:
                #     words = "(British " + words
                # elif words.find("(verb,") > -1:
                #     words = words + " British English)"
                # if re.search(r"\bK$|\bh$|\bL$", words) != None:
                #     words = words[:-1].strip()
                # elif re.search(r"\bU$", words) != None:
                #     words = words[:-1].strip() + " Missing Translation (Courtesy of the LTTC)"
                # print(words)
                # words = words.split(" ")
        #         new_words.append(words)
        # for words in word_list:
        #     if "，" in words:
                # print(words)
                # words = words.split("，")
                # new_words = ",".join(words)
                # words = words.split(" ")
                # new_words.append(words)
        # for nws in new_words:
        #     nws = nws.strip()
        #     # nws = nws.split("(")
        #     # print(nws[0])
        #     new_new_words.append(nws)
        # global val
        # for rs in word_list:
        #     # if re.search(r"^[a-z.]+\/|\/[a-z.]+$|^noun$|noun$|^verb$|verb$|^adj\.|^adjective$|adjective$|^conj\.|^conjunction$|conjunction$|^adv\.|^adverb$|adverb$|^interj\.|^interjection$|interjection$|^art\.|^prep\.|^preposition$|preposition$|^aux\.|^auxiliary$|auxiliary$|^pron\.|^pronoun$|pronoun$|^det\.|^determiner|determiner$|^number\/|^num\.", rs) != None:
        #     if rs not in grandehi:
        #     # # if re.search(r"=|，", rs):
        #     #     # val += 1
        #     #     if rs not in empty_for_now:
        #         empty_for_now.append(rs)
        # # print(empty_for_now)
        # for words in word_list:
        #     if re.search(r"\^|^[A-Z]|^[A-Z]{1}$|^[ysowh]{1}$|^[a-z.]+\/|=|，| |^爭吵\(P\)$|^詞類$|^註解$|^字彙$|^@};\(f\)o@$|^yl$|^英式拼法$|^fP$|^rJ$|^\(P\)$|^\(British$|^English\)$|^\(American$|^English\)$|^British English\)$|^noun$|^verb$|^adj\.$|^adjective$|^conj\.$|^conjunction$|^adv\.$|^adverb$|^interj\.$|^interjection$|^art\.$|^article$|^prep\.$|^preposition$|^aux\.$|^auxiliary$|^pron\.$|^pronoun$|^det\.$|^determiner$", words) != None:
        #         arr.append(words)
        # for rs in arr + e_unique_list + i_unique_list + hi_unique_list:
        #     if rs in word_list:
        #         word_list.remove(rs)

        # for words in word_list:
        #     if words[0] != alpha_lower[val] and words[0] != alpha_upper[val]:
        #         print(words, alpha_upper[val])
        # val += 1
        # print(val)
        # print(word_list)

# Day D
# Festival D
# Festival L
# Day M
# Day N
# Eve N

# carrier M

# 2263 2684

        # for word in word_list:
        #     subprocess.run("osx-dictionary {}".format(word) + " >> more_words.txt", shell=True, universal_newlines=True)
        # global val

        # for rs in arr:
        #     if re.search(r"=|\^|\)$|字彙|詞類|英式拼法|註解|^\(British English\)$|^British English\)$|^\(British$|^English\)$|^English）$|^\(American$|^English\)$|\(P\)|rJ|^adj\/noun|^noun$|^verb$|^adj\.$|^adjective$|^conj\.$|^conjunction$|^adv\.$|^adverb$|^interj\.$|^interjection$|^art\.$|^article$|^prep\.$|^preposition$|^aux\.$|^auxiliary$|^pron\.$|^pronoun$|^det\.$|^determiner$|^noun\/|^verb\/|^adj\.\/|^adjective\/|^conj\.\/|^conjunction\/|^adv\.\/|^adverb\/|^interj\.\/|^interjection\/|^art\.\/|^article\/|^prep\.\/|^preposition\/|^aux\.\/|^auxiliary\/|^pron\.\/|^pronoun\/|^det\.\/|^determiner\/|^number\/|^[A-Zb-z]{1}$", rs) != None:
        #         new_words.append(rs)
        #     # if re.search(r",$", rs) != None:
        #     #     print(rs)



        # for rs in new_words:
        #     if rs in arr:
        #         arr.remove(rs)
            # if re.search(r"[ ](?=[^ ]+$)", rs):
        

        
        # global val
        # for rs in arr:
        #     r = rs.split()
        #     # r.split()
        #     # rs = rs[:-1]
        #     if r[0][0] not in alpha_upper:
        #         val += 1
        #         print(r[:-1], val)# 31
    
        # val += (len(word_list))
        
        # global val
        # for rs in arr:
        #     # r = rs.split()
        #     # r.split()
        #     # rs = rs[:-1]
        #     if rs[0][0] in alpha_upper:
        #         val += 1
        #         print(rs, val)#99-6
        # global grandee
        # grandee += arr
        # val += (len(arr))
        # print(arr, val)
        # alpha_words = sorted(arr)
        # print(alpha_words, arr) #2137 + 1 ("article") + 1 ("I") - 1 ("carrier") = 2138
        # print(len(empty_for_now))

        # return word_list

    clean_word_list("filename.txt")

# print(len(grandee)) 


# for word in word_list: '跳躍，反彈' '渴望，日本貨幣單位￥' '包圍，裝邊' '抽象的，摘要' ; sceptic, crosswalk, intelligence, 'adj.  傲慢的', '農產品  (P)', '(P)', '爭吵(P)', 'servicewoman (女性)'
#     subprocess.run("osx-dictionary {}".format(word) + " >> more_words.txt", shell=True, universal_newlines=True)
    
 