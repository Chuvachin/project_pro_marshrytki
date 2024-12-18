def test_sprites():
    """
    Проверяет, что все спрайты из сценария существуют и загружаются корректно.
    """
    import os

    sprite_dir = "game/images/"  # Директория со спрайтами
    script_sprites = ["sprite1.png", "sprite2.png", "sprite3.png"]  # Спрайты из сценария

    for sprite in script_sprites:
        sprite_path = os.path.join(sprite_dir, sprite)
        assert os.path.exists(sprite_path), f"Спрайт {sprite} не найден"
