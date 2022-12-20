# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'mysql.connector.django',
        'NAME': 'cars_database',
        'HOST': 'localhost',
        'USER': 'root',
        'PASSWORD' : 'password'
    }
}

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure--tu!w4dg3d%$b)h&@=l$_mah)!6^)h27rek2ppm*-b%*%mxynw'