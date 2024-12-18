import language_tool_python

def test_spelling():
    """
    Тест проверяет текстовые файлы игры на наличие ошибок орфографии.
    """
    tool = language_tool_python.LanguageTool('ru')  # Проверка русского текста
    with open("game/script.rpy", "r", encoding="utf-8") as f:
        text = f.read()

    matches = tool.check(text)
    assert len(matches) == 0, f"Обнаружены орфографические ошибки: {matches}"
