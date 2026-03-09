from authx import AuthX
from src.core.config.settings import DevAuthConfig

auth_config = DevAuthConfig().create_authx_config()

security = AuthX(config=auth_config)
