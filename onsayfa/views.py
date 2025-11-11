from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.shortcuts import render

# Create your views here.
# localhost:8000
# http://127.0.0.1:8000  AYNISI HA

def onindex(request):                                         # bu fonksiyon çağırıldığında onsayfa uygulamasının index.html dosyasını getir
	return render (request, 'onsayfa/onindex.html')

def sorular(request):
	return render (request, 'onsayfa/sorular.html')


def index(request):                                         # bu fonksiyon çağırıldığında onsayfa uygulamasının index.html dosyasını getir
	return render (request, 'onsayfa/index.html')

def hakkimizda(request):
	return render (request, 'onsayfa/hakkimizda.html')      # bu fonksiyon çağırıldığında onsayfa uygulamasının hakkimizda.html dosyasını getir


def ornek1(request):
	return render (request, 'onsayfa/ornek1.html')


def yetki(request):
	return render (request, 'onsayfa/yetki.html')


def turkce(request):
	user_groups = request.user.groups.all()
	if Group.objects.get(name='asiluyelik') in user_groups:
		return render (request, 'onsayfa/turkce.html')
	else:
		return render(request,'onsayfa/yetki.html')

def anayasa1(request):
	user_groups = request.user.groups.all()
	if Group.objects.get(name='asiluyelik') in user_groups:
		return render (request, 'onsayfa/anayasa1.html')
	else:
		return render(request,'onsayfa/yetki.html')

def darisüreler(request):
	return render (request, 'onsayfa/darisüreler.html')


def bim5mad(request):
	return render (request, 'onsayfa/bim5mad.html')




def devletintemelorg(request):
	user_groups = request.user.groups.all()
	if Group.objects.get(name='asiluyelik') in user_groups:
		return render (request, 'onsayfa/devletintemelorg.html')
	else:
		return render(request,'onsayfa/yetki.html')

def anayasaNot(request):
	user_groups = request.user.groups.all()
	if Group.objects.get(name='asiluyelik') in user_groups:
		return render (request, 'onsayfa/anayasaNot.html')
	else:
		return render(request,'onsayfa/yetki.html')

def turkıyebmm(request):
	user_groups = request.user.groups.all()
	if Group.objects.get(name='asiluyelik') in user_groups:
		return render (request, 'onsayfa/turkıyebmm.html')
	else:
		return render(request,'onsayfa/yetki.html')

def inkilapTarihi(request):
	user_groups = request.user.groups.all()
	if Group.objects.get(name='asiluyelik') in user_groups:
		return render (request, 'onsayfa/inkilapTarihi.html')
	else:
		return render(request,'onsayfa/yetki.html')

def ulusalGuvenlik(request):
	user_groups = request.user.groups.all()
	if Group.objects.get(name='asiluyelik') in user_groups:
		return render (request, 'onsayfa/ulusalGuvenlik.html')
	else:
		return render(request,'onsayfa/yetki.html')

def KAMUiktisatitesebbusleri(request):
	user_groups = request.user.groups.all()
	if Group.objects.get(name='asiluyelik') in user_groups:
		return render (request, 'onsayfa/KAMUiktisatitesebbusleri.html')
	else:
		return render(request,'onsayfa/yetki.html')

def devlettescum1kar(request):
	user_groups = request.user.groups.all()
	if Group.objects.get(name='asiluyelik') in user_groups:
		return render (request, 'onsayfa/devlettescum1kar.html')
	else:
		return render(request,'onsayfa/yetki.html')

def ilidaresi(request):
	user_groups = request.user.groups.all()
	if Group.objects.get(name='asiluyelik') in user_groups:
		return render (request, 'onsayfa/ilidaresi.html')
	else:
		return render(request,'onsayfa/yetki.html')

def ilozelidaresi(request):
	user_groups = request.user.groups.all()
	if Group.objects.get(name='asiluyelik') in user_groups:
		return render (request, 'onsayfa/ilozelidaresi.html')
	else:
		return render(request,'onsayfa/yetki.html')

def belediyekanunu(request):
	user_groups = request.user.groups.all()
	if Group.objects.get(name='asiluyelik') in user_groups:
		return render (request, 'onsayfa/belediyekanunu.html')
	else:
		return render(request,'onsayfa/yetki.html')

def buyuksehir(request):
	user_groups = request.user.groups.all()
	if Group.objects.get(name='asiluyelik') in user_groups:
		return render (request, 'onsayfa/buyuksehir.html')
	else:
		return render(request,'onsayfa/yetki.html')

def devletmemuru657(request):
	user_groups = request.user.groups.all()
	if Group.objects.get(name='asiluyelik') in user_groups:
		return render (request, 'onsayfa/devletmemuru657.html')
	else:
		return render(request,'onsayfa/yetki.html')

def dmksureler(request):
	user_groups = request.user.groups.all()
	if Group.objects.get(name='asiluyelik') in user_groups:
		return render (request, 'onsayfa/dmksureler.html')
	else:
		return render(request,'onsayfa/yetki.html')

def halklailiskiler(request):
	user_groups = request.user.groups.all()
	if Group.objects.get(name='asiluyelik') in user_groups:
		return render (request, 'onsayfa/halklailiskiler.html')
	else:
		return render(request,'onsayfa/yetki.html')

def etik(request):
	user_groups = request.user.groups.all()
	if Group.objects.get(name='asiluyelik') in user_groups:
		return render (request, 'onsayfa/etik.html')
	else:
		return render(request,'onsayfa/yetki.html')

def bakanlıkmerkez(request):
	user_groups = request.user.groups.all()
	if Group.objects.get(name='asiluyelik') in user_groups:
		return render (request, 'onsayfa/bakanlıkmerkez.html')
	else:
		return render(request,'onsayfa/yetki.html')

def adaletKomisyonlarınnYapısı(request):
	user_groups = request.user.groups.all()
	if Group.objects.get(name='asiluyelik') in user_groups:
		return render (request, 'onsayfa/adaletKomisyonlarınnYapısı.html')
	else:
		return render(request,'onsayfa/yetki.html')

def ulusalYargıAgıBilisim(request):
	user_groups = request.user.groups.all()
	if Group.objects.get(name='asiluyelik') in user_groups:
		return render (request, 'onsayfa/ulusalYargıAgıBilisim.html')
	else:
		return render(request,'onsayfa/yetki.html')

def maliYonetim5018(request):
	user_groups = request.user.groups.all()
	if Group.objects.get(name='asiluyelik') in user_groups:
		return render (request, 'onsayfa/maliYonetim5018.html')
	else:
		return render(request,'onsayfa/yetki.html')

def noluCumhur(request):
	user_groups = request.user.groups.all()
	if Group.objects.get(name='asiluyelik') in user_groups:
		return render (request, 'onsayfa/noluCumhur.html')
	else:
		return render(request,'onsayfa/yetki.html')

def genelge154(request):
	user_groups = request.user.groups.all()
	if Group.objects.get(name='asiluyelik') in user_groups:
		return render (request, 'onsayfa/genelge154.html')
	else:
		return render(request,'onsayfa/yetki.html')

def genelge124(request):
	user_groups = request.user.groups.all()
	if Group.objects.get(name='asiluyelik') in user_groups:
		return render (request, 'onsayfa/genelge124.html')
	else:
		return render(request,'onsayfa/yetki.html')

def genelge16(request):
	user_groups = request.user.groups.all()
	if Group.objects.get(name='asiluyelik') in user_groups:
		return render (request, 'onsayfa/genelge16.html')
	else:
		return render(request,'onsayfa/yetki.html')

def genelge161(request):
	user_groups = request.user.groups.all()
	if Group.objects.get(name='asiluyelik') in user_groups:
		return render (request, 'onsayfa/genelge161.html')
	else:
		return render(request,'onsayfa/genelge161.html')

def genelge128(request):
	user_groups = request.user.groups.all()
	if Group.objects.get(name='asiluyelik') in user_groups:
		return render (request, 'onsayfa/genelge128.html')
	else:
		return render(request,'onsayfa/genelge128.html')

def genelge63(request):
	user_groups = request.user.groups.all()
	if Group.objects.get(name='asiluyelik') in user_groups:
		return render (request, 'onsayfa/genelge63.html')
	else:
		return render(request,'onsayfa/genelge63.html')

def genelge630(request):
	user_groups = request.user.groups.all()
	if Group.objects.get(name='asiluyelik') in user_groups:
		return render (request, 'onsayfa/genelge630.html')
	else:
		return render(request,'onsayfa/genelge630.html')

def genelge69(request):
	user_groups = request.user.groups.all()
	if Group.objects.get(name='asiluyelik') in user_groups:
		return render (request, 'onsayfa/genelge69.html')
	else:
		return render(request,'onsayfa/genelge69.html')

def genelge690(request):
	user_groups = request.user.groups.all()
	if Group.objects.get(name='asiluyelik') in user_groups:
		return render (request, 'onsayfa/genelge690.html')
	else:
		return render(request,'onsayfa/yetki.html')

def genelge104(request):
	user_groups = request.user.groups.all()
	if Group.objects.get(name='asiluyelik') in user_groups:
		return render (request, 'onsayfa/genelge104.html')
	else:
		return render(request,'onsayfa/yetki.html')

def genelge107(request):
	user_groups = request.user.groups.all()
	if Group.objects.get(name='asiluyelik') in user_groups:
		return render (request, 'onsayfa/genelge107.html')
	else:
		return render(request,'onsayfa/yetki.html')

def genelge109(request):
	user_groups = request.user.groups.all()
	if Group.objects.get(name='asiluyelik') in user_groups:
		return render (request, 'onsayfa/genelge109.html')
	else:
		return render(request,'onsayfa/yetki.html')

def genelge168(request):
	user_groups = request.user.groups.all()
	if Group.objects.get(name='asiluyelik') in user_groups:
		return render (request, 'onsayfa/genelge168.html')
	else:
		return render(request,'onsayfa/yetki.html')

def genelge79(request):
	user_groups = request.user.groups.all()
	if Group.objects.get(name='asiluyelik') in user_groups:
		return render (request, 'onsayfa/genelge79.html')
	else:
		return render(request,'onsayfa/yetki.html')

def yargikolları(request):
	user_groups = request.user.groups.all()
	if Group.objects.get(name='asiluyelik') in user_groups:
		return render (request, 'onsayfa/yargikolları.html')
	else:
		return render(request,'onsayfa/yetki.html')

def adliye5235(request):
	user_groups = request.user.groups.all()
	if Group.objects.get(name='asiluyelik') in user_groups:
		return render (request, 'onsayfa/adliye5235.html')
	else:
		return render(request,'onsayfa/yetki.html')

def idare2576(request):
	user_groups = request.user.groups.all()
	if Group.objects.get(name='asiluyelik') in user_groups:
		return render (request, 'onsayfa/idare2576.html')
	else:
		return render(request,'onsayfa/yetki.html')

def onuncukısım(request):
	user_groups = request.user.groups.all()
	if Group.objects.get(name='asiluyelik') in user_groups:
		return render (request, 'onsayfa/onuncukısım.html')
	else:
		return render(request,'onsayfa/yetki.html')

def imza5070(request):
	user_groups = request.user.groups.all()
	if Group.objects.get(name='asiluyelik') in user_groups:
		return render (request, 'onsayfa/imza5070.html')
	else:
		return render(request,'onsayfa/yetki.html')

def hukukmuh445(request):
	user_groups = request.user.groups.all()
	if Group.objects.get(name='asiluyelik') in user_groups:
		return render (request, 'onsayfa/hukukmuh445.html')
	else:
		return render(request,'onsayfa/yetki.html')

def ceza38a(request):
	user_groups = request.user.groups.all()
	if Group.objects.get(name='asiluyelik') in user_groups:
		return render (request, 'onsayfa/ceza38a.html')
	else:
		return render(request,'onsayfa/yetki.html')

def bam5madde(request):
	user_groups = request.user.groups.all()
	if Group.objects.get(name='asiluyelik') in user_groups:
		return render (request, 'onsayfa/bam5madde.html')
	else:
		return render(request,'onsayfa/yetki.html')

def bim5madd(request):
	user_groups = request.user.groups.all()
	if Group.objects.get(name='asiluyelik') in user_groups:
		return render (request, 'onsayfa/bim5madd.html')
	else:
		return render(request,'onsayfa/yetki.html')

def segbis(request):
	user_groups = request.user.groups.all()
	if Group.objects.get(name='asiluyelik') in user_groups:
		return render (request, 'onsayfa/segbis.html')
	else:
		return render(request,'onsayfa/yetki.html')

def tebkveeleki(request):
	user_groups = request.user.groups.all()
	if Group.objects.get(name='asiluyelik') in user_groups:
		return render (request, 'onsayfa/tebkveeleki.html')
	else:
		return render(request,'onsayfa/yetki.html')

def resmiyazısma(request):
	user_groups = request.user.groups.all()
	if Group.objects.get(name='asiluyelik') in user_groups:
		return render (request, 'onsayfa/resmiyazısma.html')
	else:
		return render(request,'onsayfa/yetki.html')

def tebligatkanunu(request):
	user_groups = request.user.groups.all()
	if Group.objects.get(name='asiluyelik') in user_groups:
		return render (request, 'onsayfa/tebligatkanunu.html')
	else:
		return render(request,'onsayfa/yetki.html')

def tebligatyonetmelik(request):
	user_groups = request.user.groups.all()
	if Group.objects.get(name='asiluyelik') in user_groups:
		return render (request, 'onsayfa/tebligatyonetmelik.html')
	else:
		return render(request,'onsayfa/yetki.html')

def elektroniktebligatyonetmelik(request):
	user_groups = request.user.groups.all()
	if Group.objects.get(name='asiluyelik') in user_groups:
		return render (request, 'onsayfa/elektroniktebligatyonetmelik.html')
	else:
		return render(request,'onsayfa/yetki.html')

def baslangıc4721(request):
	user_groups = request.user.groups.all()
	if Group.objects.get(name='asiluyelik') in user_groups:
		return render (request, 'onsayfa/baslangıc4721.html')
	else:
		return render(request,'onsayfa/yetki.html')

def kısım4721(request):
	user_groups = request.user.groups.all()
	if Group.objects.get(name='asiluyelik') in user_groups:
		return render (request, 'onsayfa/kısım4721.html')
	else:
		return render(request,'onsayfa/yetki.html')

def Altıyuzseksenuc4721(request):
	user_groups = request.user.groups.all()
	if Group.objects.get(name='asiluyelik') in user_groups:
		return render (request, 'onsayfa/Altıyuzseksenuc4721.html')
	else:
		return render(request,'onsayfa/yetki.html')

def cezakanunu5237(request):
	user_groups = request.user.groups.all()
	if Group.objects.get(name='asiluyelik') in user_groups:
		return render (request, 'onsayfa/cezakanunu5237.html')
	else:
		return render(request,'onsayfa/yetki.html')

def idariyargılama2577(request):
	user_groups = request.user.groups.all()
	if Group.objects.get(name='asiluyelik') in user_groups:
		return render (request, 'onsayfa/idariyargılama2577.html')
	else:
		return render(request,'onsayfa/yetki.html')

def kısım6100(request):
	user_groups = request.user.groups.all()
	if Group.objects.get(name='asiluyelik') in user_groups:
		return render (request, 'onsayfa/kısım6100.html')
	else:
		return render(request,'onsayfa/yetki.html')

def kısım5271(request):
	user_groups = request.user.groups.all()
	if Group.objects.get(name='asiluyelik') in user_groups:
		return render (request, 'onsayfa/kısım5271.html')
	else:
		return render(request,'onsayfa/yetki.html')

def adaletbakanlıgıdisiplin(request):
	user_groups = request.user.groups.all()
	if Group.objects.get(name='asiluyelik') in user_groups:
		return render (request, 'onsayfa/adaletbakanlıgıdisiplin.html')
	else:
		return render(request,'onsayfa/yetki.html')

def idarisüreler(request):
	user_groups = request.user.groups.all()
	if Group.objects.get(name='asiluyelik') in user_groups:
		return render (request, 'onsayfa/idarisüreler.html')
	else:
		return render(request,'onsayfa/yetki.html')

def cezakanunu5271(request):
	user_groups = request.user.groups.all()
	if Group.objects.get(name='asiluyelik') in user_groups:
		return render (request, 'onsayfa/cezakanunu5271.html')
	else:
		return render(request,'onsayfa/yetki.html')

def harclarkanunu492(request):
	user_groups = request.user.groups.all()
	if Group.objects.get(name='asiluyelik') in user_groups:
		return render (request, 'onsayfa/harclarkanunu492.html')
	else:
		return render(request,'onsayfa/yetki.html')

def bamhizmetleri(request):
	user_groups = request.user.groups.all()
	if Group.objects.get(name='asiluyelik') in user_groups:
		return render (request, 'onsayfa/bamhizmetleri.html')
	else:
		return render(request,'onsayfa/yetki.html')

def bimhizmetleri(request):
	user_groups = request.user.groups.all()
	if Group.objects.get(name='asiluyelik') in user_groups:
		return render (request, 'onsayfa/bimhizmetleri.html')
	else:
		return render(request,'onsayfa/yetki.html')

def bamkayıtlar(request):
	user_groups = request.user.groups.all()
	if Group.objects.get(name='asiluyelik') in user_groups:
		return render (request, 'onsayfa/bamkayıtlar.html')
	else:
		return render(request,'onsayfa/yetki.html')

def hukukmuhakemesi6100(request):
	user_groups = request.user.groups.all()
	if Group.objects.get(name='asiluyelik') in user_groups:
		return render (request, 'onsayfa/hukukmuhakemesi6100.html')
	else:
		return render(request,'onsayfa/yetki.html')

def süreler(request):
	user_groups = request.user.groups.all()
	if Group.objects.get(name='asiluyelik') in user_groups:
		return render (request, 'onsayfa/süreler.html')
	else:
		return render(request,'onsayfa/yetki.html')

def infaz5275(request):
	user_groups = request.user.groups.all()
	if Group.objects.get(name='asiluyelik') in user_groups:
		return render (request, 'onsayfa/infaz5275.html')
	else:
		return render(request,'onsayfa/yetki.html')

def sorucoz(request):
	user_groups = request.user.groups.all()
	if Group.objects.get(name='asiluyelik') in user_groups:
		return render (request, 'onsayfa/sorucoz.html')
	else:
		return render(request,'onsayfa/yetki.html')

def denebakem(request):
	user_groups = request.user.groups.all()
	if Group.objects.get(name='asiluyelik') in user_groups:
		return render (request, 'onsayfa/denebakem.html')
	else:
		return render(request,'onsayfa/yetki.html')

def bilgiedin(request):
	user_groups = request.user.groups.all()
	if Group.objects.get(name='asiluyelik') in user_groups:
		return render (request, 'onsayfa/bilgiedin.html')
	else:
		return render(request,'onsayfa/yetki.html')

def dilekçehak(request):
	user_groups = request.user.groups.all()
	if Group.objects.get(name='asiluyelik') in user_groups:
		return render (request, 'onsayfa/dilekçehak.html')
	else:
		return render(request,'onsayfa/yetki.html')

def unvanyön(request):
	user_groups = request.user.groups.all()
	if Group.objects.get(name='asiluyelik') in user_groups:
		return render (request, 'onsayfa/unvanyön.html')
	else:
		return render(request,'onsayfa/yetki.html')

def sinavatama(request):
	user_groups = request.user.groups.all()
	if Group.objects.get(name='asiluyelik') in user_groups:
		return render (request, 'onsayfa/sinavatama.html')
	else:
		return render(request,'onsayfa/yetki.html')

def hukukdurus(request):
	user_groups = request.user.groups.all()
	if Group.objects.get(name='asiluyelik') in user_groups:
		return render (request, 'onsayfa/hukukdurus.html')
	else:
		return render(request,'onsayfa/yetki.html')




