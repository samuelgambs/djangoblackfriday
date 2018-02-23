DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'blackfriday',
        'USER': 'blackfriday',
        'PASSWORD': 'HCYxmw987as9P8T',
        'HOST': 'rds-bf.maxmilhas.com.br',
        'PORT': '3306',
    }
}

ALLOWED_HOSTS = [
    '0.0.0.0',
    '127.0.0.1',
    '10.0.2.187',
    'maxfriday.com.br',
    'www.maxfriday.com.br',
    'maxfriday.maxmilhas.com.br',
    'blackfriday.maxmilhas.com.br',
    'elb-mm-prd-blackfriday-230582365.us-east-1.elb.amazonaws.com'
]

STATIC_ROOT = "/srv/maxfriday/static/"
