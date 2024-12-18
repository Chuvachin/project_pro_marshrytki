def test_dialogues_and_choices():
    """
    Тест проверяет, что все выборы работают корректно,
    а диалоги не содержат пустых строк.
    """
    import renpy.exports as renpy

    script = renpy.game.script
    for label in script.namemap.values():
        if hasattr(label, 'block'):
            for line in label.block:
                # Проверка строк диалогов
                if isinstance(line, renpy.ast.Say):
                    assert line.what.strip(), f"Пустой диалог в {label.name}"

                # Проверка выборов
                if isinstance(line, renpy.ast.Menu):
                    for choice, _ in line.items:
                        assert choice.strip(), f"Пустой вариант выбора в {label.name}"
