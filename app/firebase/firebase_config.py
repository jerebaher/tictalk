settings = get_settings()

cred = credentials.Certificate(settings.FIREBASE_CREDENTIALS_PATH)
firebase_admin.initialize_app(cred)