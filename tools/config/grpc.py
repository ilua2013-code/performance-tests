from pydantic import BaseModel, HttpUrl

class GRPCClientConfig(BaseModel):
    host: str
    port: int

    @property
    def client_url(self) -> str:
        return f"{self.host}:{self.port}"