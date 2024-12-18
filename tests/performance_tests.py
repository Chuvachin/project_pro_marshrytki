import time


def test_scene_load_time():
    """
    Тест проверяет, что сцены загружаются за приемлемое время.
    """
    scenes_to_test = ["scene1", "scene2", "scene3"]  # Список сцен
    max_load_time = 2.0  # Максимальное время загрузки (в секундах)

    for scene in scenes_to_test:
        start_time = time.time()
        renpy.call_in_new_context(scene)
        load_time = time.time() - start_time
        assert load_time <= max_load_time, f"Сцена {scene} загружается слишком долго: {load_time} секунд"
