import reflex as rx
import os

config = rx.Config(
    app_name="link_bio",
    backend_host = os.getenv("API_URL", "https://esteban-web.up.railway.app"),
    is_production = True
)