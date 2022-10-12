from ..devstack import *

{% include "ecommerce/apps/ecommerce/settings/partials/common.py" %}

{% if MFE_HOST is defined %}
CORS_ORIGIN_WHITELIST = list(CORS_ORIGIN_WHITELIST) + [
    "http://{{ MFE_HOST }}:{{ ECOMMERCE_MFE_APP['port'] }}",
    "http://{{ MFE_HOST }}:{{ ECOMMERCE_PAYMENT_MFE_APP['port'] }}",
]
CSRF_TRUSTED_ORIGINS = [
    "http://{{ MFE_HOST }}:{{ ECOMMERCE_MFE_APP['port'] }}",
]
{% endif %}

SOCIAL_AUTH_EDX_OAUTH2_PUBLIC_URL_ROOT = "http://{{ LMS_HOST }}:8000"

BACKEND_SERVICE_EDX_OAUTH2_KEY = "{{ ECOMMERCE_OAUTH2_KEY_DEV }}"

{% if ECOMMERCE_ENABLE_COMPREHENSIVE_THEMING is defined %}
ENABLE_COMPREHENSIVE_THEMING = True
COMPREHENSIVE_THEME_DIRS = ["{{ ECOMMERCE_COMPREHENSIVE_THEME_DIR }}"]
DEFAULT_SITE_THEME = "{{ECOMMERCE_DEFAULT_SITE_THEME}}"
{% endif %}

{{ patch("ecommerce-settings-development") }}
