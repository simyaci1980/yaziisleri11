from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth, messages
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .models import ChatMessage
import requests

# -------------------- LOGIN --------------------
def login(request):
    if request.method == 'POST':
        username = request.POST['username'].strip()
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'Hatalı Kullanıcı Adı ya da Parola')
            return redirect('login')
    else:
        return render(request, 'user/login.html')

# -------------------- REGISTER --------------------
def register(request):
    if request.method == 'POST':
        username = request.POST['username'].strip()
        email = request.POST['email'].strip()
        password = request.POST['password']
        repassword = request.POST['repassword']
        telefon = request.POST['telefon'].strip()

        context = {
            'username': username,
            'email': email,
            'telefon': telefon,
        }

        if " " in username:
            messages.warning(request, "Kullanıcı adında boşluk olamaz.")
            return render(request, 'user/register.html', context)

        if len(password) < 6:
            messages.warning(request, "Şifreniz en az 6 karakter olmalı.")
            return render(request, 'user/register.html', context)

        if password != repassword:
            messages.warning(request, "Parolalar eşleşmiyor.")
            return render(request, 'user/register.html', context)

        try:
            validate_email(email)
        except ValidationError:
            messages.warning(request, "Geçerli bir e-mail adresi giriniz.")
            return render(request, 'user/register.html', context)

        if User.objects.filter(username=username).exists():
            messages.warning(request, "Bu kullanıcı adı daha önce alınmış.")
            return render(request, 'user/register.html', context)

        if User.objects.filter(email=email).exists():
            messages.warning(request, "Bu e-mail adresi ile daha önce kayıt olunmuş.")
            return render(request, 'user/register.html', context)

        # Kullanıcı oluştur (sinyal Profile'ı otomatik oluşturacak)
        user = User.objects.create_user(username=username, password=password, email=email)
        user.save()

        # Telefonu profile'a kaydet
        user.profile.telefon = telefon
        user.profile.save()

        messages.success(request, "Hesabınız başarıyla oluşturuldu.")
        return redirect('login')

    return render(request, 'user/register.html')

# -------------------- LOGOUT --------------------
def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('onindex')

# -------------------- ÖDEME SAYFASI --------------------
def odeme_sayfasi(request):
    return render(request, 'user/odeme_sayfasi.html')

# -------------------- ÖDEME BİLDİRİM --------------------
TELEGRAM_TOKEN = "8396849258:AAGNywR-UlF20pftP09JtXGiL_VSY_iv4S0"  # Örnek
CHAT_ID = "1551759004"  # Senin chat ID

@login_required
def odeme_bildirim(request):
    if request.method == "POST":
        telefon = request.user.profile.telefon

        if not telefon:
            messages.error(request, "Telefon numaranız sistemde kayıtlı değil. Lütfen profilinizi güncelleyin.")
            return redirect("odeme_bildirim")

        mesaj = (
            f"💳 Yeni Ödeme Bildirimi\n\n"
            f"Kullanıcı: {request.user.username}\n"
            f"Tutar: 1000 TL\n"
            f"Telefon: {telefon}\n"
            f"Admin paneli: https://gorevdeyukselmeyaziislerimudur.pythonanywhere.com/admin/"
        )

        url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
        data = {"chat_id": CHAT_ID, "text": mesaj}

        try:
            requests.post(url, data=data)
            messages.success(request, "Ödeme bildiriminiz gönderildi ✅")
        except:
            messages.error(request, "Bildirim gönderilirken hata oluştu ❌")

        return redirect("odeme_bildirim")

    return render(request, "user/odeme.html")

# -------------------- CHAT API --------------------
import os, re, requests
from .models import ChatMessage

LAST_UPDATE_FILE = "last_update.txt"
TELEGRAM_TOKEN = "8396849258:AAGNywR-UlF20pftP09JtXGiL_VSY_iv4S0"

def fetch_telegram_messages():
    # Son update_id’yi oku
    if os.path.exists(LAST_UPDATE_FILE):
        with open(LAST_UPDATE_FILE, "r") as f:
            try:
                last_update_id = int(f.read().strip())
            except ValueError:
                last_update_id = 0
    else:
        last_update_id = 0

    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/getUpdates?offset={last_update_id + 1}"

    try:
        # 🛡 Telegram API çağrısı
        r = requests.get(url, timeout=5)
        r.raise_for_status()  # HTTP hatalarını yakalar
        data = r.json()
    except Exception as e:
        # ❗ Telegram bağlantısı başarısızsa siteyi çökertmez
        print(f"[Telegram Hatası] Bağlantı kurulamadı: {e}")
        return  # fonksiyondan çık, hata vermeden

    # 🔽 Gelen mesajları işle
    for update in data.get("result", []):
        update_id = update["update_id"]

        if "message" in update:
            text = update["message"].get("text", "")
            user_name = update["message"]["from"].get("first_name", "Admin")

            # 🔹 Adminin cevabında session=(...) var mı kontrol et
            match = re.match(r"\(session=(?P<sid>[a-zA-Z0-9]+)\)\s*(?P<msg>.*)", text)

            if match:
                session_key = match.group("sid")
                pure_text = match.group("msg")

                # Aynı admin mesajı DB'de yoksa ekle
                if not ChatMessage.objects.filter(
                    session_key=session_key,
                    message=pure_text,
                    is_admin=True
                ).exists():
                    ChatMessage.objects.create(
                        session_key=session_key,
                        visitor_name="Admin",
                        message=pure_text,
                        is_admin=True
                    )

        # Güncel offset’i sakla
        last_update_id = update_id

    # ✅ Son ID’yi güncelle
    with open(LAST_UPDATE_FILE, "w") as f:
        f.write(str(last_update_id))



from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import ChatMessage
import requests
from django.db.models import Q

# Telegram bilgilerin
TELEGRAM_TOKEN = "8396849258:AAGNywR-UlF20pftP09JtXGiL_VSY_iv4S0"
CHAT_ID = "1551759004"




@csrf_exempt
def chat_api(request):
    # Session key oluştur
    session_key = request.session.session_key
    if not session_key:
        request.session.create()
        session_key = request.session.session_key

    # Telegram mesajlarını DB'ye çek
    fetch_telegram_messages()


    if request.method == "GET":
        # 🔹 Ziyaretçi kendi mesajlarını görecek
        # 🔹 Admin mesajları sadece aynı session_key için gözükecek
        messages = ChatMessage.objects.filter(
            Q(session_key=session_key, is_admin=False) |  # Ziyaretçinin kendi mesajları
            Q(session_key=session_key, is_admin=True)    # O session’a özel admin cevapları
        ).order_by("timestamp")

        data = [
            {
                "id": m.id,
                "user": "Admin" if m.is_admin else (m.visitor_name or "Ziyaretçi"),
                "message": m.message,
                "time": m.timestamp.strftime("%H:%M")
            }
            for m in messages
        ]
        return JsonResponse(data, safe=False)

    elif request.method == "POST":
        text = request.POST.get("text", "").strip()

        if not text:
            return JsonResponse({"status": "error", "message": "Mesaj boş"}, status=400)

        if request.user.is_authenticated:
            # 🔹 Kullanıcı giriş yaptıysa
            ChatMessage.objects.create(
                user=request.user,
                visitor_name=request.user.username,  # kullanıcı adı yazılsın
                message=text,
                is_admin=False,
                session_key=session_key
            )
            name = request.user.username
        else:
            # 🔹 Giriş yapmamışsa ziyaretçi
            name = request.POST.get("name", "Ziyaretçi").strip()
            ChatMessage.objects.create(
                visitor_name=name,
                message=text,
                is_admin=False,
                session_key=session_key
            )

        # Telegram’a da gönder
        telegram_text = f"(session={session_key})\n{name}: {text}"


                # Önce session bilgisini gönder
        requests.get(
          f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage",
          params={"chat_id": CHAT_ID, "text": f"(session={session_key})"}
        )
#Ardından mesaj içeriğini gönder
        requests.get(
            f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage",
            params={"chat_id": CHAT_ID, "text": f"{name}: {text}"}
)


        return JsonResponse({"status": "ok"})



# -------------------- ONINDEX --------------------
def onindex(request):
    if request.method == "POST":
        text = request.POST.get("message")
        if text:
            ChatMessage.objects.create(visitor_name="Ziyaretçi", message=text)
        return redirect("onindex")

    messages = ChatMessage.objects.filter(user=request.user).order_by("timestamp")
    return render(request, "onsayfa/onindex.html", {"messages": messages})

