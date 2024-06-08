from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    client_base_url: str = 'www.external_client.com'
    client_path: str = '/stats?uid={}'
    client_headers: dict = {"Authorization": "Bearer some_token_111"}

    batch_size: int = 100

    model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8')


settings = Settings()
