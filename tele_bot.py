import telebot
import surrogates
from Course import get_course


DOLLAR_RUB = 'https://www.google.com/search?q=%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80%D1%8B+%D0%B2+%D1%80%D1%83%D0%B' + \
             '1%D0%BB%D0%B8&oq=%D0%B4%D0%9E%D0%9B%D0%9B%D0%90%D0%A0&gs_lcrp=EgZjaHJvbWUqDQgBEAAYgwEYsQMYgAQyDwg' + \t
             'AEEUYORiDARixAxiABDINCAEQABiDARixAxiABDIKCAIQABixAxiABDINCAMQABiDARixAxiABDINCAQQABiDARixAxiABDIN' + \
             'CAUQABiDARixAxiABDIKCAYQABixAxiABDINCAcQABiDARixAxiABDINCAgQABiDARixAxiABDIHCAkQABiABNIBCTY4NDNqM' + \
             'GoxNagCALACAA&sourceid=chrome&ie=UTF-8'
POUND_RUB = 'https://www.google.com/search?q=aeyns+%D0%B2+%D1%80%D1%83%D0%B1%D0%BB%D0%B8&sca_esv=40ad471a4e6b196f&' + \
            'sca_upv=1&ei=HHvLZfrODaikwPAPscqPsA8&udm=&ved=0ahUKEwj6zI36waiEAxUoEhAIHTHlA_YQ4dUDCBA&uact=5&oq=aeyn' + \
            's+%D0%B2+%D1%80%D1%83%D0%B1%D0%BB%D0%B8&gs_lp=Egxnd3Mtd2l6LXNlcnAiE2FleW5zINCyINGA0YPQsdC70LgyDRAAGIA' + \
            'EGIoFGEMYsQMyBxAAGIAEGAoyBxAAGIAEGAoyBxAAGIAEGAoyBxAAGIAEGAoyBxAAGIAEGAoyBxAAGIAEGAoyBxAAGIAEGAoyBxAA' + \
            'GIAEGApIrTtQtgRYmTNwAXgBkAEAmAGfAqABihGqAQUwLjcuNbgBA8gBAPgBAcICChAAGEcY1gQYsAPCAg0QABiABBiKBRhDGLADw' + \
            'gIZEC4YgAQYigUYQxjHARjRAxjIAxiwA9gBAcICCxAAGIAEGLEDGIMBwgIFEAAYgATCAgYQABgHGB7CAgoQABiABBgNGLEDwgIHEA' + \
            'AYgAQYDcICBhAAGB4YDcICCBAAGAUYHhgN4gMEGAAgQYgGAZAGC7oGBAgBGAg&sclient=gws-wiz-serp'
EURO_RUB = 'https://www.google.com/search?q=%D0%B5%D0%B2%D1%80%D0%BE+%D0%B2+%D1%80%D1%83%D0%B1%D0%BB%D0%B8&sca_esv' + \
           '=40ad471a4e6b196f&sca_upv=1&ei=HoTLZb6RPIKSwPAP1fOMsA8&udm=&oq=%D0%95%D0%B2%D1%80%D0%BE+&gs_lp=Egxnd3M' + \
           'td2l6LXNlcnAiCdCV0LLRgNC-ICoCCAAyFRAAGIAEGIoFGEMYsQMYgwEYRhiCAjIIEAAYgAQYsQMyCxAAGIAEGLEDGIMBMggQABiAB' + \
           'BixAzIIEAAYgAQYsQMyBRAAGIAEMg4QABiABBiKBRixAxiDATIFEAAYgAQyCBAAGIAEGLEDMgUQABiABDIhEAAYgAQYigUYQxixAxi' + \
           'DARhGGIICGJcFGIwFGN0E2AEDSJMqUIcYWIsfcAF4AZABAJgBmgKgAaAGqgEFMS4zLjG4AQHIAQD4AQGoAhTCAhMQABiABBiKBRhDG' + \
           'OoCGLQC2AEBwgIgEAAYgAQYigUY5QIY5QIY6gIYtAIYigMYtwMY1APYAQHCAhYQABgDGI8BGOUCGOoCGLQCGIwD2AECwgIWEC4YAxi' + \
           'PARjlAhjqAhi0AhiMA9gBAsICDhAuGIAEGIoFGLEDGIMBwgIREC4YgAQYsQMYgwEYxwEY0QPCAgsQLhiABBixAxiDAcICChAAGIAEG' + \
           'IoFGEPCAhAQABiABBiKBRhDGLEDGIMB4gMEGAAgQeIDBRIBMSBAugYECAEYB7oGBggCEAEYCroGBggDEAEYEw&sclient=gws-wiz-serp'
HRYVNIA_RUB = 'https://www.google.com/search?q=%D0%B3%D1%80%D0%B8%D0%B2%D0%BD%D1%8B+%D0%B2+%D1%80%D1%83%D0%B1%D0%B' + \
              'B%D0%B8&sca_esv=ce20ddb9e1b59ac9&sca_upv=1&ei=tnPMZZmQDKHAxc8PjOC84AY&udm=&oq=uhbdys+%D0%B2+%D1%80%' + \
              'D1%83%D0%B1%D0%BB%D0%B8&gs_lp=Egxnd3Mtd2l6LXNlcnAiFHVoYmR5cyDQsiDRgNGD0LHQu9C4KgIIADISEAAYgAQYigUYQ' + \
              'xixAxhGGIICMgcQABiABBgKMgcQABiABBgKMgcQABiABBgKMgcQABiABBgKMgcQABiABBgKMgcQABiABBgKMgcQABiABBgKMgcQ' + \
              'ABiABBgKMgcQABiABBgKMh4QABiABBiKBRhDGLEDGEYYggIYlwUYjAUY3QTYAQFI6R5QAFi-D3AAeAGQAQCYAZMBoAGDBaoBAzU' + \
              'uMrgBAcgBAPgBAcICBhAAGAcYHsICBxAAGIAEGA3CAggQABgHGB4YCsICChAAGAUYHhgNGArCAggQABgFGB4YDcICBxAAGIAEGA' + \
              'HCAgoQABiABBgNGLED4gMEGAAgQboGBggBEAEYEw&sclient=gws-wiz-serp'
DIRHAMS_RUB = 'https://www.google.com/search?q=%D0%B4%D0%B8%D1%80%D1%85%D0%B0%D0%BC%D1%8B+%D0%B2+%D1%80%D1%83%D0%B' + \
              '1%D0%BB%D0%B8&sca_esv=ce20ddb9e1b59ac9&sca_upv=1&ei=x6TMZYjKFIidwPAP58qZsA8&udm=&oq=Lbh%5Bfvs+%D0%B' + \
              '2+%D1%80%D1%83%D0%B1%D0%BB%D0%B8&gs_lp=Egxnd3Mtd2l6LXNlcnAiFUxiaFtmdnMg0LIg0YDRg9Cx0LvQuCoCCAAyChAA' + \
              'GIAEGA0YsQMyBxAAGIAEGA0yBxAAGIAEGA0yBxAAGIAEGA0yBxAAGIAEGA0yBxAAGIAEGA0yBxAAGIAEGA0yBxAAGIAEGA0yBxA' + \
              'AGIAEGA0yBxAAGIAEGA1I3yhQAFiFG3AAeAGQAQCYAbUDoAGvCaoBCTUuMS4xLjAuMbgBAcgBAPgBAcICBhAAGAcYHsICCBAAGA' + \
              'cYHhgKwgIIEAAYBRgeGA3CAgwQABiABBgNGEYYggLCAhgQABiABBgNGEYYggIYlwUYjAUY3QTYAQHiAwQYACBBugYGCAEQARgT&' + \
              'sclient=gws-wiz-serp'
YUAN_RUB = 'https://www.google.com/search?q=%D1%8E%D0%B0%D0%BD%D0%B8+%D0%B2+%D1%80%D1%83%D0%B1%D0%BB%D0%B8&sca_esv' + \
           '=ce20ddb9e1b59ac9&sca_upv=1&ei=8arMZf7UFpnZwPAPreOTgA4&udm=&oq=%3Efyb+%D0%B2+%D1%80%D1%83%D0%B1%D0%BB%' + \
           'D0%B8&gs_lp=Egxnd3Mtd2l6LXNlcnAiEj5meWIg0LIg0YDRg9Cx0LvQuCoCCAAyDBAAGIAEGAEYRhiCAjIHEAAYgAQYATIHEAAYgA' + \
           'QYATIHEAAYgAQYATIHEAAYgAQYATIHEAAYgAQYATIHEAAYgAQYATIHEAAYgAQYATIHEAAYgAQYATIHEAAYgAQYATIYEAAYgAQYARhG' + \
           'GIICGJcFGIwFGN0E2AEBSJAeUABYyhFwAHgBkAEAmAG9AqABnQiqAQcwLjIuMi4xuAEByAEA-AEBwgIGEAAYBxgewgILEAAYgAQYAR' + \
           'gKGCriAwQYACBBugYGCAEQARgT&sclient=gws-wiz-serp'
bot = telebot.TeleBot('6315706847:AAF2XDnyBwxmUQM4L_wV0nux0DXnWchESGk')


@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name} {message.from_user.last_name}. ' + \
                     f'Это бот который будет тебе помогать с твоими финансами.')


@bot.message_handler(commands=['course'])
def main(message):
    bot.send_message(message.chat.id, f'🇺🇸{get_course(DOLLAR_RUB)}$ USD\n🇬🇧{get_course(POUND_RUB)}£ GBP\n' + \
                     f'🇪🇺{get_course(EURO_RUB)}€ EUR\n🇺🇦{get_course(HRYVNIA_RUB)}₴ UAH\n🇦🇪{get_course(DIRHAMS_RUB)}' + \
                     f'Dhs AED\n🇨🇳{get_course(YUAN_RUB)}¥ CNY')


@bot.message_handler(func=lambda message: True)
def main(message):
    try:
        message_text = message.text
        currency = message_text.split()
        currency[0] = float(currency[0])
        if len(currency) == 2:
            if 'руб' in currency[1].lower() or currency[1].lower() == \
                    'р' or 'rub' in currency[1].lower() or \
                    currency[1].lower() == 'r' or currency[1].lower() == '₽' or currency[1].lower() == 'rub':
                bot.reply_to(message,
                                 f'======\n🇷🇺{currency[0]}₽ RUB\n\n🇺🇸{round(currency[0] / get_course(DOLLAR_RUB), 2)}' + \
                                 f'$ USD\n🇬🇧{round(currency[0] / get_course(POUND_RUB), 2)}£ GBP\n🇪🇺' + \
                                 f'{round(currency[0] / get_course(EURO_RUB), 2)}€ EUR\n🇺🇦' + \
                                 f'{round(currency[0] / get_course(HRYVNIA_RUB), 2)}₴ UAH\n🇦🇪' + \
                                 f'{round(currency[0] / get_course(DIRHAMS_RUB), 2)}' + \
                                 f'Dhs AED\n🇨🇳{round(currency[0] / get_course(YUAN_RUB), 2)}¥ CNY')
            elif 'дол' in currency[1].lower() or currency[1].lower() == \
                    'д' or 'dol' in currency[1].lower() or \
                    currency[1].lower() == 'd' or currency[1].lower() == '$' or currency[1].lower() == 'usd':
                bot.reply_to(message,
                                 f'======\n🇺🇸{currency[0]}$ USD\n\n🇷🇺{round(currency[0] * get_course(DOLLAR_RUB), 2)}' + \
                                 f'₽ RUB\n🇬🇧{round(currency[0] * get_course(DOLLAR_RUB) / get_course(POUND_RUB), 2)}£ GBP\n🇪🇺' + \
                                 f'{round(currency[0] * get_course(DOLLAR_RUB) / get_course(EURO_RUB), 2)}€ EUR\n🇺🇦' + \
                                 f'{round(currency[0] * get_course(DOLLAR_RUB) / get_course(HRYVNIA_RUB), 2)}₴ UAH\n🇦🇪' + \
                                 f'{round(currency[0] * get_course(DOLLAR_RUB) / get_course(DIRHAMS_RUB), 2)}' + \
                                 f'Dhs AED\n🇨🇳{round(currency[0]  * get_course(DOLLAR_RUB) / get_course(YUAN_RUB), 2)}¥ CNY')
            elif 'фун' in currency[1].lower() or currency[1].lower() == \
                    'ф' or 'pou' in currency[1].lower() or \
                    currency[1].lower() == 'p' or currency[1].lower() == 'gbp':
                print(currency[0] * get_course(POUND_RUB) / get_course(DOLLAR_RUB))
                bot.reply_to(message,
                                 f'======\n🇬🇧{currency[0]}£ GBP\n\n🇷🇺{round(currency[0] * get_course(POUND_RUB), 2)}' + \
                                 f'₽ RUB\n🇺🇸{round(currency[0] * get_course(POUND_RUB) / get_course(DOLLAR_RUB), 2)}$ USD\n🇪🇺' + \
                                 f'{round(currency[0] * get_course(POUND_RUB) / get_course(EURO_RUB), 2)}€ EUR\n🇺🇦' + \
                                 f'{round(currency[0] * get_course(POUND_RUB) / get_course(HRYVNIA_RUB), 2)}₴ UAH\n🇦🇪' + \
                                 f'{round(currency[0] * get_course(POUND_RUB) / get_course(DIRHAMS_RUB), 2)}' + \
                                 f'Dhs AED\n🇨🇳{round(currency[0]  * get_course(POUND_RUB) / get_course(YUAN_RUB), 2)}¥ CNY')
            elif 'евр' in currency[1].lower() or currency[1].lower() == \
                    'е' or 'eur' in currency[1].lower() or  \
                    currency[1].lower() == 'e' or currency[1].lower() == 'eur':
                bot.reply_to(message,
                                 f'======\n🇪🇺{currency[0]}€ EUR\n\n🇷🇺{round(currency[0] * get_course(EURO_RUB), 2)}' + \
                                 f'₽ RUB\n🇬🇧{round(currency[0] * get_course(EURO_RUB) / get_course(POUND_RUB), 2)}£ GBP\n🇺🇸' + \
                                 f'{round(currency[0] * get_course(EURO_RUB) / get_course(DOLLAR_RUB), 2)}$ USD\n🇺🇦' + \
                                 f'{round(currency[0] * get_course(EURO_RUB) / get_course(HRYVNIA_RUB), 2)}₴ UAH\n🇦🇪' + \
                                 f'{round(currency[0] * get_course(EURO_RUB) / get_course(DIRHAMS_RUB), 2)}' + \
                                 f'Dhs AED\n🇨🇳{round(currency[0]  * get_course(EURO_RUB) / get_course(YUAN_RUB), 2)}¥ CNY')
            elif 'гри' in currency[1].lower() or currency[1].lower() == \
                    'г' or 'hry' in currency[1].lower() or \
                    currency[1].lower() == 'h' or currency[1].lower() == 'uah':
                bot.reply_to(message,
                                 f'======\n🇺🇦{currency[0]}₴ UAH\n\n🇷🇺{round(currency[0] * get_course(HRYVNIA_RUB), 2)}' + \
                                 f'₽ RUB\n🇬🇧{round(currency[0] * get_course(HRYVNIA_RUB) / get_course(POUND_RUB), 2)}£ GBP\n🇪🇺' + \
                                 f'{round(currency[0] * get_course(HRYVNIA_RUB) / get_course(EURO_RUB), 2)}€ EUR\n🇺🇸' + \
                                 f'{round(currency[0] * get_course(HRYVNIA_RUB) / get_course(DOLLAR_RUB), 2)}$ USD\n🇦🇪' + \
                                 f'{round(currency[0] * get_course(HRYVNIA_RUB) / get_course(DIRHAMS_RUB), 2)}' + \
                                 f'Dhs AED\n🇨🇳{round(currency[0]  * get_course(HRYVNIA_RUB) / get_course(YUAN_RUB), 2)}¥ CNY')
            elif 'дир' in currency[1].lower() or  currency[1].lower() == \
                    'д' or 'dir' in currency[1].lower() or  \
                    currency[1].lower() == 'di' or currency[1].lower() == 'aed':
                bot.reply_to(message,
                                 f'======\n🇦🇪{currency[0]}Dhs AED\n\n🇷🇺{round(currency[0] * get_course(DIRHAMS_RUB), 2)}' + \
                                 f'₽ RUB\n🇬🇧{round(currency[0] * get_course(DIRHAMS_RUB) / get_course(POUND_RUB), 2)}£ GBP\n🇪🇺' + \
                                 f'{round(currency[0] * get_course(DIRHAMS_RUB) / get_course(EURO_RUB), 2)}€ EUR\n🇺🇦' + \
                                 f'{round(currency[0] * get_course(DIRHAMS_RUB) / get_course(HRYVNIA_RUB), 2)}₴ UAH\n🇺🇸' + \
                                 f'{round(currency[0] * get_course(DIRHAMS_RUB) / get_course(DOLLAR_RUB), 2)}' + \
                                 f'$ USD\n🇨🇳{round(currency[0]  * get_course(DIRHAMS_RUB) / get_course(YUAN_RUB), 2)}¥ CNY')
            elif 'юан' in currency[1].lower() or currency[1].lower() == \
                    'ю' or 'yua' in currency[1].lower() or  \
                    currency[1].lower() == 'y' or currency[1].lower() == 'cny':
                bot.reply_to(message,
                                 f'======\n🇨🇳{currency[0]}¥ CNY\n\n🇷🇺{round(currency[0] * get_course(YUAN_RUB), 2)}' + \
                                 f'₽ RUB\n🇬🇧{round(currency[0] * get_course(YUAN_RUB) / get_course(POUND_RUB), 2)}£ GBP\n🇪🇺' + \
                                 f'{round(currency[0] * get_course(YUAN_RUB) / get_course(EURO_RUB), 2)}€ EUR\n🇺🇦' + \
                                 f'{round(currency[0] * get_course(YUAN_RUB) / get_course(HRYVNIA_RUB), 2)}₴ UAH\n🇦🇪' + \
                                 f'{round(currency[0] * get_course(YUAN_RUB) / get_course(DIRHAMS_RUB), 2)}' + \
                                 f'Dhs AED\n🇺🇸{round(currency[0]  * get_course(YUAN_RUB) / get_course(DOLLAR_RUB), 2)}$ USD')
    except:
        bot.reply_to(message, f'Вы ввели не коректный запрос')


bot.polling(none_stop=True)
