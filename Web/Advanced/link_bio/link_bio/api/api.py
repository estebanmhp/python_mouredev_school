import link_bio.url as url

async def repo() -> str:
    return url.REPO_URL

async def live(user: str) -> bool:
    if user == "mouredev":
        return True
    return False