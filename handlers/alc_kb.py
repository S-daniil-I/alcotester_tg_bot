from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
drink_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)

drink_keyboard.add(KeyboardButton('Пиво лёгкое (4%)'), KeyboardButton('Пиво обычное/Сидр (5%)'))
drink_keyboard.add(KeyboardButton('Пиво портер/тёмное (6%)'), KeyboardButton('Слабоалкогольные напитки (7%)'))
drink_keyboard.add(KeyboardButton('Пиво крепкое (8%)'), KeyboardButton('Шампанское (10%)'))
drink_keyboard.add(KeyboardButton('Водка (40%)'), KeyboardButton('Коньяк (40%)'))
drink_keyboard.add(KeyboardButton('Виски/Бурбон/Скотч (40%)'), KeyboardButton('Самбука (40%)'))
drink_keyboard.add(KeyboardButton('Вино (12%)'), KeyboardButton('Вермут (Martini и пр.) (15%)'))
drink_keyboard.add(KeyboardButton('Мягкие ликёры (Baileys и пр.) (17%)'), KeyboardButton('Портвейн (20%)'))
drink_keyboard.add(KeyboardButton('Средние ликёры (Malibu и пр.) (20%)'),
                   KeyboardButton('Рижский бальзам и т.п. (30%)'))
drink_keyboard.add(KeyboardButton('Крепкие ликёры (Jagermeister и т.п.) (35%)'),
                   KeyboardButton('Текила/Бренди/Бехеровка и т.п. (38%)'))
drink_keyboard.add(KeyboardButton('Безалкогольное пиво (0.5%)'), KeyboardButton('Кефир старше 3х дней (0.7%)'))
drink_keyboard.add(KeyboardButton('Хлебный квас (0.5%)'), KeyboardButton('Кумыс (1.2%)'))
drink_keyboard.add(KeyboardButton('Ром (39%)'), KeyboardButton('Джин (40%)'))

drink_keyboard.add(KeyboardButton('Абсент лёгкий (60%)'), KeyboardButton('Абсент средний (69%)'))
drink_keyboard.add(KeyboardButton('Настойка боярышника (70%)'), KeyboardButton('Абсент крепкий (80%)'))
drink_keyboard.add(KeyboardButton('Чистый спирт (95%)'))