import os

from dotenv import load_dotenv
from pydantic import ValidationError


def from_env(var: str, throw_err: bool = False) -> str:
    load_dotenv()
    res = os.environ[var]
    if len(res) == 0 and throw_err:
        raise ValidationError(f"Variable {var} is not set!")
    else:
        return res
