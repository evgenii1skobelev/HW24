import os

from api import PetFriends
from settings import valid_email, valid_password, valid_email1

pf = PetFriends()

def test_get_api_key(email=valid_email, password=valid_password):
    status, result = pf.get_api_key(email, password)
    assert status == 200
    assert 'key' in result

def test_get_all_pets_with_valid_key(filter=''):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.get_list_of_pets(auth_key, filter)
    assert status == 200
    assert len(result['pets']) > 0
def test_post_new_pet(name='Пес', animal_type='Собака', age=4):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet(auth_key, name, animal_type, age)
    assert status == 200
    assert result['name'] == name
def test_successful_delete_self_pet():
    """Проверяем возможность удаления питомца"""

    # Получаем ключ auth_key и запрашиваем список своих питомцев
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    # Проверяем - если список своих питомцев пустой, то добавляем нового и опять запрашиваем список своих питомцев
    if len(my_pets['pets']) == 0:
        pf.add_new_pet(auth_key, "Суперкот", "кот", "3", "images/dog1.jpg")
        _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    # Берём id первого питомца из списка и отправляем запрос на удаление
    pet_id = my_pets['pets'][0]['id']
    status, _ = pf.delete_pet(auth_key, pet_id)

    # Ещё раз запрашиваем список своих питомцев
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    # Проверяем что статус ответа равен 200 и в списке питомцев нет id удалённого питомца
    assert status == 200
    assert pet_id not in my_pets.values()
def test_successful_update_self_pet_info(name='Anton', animal_type='kot', age=4):
    """Проверяем возможность обновления информации о питомце"""
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
    if len(my_pets['pets']) > 0:
        status, result = pf.update_pet_info(auth_key, my_pets['pets'][0]['id'], name, animal_type, age)
        assert status == 200
        assert result['name'] == name
    else:
        # если спиок питомцев пустой, то выкидываем исключение с текстом об отсутствии своих питомцев
        raise Exception("There is no my pets")
def test_post_new_pet5(name='Песссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссс', animal_type='Собака', age='4'):
    """Проверяем возможность создание питомца с длинным именем"""
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet(auth_key, name, animal_type, age)
    assert status == 200
    assert result['name'] == name
def test_post_new_pet4(name='Антонио', animal_type='Собака', age=-6):
    """ Проверяем возможность создание питомца с отрицательным возрастом"""
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet(auth_key, name, animal_type, age)
    assert status == 200
    assert result['name'] == name
def test_post_new_pet3(name='Пес', animal_type='Собака'):
    """Проверяем возможность создание питомца без 1 параметра"""
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet(auth_key, name, animal_type)
    assert status == 200
    assert result['name'] == name
def test_post_new_pet2(name='AsdФывйц12!+$', animal_type='Собака', age=4):
    """ Проверяем возможность создание питомца c именем содержащие различные символы"""
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet(auth_key, name, animal_type, age)
    assert status == 200
    assert result['name'] == name
def test_post_new_pet1(name='Антонио', animal_type='Собака', age=8):
    """ Проверяем возможность создание питомца с неправильным ключом авторизации"""
    _, auth_key = pf.get_api_key(valid_email1, valid_password)
    status, result = pf.add_new_pet(auth_key, name, animal_type, age)
    assert status == 403
def test_get_api_key6(email=valid_email1, password=valid_password):
    """Проверяем возможность получения ключа с неправильными данными"""
    status, result = pf.get_api_key(email, password)
    assert status == 403
def test_set_photo7(pet_photo='images/dog1.jpg'):
    """Проверяем возможность обновления фотографии животного"""
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
    status, result = pf.add_new_pet1(auth_key, my_pets['pets'][0]['id'],pet_photo)
    assert status == 200
def test_post_new_pet8(name='Антонио', animal_type='Собака', age='Семнадцать'):
    """ Проверяем возможность создание питомца с возрастом принимающий буквенное значение"""
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet(auth_key, name, animal_type, age)
    assert status == 200
    assert result['name'] == name




