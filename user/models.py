from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# --- Kullanıcı Profili ---
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    telefon = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.user.username

# Kullanıcı oluşturulduğunda Profile otomatik oluştur
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


# --- Chat Mesajları ---
class ChatMessage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='chat_messages')

    visitor_name = models.CharField(max_length=50, blank=True, null=True)
    session_key = models.CharField(max_length=40, null=True, blank=True)  # 🔹 yeni alan
    message = models.TextField()
    is_admin = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)


    class Meta:
        ordering = ['timestamp']

    def __str__(self):
        sender = self.user.username if self.user else (self.visitor_name or "Ziyaretçi")
        return f"{sender}: {self.message[:30]}"
