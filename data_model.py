from dataclasses import dataclass, field
from typing import Literal
from enum import Enum
from dotenv import load_dotenv

import mesop as me
import os

load_dotenv()

Role = Literal["user", "model"]

@dataclass(kw_only=True)
class ChatMessage:
    role: Role = "user"
    content: str = ""
    in_progress: bool = False

class Models(Enum):
    GEMINI_1_5_FLASH = "Gemini 1.5 Flash"
    GEMINI_1_5_PRO = "Gemini 1.5 Pro"
    CLAUDE_3_5_SONNET = "Claude 3.5 Sonnet"

@dataclass
class Conversation:
    model: str = ""
    messages: list[ChatMessage] = field(default_factory=list)

@me.stateclass
class State:
    is_model_picker_dialog_open: bool = False
    input: str = ""
    conversations: list[Conversation] = field(default_factory=list)
    models: list[str] = field(default_factory=list)
    gemini_api_key: str = os.getenv('GOOGLE_API_KEY')
    claude_api_key: str = os.getenv('CLAUDE_API_KEY')

@me.stateclass
class ModelDialogState:
    selected_models: list[str] = field(default_factory=list)
