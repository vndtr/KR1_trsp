#Задание 1.4, 1.5, 2.1, 2.2
from pydantic import BaseModel, field_validator
import re

class User(BaseModel):
    name: str
    id: int

class UserAge(BaseModel):
    name: str
    age: int

class Feedback(BaseModel):
    name: str
    message: str

    # Валидация имени
    @field_validator("name")
    def validate_name(cls, v):
        if len(v) < 2 or len(v) > 50:
            raise ValueError("Имя должно быть от 2 до 50 символов")
        return v

    # Валидация сообщения
    @field_validator("message")
    def validate_message(cls, v):
        if len(v) < 10 or len(v) > 500:
            raise ValueError("Сообщение должно быть от 10 до 500 символов")
        
        # Проверка на запрещённые слова
        bad_words = ["крингк", "рофл", "вайб"]
        pattern = re.compile("|".join(bad_words), re.IGNORECASE)
        if pattern.search(v):
            raise ValueError("Использование недопустимых слов")
        
        return v