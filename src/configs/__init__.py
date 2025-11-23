
from dynaconf import Dynaconf

# создаём объект настроек
settings = Dynaconf(
    envvar_prefix="MEDIA_STORAGE",          # префикс для переменных окружения (по желанию)
    settings_files=["configs/settings.toml"]  # путь до settings.toml относительно корня проекта
)