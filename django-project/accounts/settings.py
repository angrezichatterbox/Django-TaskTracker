# settings.py

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / "db.sqlite3",
    },
    'auth_db': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / "auth_db.sqlite3",
    },
    'user_db': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / "user_db.sqlite3",
    },
    # Add more databases as needed
}

DATABASE_ROUTERS = ['path.to.AuthRouter']
