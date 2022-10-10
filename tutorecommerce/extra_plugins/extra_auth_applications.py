from tutor import hooks

hooks.Filters.ENV_PATCHES.add_item(
    (
        "openedx-lms-common-settings",
        """
# Discovery and ecommerce applications.
if not ALLOWED_AUTH_APPLICATIONS:
    ALLOWED_AUTH_APPLICATIONS = []
ALLOWED_AUTH_APPLICATIONS += [
    'discovery', 'discovery-sso', 'discovery-dev', 'discovery-sso-dev',
    'ecommerce', 'ecommerce-sso','ecommerce-dev','ecommerce-sso-dev',
    ]
"""
    )
)
