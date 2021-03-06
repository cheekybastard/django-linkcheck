from django.conf import settings

EXTERNAL_RECHECK_INTERVAL = getattr(settings, 'LINKCHECK_EXTERNAL_RECHECK_INTERVAL', 10080) # 1 week
EXTERNAL_REGEX_STRING = getattr(settings, 'LINKCHECK_EXTERNAL_REGEX_STRING', r'^https?://')
MAX_CHECKS_PER_RUN = getattr(settings, 'LINKCHECK_MAX_CHECKS_PER_RUN', -1)
MEDIA_PREFIX = getattr(settings, 'LINKCHECK_MEDIA_PREFIX', '/media/')
RESULTS_PER_PAGE = getattr(settings, 'LINKCHECK_RESULTS_PER_PAGE', 500)
SITE_DOMAINS = getattr(settings, 'LINKCHECK_SITE_DOMAINS', [])
MAX_URL_LENGTH = getattr(settings, 'LINKCHECK_MAX_URL_LENGTH', 255)