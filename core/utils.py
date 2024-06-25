from django.contrib.auth.hashers import make_password


def get_package_hash(resident_name: str, resident_email: str, resident_apto: int) -> str:
    text = f"{resident_name}{resident_email}{resident_apto}"
    return make_password(text)
