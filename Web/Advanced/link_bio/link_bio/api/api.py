import link_bio.url as url
from .supabaseAPI import SupabaseAPI

SUPABASE_API = SupabaseAPI()

async def repo() -> str:
    return url.REPO_URL

async def live(user: str) -> bool:
    if user == "mouredev":
        return True
    return False

async def featured() -> list:
    return SUPABASE_API.featured()