import asyncio
from vkbottle import Bot, Message
from vkbottle.tools import Keyboard, Text, OpenLink, Location
from vkbottle.longpoll import LongPoll

# pip install vkbottle

TOKEN = "your_group_token_here"

bot = Bot(token=TOKEN)
lp = LongPoll(bot)

# Хранилище состояний пользователей (в памяти)
user_states = {}


def create_main_keyboard():
    """Создаёт главную клавиатуру"""
    keyboard = Keyboard(one_time=False)  # one_time=False - клавиатура не исчезает после нажатия
    
    keyboard.add(Text("📋 Меню"), color="positive")
    keyboard.add(Text("❓ Помощь"), color="secondary")
    keyboard.row()  # Новая строка
    keyboard.add(Text("🌐 Сайт"), color="primary")
    keyboard.add(Text("📍 Локация"), color="default")
    
    return keyboard.get_json()


def create_menu_keyboard():
    """Клавиатура меню"""
    keyboard = Keyboard(one_time=True)
    
    keyboard.add(Text("📊 Статистика"), color="positive")
    keyboard.add(Text("⚙️ Настройки"), color="secondary")
    keyboard.row()
    keyboard.add(Text("🔙 Назад"), color="negative")
    
    return keyboard.get_json()


@bot.on.message(text=["привет", "старт", "/start"])
async def handler_start(message: Message):
    """Приветствие пользователя"""
    user_id = message.from_id
    user_states[user_id] = "main"  # Устанавливаем состояние
    
    await message.answer(
        "👋 Привет! Я умный бот.\n\n"
        "Выбери действие из меню ниже:",
        keyboard=create_main_keyboard()
    )


@bot.on.message(text="📋 Меню")
async def handler_menu(message: Message):
    """Показываем меню"""
    user_id = message.from_id
    user_states[user_id] = "menu"
    
    await message.answer(
        "📋 Главное меню:\n\n"
        "• 📊 Статистика - узнать статистику\n"
        "• ⚙️ Настройки - изменить настройки\n"
        "• 🔙 Назад - вернуться в главное меню",
        keyboard=create_menu_keyboard()
    )


@bot.on.message(text="📊 Статистика")
async def handler_stats(message: Message):
    """Показываем статистику"""
    user_id = message.from_id
    
    # Имитация получения статистики
    stats_text = (
        "📊 Твоя статистика:\n\n"
        f"• ID пользователя: {user_id}\n"
        f"• Сообщений отправлено: 1\n"
        f"• Статус: Активен ✅\n\n"
        "Это демо-статистика. В реальном боте здесь будут реальные данные!"
    )
    
    await message.answer(stats_text, keyboard=create_menu_keyboard())


@bot.on.message(text="⚙️ Настройки")
async def handler_settings(message: Message):
    """Настройки пользователя"""
    user_id = message.from_id
    user_states[user_id] = "settings"
    
    keyboard = Keyboard(one_time=True)
    keyboard.add(Text("🔔 Уведомления: ВКЛ"), color="positive")
    keyboard.add(Text("🌙 Темная тема: ВЫКЛ"), color="secondary")
    keyboard.row()
    keyboard.add(Text("🔙 Назад"), color="negative")
    
    await message.answer(
        "⚙️ Настройки:\n\n"
        "Здесь можно изменить параметры бота.",
        keyboard=keyboard.get_json()
    )


@bot.on.message(text="❓ Помощь")
async def handler_help(message: Message):
    """Помощь"""
    help_text = (
        "❓ Помощь:\n\n"
        "Доступные команды:\n"
        "• привет / старт - начать общение\n"
        "• меню - показать главное меню\n"
        "• помощь - эта справка\n\n"
        "Также ты можешь использовать кнопки внизу экрана 👇"
    )
    
    await message.answer(help_text, keyboard=create_main_keyboard())


@bot.on.message(text="🌐 Сайт")
async def handler_website(message: Message):
    """Открываем сайт"""
    keyboard = Keyboard(one_time=True)
    keyboard.add(OpenLink("https://vk.com", "Перейти на VK"))
    keyboard.row()
    keyboard.add(Text("🔙 Назад"), color="negative")
    
    await message.answer(
        "🌐 Вот ссылка на наш сайт:",
        keyboard=keyboard.get_json()
    )


@bot.on.message(text="📍 Локация")
async def handler_location(message: Message):
    """Отправляем локацию"""
    # Отправляем геолокацию (координаты Москвы)
    await message.answer(
        "📍 Вот наша локация:",
        latitude=55.7558,
        longitude=37.6173
    )
    
    # После локации показываем главную клавиатуру
    await asyncio.sleep(1)
    await message.answer(
        "Что ещё хочешь узнать?",
        keyboard=create_main_keyboard()
    )


@bot.on.message(text="🔙 Назад")
async def handler_back(message: Message):
    """Возврат в главное меню"""
    user_id = message.from_id
    user_states[user_id] = "main"
    
    await message.answer(
        "🔙 Возвращаемся в главное меню...",
        keyboard=create_main_keyboard()
    )


@bot.on.message(text=["🔔 Уведомления: ВКЛ", "🔔 Уведомления: ВЫКЛ"])
async def handler_notifications(message: Message):
    """Переключение уведомлений"""
    current_text = message.text
    
    if "ВКЛ" in current_text:
        new_text = "🔔 Уведомления: ВЫКЛ"
        status = "выключены"
        color = "secondary"
    else:
        new_text = "🔔 Уведомления: ВКЛ"
        status = "включены"
        color = "positive"
    
    keyboard = Keyboard(one_time=True)
    keyboard.add(Text(new_text), color=color)
    keyboard.add(Text("🌙 Темная тема: ВЫКЛ"), color="secondary")
    keyboard.row()
    keyboard.add(Text("🔙 Назад"), color="negative")
    
    await message.answer(
        f"✅ Уведомления {status}!",
        keyboard=keyboard.get_json()
    )


@bot.on.message()
async def handler_default(message: Message):
    """Обработчик всех остальных сообщений"""
    user_id = message.from_id
    current_state = user_states.get(user_id, "main")
    
    # Если пользователь в каком-то состоянии, обрабатываем соответственно
    if current_state == "settings":
        await message.answer(
            "⚙️ Вы в настройках. Используйте кнопки для изменения параметров.",
            keyboard=create_menu_keyboard()
        )
    else:
        await message.answer(
            "🤔 Я не понял команду.\n\n"
            "Напиши 'привет' или используй кнопки меню 👇",
            keyboard=create_main_keyboard()
        )


if __name__ == "__main__":
    print("🚀 Бот запущен и слушает сообщения...")
    print("💡 Доступные функции:")
    print("   • Клавиатуры с кнопками")
    print("   • Состояния пользователей")
    print("   • Геолокация")
    print("   • Ссылки")
    print("   • Переключение настроек")
    bot.run_polling()