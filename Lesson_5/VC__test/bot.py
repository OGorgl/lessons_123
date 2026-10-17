import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType

# pip install vk_api

# Вставьте сюда ваш токен группы
token = ""
vk = vk_api.VkApi(token=token)
# Работа с сообщениями через LongPoll
longpoll = VkLongPoll(vk)
vk_api_method = vk.get_api()

print("Бот запущен и слушает сообщения...")

for event in longpoll.listen():
    # Проверяем, пришло ли новое сообщение
    if event.type == VkEventType.MESSAGE_NEW and event.to_me:
        # Текст сообщения от пользователя
        msg_text = event.text.lower()
        user_id = event.user_id

        if msg_text == "привет":
            vk_api_method.messages.send(
                user_id=user_id,
                message="Привет! Я бот на Python.",
                random_id=0,
            )
        else:
            vk_api_method.messages.send(
                user_id=user_id,
                message="Я тебя не понял. Напиши 'привет'.",
                random_id=0,
            )


