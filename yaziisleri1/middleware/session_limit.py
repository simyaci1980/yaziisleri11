from django.contrib.sessions.models import Session
from django.utils import timezone
from django.http import HttpResponse

class SessionLimitMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Kullanıcı mevcut bir oturuma sahip mi kontrol edin
        if request.user.is_authenticated:
            # Kullanıcının mevcut oturumunu bulun
            user_sessions = Session.objects.filter(expire_date__gte=timezone.now(), 
                                                   session_key__in=request.user.session_keys)
            # Kullanıcının aynı anda kaç oturumu olduğunu kontrol edin
            max_sessions = 1  # İzin verilen maksimum oturum sayısı
            if user_sessions.count() >= max_sessions:
                # Kullanıcı zaten izin verilen maksimum oturum sayısına ulaşmışsa,
                # yeni bir oturum oluşturmasına izin verme
                return HttpResponse("Maksimum oturum limitine ulaşıldı. Başka bir cihazdan giriş yapamazsınız.")
        # Middleware zincirini devam ettir
        response = self.get_response(request)
        return response
