# ======================== settings.py ============================
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static_root')
]

STATIC_ROOT = os.path.join(BASE_DIR, 'static/')
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media_root')



# ======================== urls.py ================================
from django.conf import settings
from django.conf.urls.static import static


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# ======================= models.py ===============================

CHOICES = (
    ('Male', 'M'),
    ('Female', 'F'),
)

def get_absolute_url(self):
    return reverse('courses:detail', kwargs={'slug': self.slug})

@property
    def lessons(self):
        return self.lesson_set.all().order_by('position')
