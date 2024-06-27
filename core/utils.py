from django.contrib.auth.hashers import make_password


def get_package_hash(resident_name: str,
                     resident_email: str,
                     resident_phone: str,
                     resident_apto: int) -> str:
    """
    :param resident_name:str
    :param resident_email:str
    :param resident_phone:str
    :param resident_apto:int
    :return:str
    """

    text = f"{resident_name}/{resident_email}/{resident_phone}/{resident_apto}"

    return make_password(text, salt="400000")
