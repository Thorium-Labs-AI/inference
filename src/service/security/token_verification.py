import os
import jwt
from configparser import ConfigParser


def get_auth0_config(config_env=None):
    if config_env == ".config":
        config = ConfigParser()
        config.read('.config')
        config = config["AUTH0"]
    else:
        config = {
            "DOMAIN": os.getenv("DOMAIN", "asteriskchat.us.auth0.com"),
            "API_AUDIENCE": os.getenv("API_AUDIENCE", "asterisk-chat-server"),
            "ISSUER": os.getenv("ISSUER", "https://asteriskchat.us.auth0.com/"),
            "ALGORITHMS": os.getenv("ALGORITHMS", "RS256"),
        }
    return config



class Auth0TokenVerifier:
    def __init__(self, token):
        self.signing_key = None
        self.token = token
        self.config = get_auth0_config()

        jwks_url = f'https://{self.config["DOMAIN"]}/.well-known/jwks.json'
        self.jwks_client = jwt.PyJWKClient(jwks_url)

    def verify(self):
        try:
            self.signing_key = self.jwks_client.get_signing_key_from_jwt(
                self.token
            ).key
        except jwt.exceptions.PyJWKClientError as error:
            return {"status": "error", "msg": error.__str__()}
        except jwt.exceptions.DecodeError as error:
            return {"status": "error", "msg": error.__str__()}

        try:
            payload = jwt.decode(
                self.token,
                self.signing_key,
                algorithms=self.config["ALGORITHMS"],
                audience=self.config["API_AUDIENCE"],
                issuer=self.config["ISSUER"],
            )
        except Exception as e:
            return {"status": "error", "message": str(e)}

        return payload
