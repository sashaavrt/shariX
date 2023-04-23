REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_RENDERER_CLASSES':[
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        #'rest_framework.permissions.AllowAny',
        #'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ),
}

SPAGHETTI_SAUCE = {
    'apps': ['auth', 'SharixAdmin', 
             'tickets', 'admin', 
             'flatpages', 'sessions', 'sites', 'metaservicesynced'],
    'show_fields': False,
    'show_proxy':True,
}
GRAPH_MODELS = {
  'all_applications': True,
  'group_models': True,
}