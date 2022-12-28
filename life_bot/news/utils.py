"""Module with utils for news parsing"""

import ssl


def fix_ssl():
    if hasattr(ssl, "_create_unverified_context"):
        ssl._create_default_https_context = ssl._create_unverified_context
