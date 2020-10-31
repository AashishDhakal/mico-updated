from django.core.mail.backends.smtp import EmailBackend


class ConfiguredEmailBackend(EmailBackend):
    def __init__(self, host=None, port=None, username=None, password=None,
                 use_tls=None, fail_silently=None, use_ssl=None, timeout=None,
                 ssl_keyfile=None, ssl_certfile=None,
                 **kwargs):

        from common.models import EmailSetting
        configuration = EmailSetting.objects.first()

        super(ConfiguredEmailBackend, self).__init__(
             host = configuration.email_host if host is None else host,
             port = configuration.email_port if port is None else port,
             username = configuration.email_host_user if username is None else username,
             password = configuration.email_host_password if password is None else password,
             use_tls = configuration.email_use_tls if use_tls is None else use_tls,
             fail_silently = True,
             **kwargs)


__all__ = ['ConfiguredEmailBackend']