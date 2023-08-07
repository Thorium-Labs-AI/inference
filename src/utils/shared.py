import os

from dotenv import load_dotenv


def from_env(var: str, throw_err: bool = False) -> str:
    load_dotenv()
    res = os.environ[var]
    if len(res) == 0 and throw_err:
        raise Exception(f"Variable {var} is not set!")
    else:
        return res
