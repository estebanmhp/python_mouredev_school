import reflex as rx

config = rx.Config(
    app_name="link_bio",
    backend_host = "https://esteban-web.up.railway.app",
    # cors_allowed_origins = [
    #     "http://localhost:3000",
    #     "https://estebanhernandezweb.vercel.app"        
    # ],
    is_production = True
)