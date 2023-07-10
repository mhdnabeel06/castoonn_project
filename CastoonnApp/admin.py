from django.contrib import admin
from .models import CreatorUserProfile
from .models import ArtistUserProfile

# Register your models here.

admin.site.register(CreatorUserProfile)

admin.site.register(ArtistUserProfile)