import vk_api
import re
from weather import *
from five_day_weather import *
from config import token
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.upload import VkUpload
from vk_api.utils import get_random_id


def main():

    vk_session = vk_api.VkApi(token=token)
    vk = vk_session.get_api()
    upload = VkUpload(vk_session)
    longpoll = VkLongPoll(vk_session)

    image = 'weather_icons/10d.png'

    help_text = """
        Я бот, который поможет посмотреть расписание, а так же покажет другую полезную информацию

        Для начала напиши номер своей группы, а я её запомню, чтобы больше не приходилось её указывать
        """

    # Создаем 2 клавиатуры
    keyboard_1 = VkKeyboard(one_time=False, inline=True)
    keyboard_1.add_button('на Сегодня', color=VkKeyboardColor.POSITIVE)
    keyboard_1.add_button('на Завтра', color=VkKeyboardColor.NEGATIVE)
    keyboard_1.add_line()
    keyboard_1.add_button('на эту неделю', color=VkKeyboardColor.PRIMARY)
    keyboard_1.add_button('на следующую неделю', color=VkKeyboardColor.PRIMARY)

    # Кнопки для погоды
    keyboard_2 = VkKeyboard(one_time=False)
    keyboard_2.add_button('сейчас', color=VkKeyboardColor.POSITIVE)
    keyboard_2.add_button('на сегодня', color=VkKeyboardColor.NEGATIVE)
    keyboard_2.add_line()
    keyboard_2.add_button('на завтра', color=VkKeyboardColor.PRIMARY)
    keyboard_2.add_button('на 5 дней', color=VkKeyboardColor.PRIMARY)

    def write_msg(user_id, message, keyboard):
        vk_session.method('messages.send',
                          {'user_id': user_id, 'keyboard': keyboard.get_keyboard(), 'message': message, 'random_id': get_random_id()})  # r_id - всегда разный

    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW and event.text:
            text = event.text
            user_id = event.user_id
            sender_name = vk.users.get(user_id=event.user_id)[0]['first_name']
            sender_last_name = vk.users.get(user_id=event.user_id)[0]['last_name']
            msg = re.match("^[А-Я]{4}[-]{1}[0-9]{2}[-]{1}[0-9]{2}$", text.upper())

            attachments = []
            upload_image = upload.photo_messages(photos=image)[0]
            attachments.append('photo{}_{}'.format(upload_image['owner_id'], upload_image['user_id']))

            print(f'New form {user_id}, text {text}')
            if (text == 'Привет') or (text == 'привет') or (text == 'начать'):
                vk.messages.send(user_id=event.user_id, random_id=get_random_id(), attachment=','.join(attachments), message='Привет, ' + \
                sender_name + ' ' + sender_last_name)


            # elif msg:
            #     vk.messages.send(user_id=event.user_id, random_id=get_random_id(), message=f'Хорошо, я запомнил, ты учишься в {text}')

            if text.lower() == 'погода в москве':
                if text.lower() == 'на сегодня':
                    print('good')
                    t = Weather()
                    write_msg(event.user_id, t.get_description, keyboard_2)
                elif text.lower() == 'на 5 дней'.lower():
                    w = Weather5Day()
                    write_msg(event.user_id, w.get_info, keyboard_2)
                elif text.lower() == 'на завтра':
                    to = Weather5Day()
                    write_msg(event.user_id, to.get_info_tomorrow, keyboard_2)
                else:
                    vk.messages.send(user_id=event.user_id,random_id=get_random_id(), message='Неизвестная команда')


if __name__ == '__main__':

    main()
