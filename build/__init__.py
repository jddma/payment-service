URL_PREFIX = '/api/v1'


def url(path: str) -> str:
    if path[0] == '/':
        return f"{URL_PREFIX}{path}"
    else:
        return f"{URL_PREFIX}/{path}"
