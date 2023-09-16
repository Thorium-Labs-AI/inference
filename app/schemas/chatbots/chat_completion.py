from pydantic import BaseModel


class OpenAIChatCompletionUsage(BaseModel):
    completion_tokens: int
    prompt_tokens: int


class OpenAIResponseMessage(BaseModel):
    content: str


class OpenAIChatCompletionInput(BaseModel):
    role: str
    content: str


class OpenAIResponseChoice(BaseModel):
    message: OpenAIResponseMessage


class OpenAIChatCompletionResponse(BaseModel):
    choices: list[OpenAIResponseChoice]
    usage: OpenAIChatCompletionUsage
