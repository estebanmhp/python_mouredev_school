import reflex as rx
from link_bio.api.api import featured

class PageState(rx.State):
    featured_info: list

    async def featured_links(self):
        self.featured_info = await featured()