from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth, messages
from django.core.validators import validate_email
from django.core.exceptions import ValidationError

# LOGIN
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


# REGISTER
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

        # Telefonu profile'a kaydet (sinyal ile zaten profile var)
        user.profile.telefon = telefon
        user.profile.save()

        messages.success(request, "Hesabınız başarıyla oluşturuldu.")
        return redirect('login')

    return render(request, 'user/register.html')



# LOGOUT
def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('onindex')
    
# views.py
from django.shortcuts import render

def odeme_sayfasi(request):
    return render(request, 'user/odeme_sayfasi.html')

import requests
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

TELEGRAM_TOKEN = "8396849258:AAGNywR-UlF20pftP09JtXGiL_VSY_iv4S0"  # Örnek
CHAT_ID = "1551759004"  # Senin kullanıcı/chat id


@login_required
def odeme_bildirim(request):
    if request.method == "POST":
        # 🔹 Telefonu artık kullanıcı profilinden alıyoruz
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
