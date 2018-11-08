from celery import task
from django.conf import settings
from django.core.mail import send_mail
from django.template import loader
from django.core.cache import caches

cache = caches["confirm"]

@task
def send_verify_mail(url,user_id,reciever):
    title = "血色浪漫"
    content = ""
    template=loader.get_template("user/email.html")
    html = template.render({"url":url})

    email_from = settings.DEFAULT_FROM_EMAIL

    send_mail(title,content,email_from,[reciever],html_message=html)

    cache.set(url.split("/")[-1],user_id,settings.VERIFY_CODE_MAX_AGE)