from ..production import *

{% include "ecommerce/apps/ecommerce/settings/partials/common.py" %}

{% if MFE_HOST is defined %}
CORS_ORIGIN_WHITELIST = list(CORS_ORIGIN_WHITELIST) + [
    "{% if ENABLE_HTTPS %}https{% else %}http{% endif %}://{{ MFE_HOST }}",
]
CSRF_TRUSTED_ORIGINS = [
    "{% if ENABLE_HTTPS %}https{% else %}http{% endif %}://{{ MFE_HOST }}",
]
{% endif %}

SOCIAL_AUTH_EDX_OAUTH2_PUBLIC_URL_ROOT = "{% if ENABLE_HTTPS %}https{% else %}http{% endif %}://{{ LMS_HOST }}"

BACKEND_SERVICE_EDX_OAUTH2_KEY = "{{ ECOMMERCE_OAUTH2_KEY }}"

{% if ECOMMERCE_ENABLE_COMPREHENSIVE_THEMING is defined %}
ENABLE_COMPREHENSIVE_THEMING = True
COMPREHENSIVE_THEME_DIRS = ["{{ ECOMMERCE_COMPREHENSIVE_THEME_DIR }}"]
DEFAULT_SITE_THEME = "{{ECOMMERCE_DEFAULT_SITE_THEME}}"
{% endif %}


{{ patch("ecommerce-settings-production") }}
