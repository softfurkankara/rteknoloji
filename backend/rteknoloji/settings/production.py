ALLOWED_HOSTS = [
    'rteknoloji.com',
    'www.rteknoloji.com',
]

CSRF_TRUSTED_ORIGINS = [
    "https://rteknoloji.com",
    "https://www.rteknoloji.com"
]

# Reverse Proxy SSL
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Güvenlik Ayarları
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_SSL_REDIRECT = True
DEBUG = False

DATA_UPLOAD_MAX_MEMORY_SIZE = 52 * 1024 * 1024  # 52 MB
FILE_UPLOAD_MAX_MEMORY_SIZE = 52 * 1024 * 1024  # 52 MB
