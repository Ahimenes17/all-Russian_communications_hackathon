import vk_api


class VK:
    def __init__(self, token):
        self.session = vk_api.VkApi(token=token, api_version='5.154')
        self.api = self.session.get_api()
        self.get_user_info('1')

    def get_group_info(self, group_id: str, raw: bool = False):
        """Возвращает информацию о группе через метод `groups.getById`

        :param group_id: ссылка на группу (вида `apiclub` или `public1`, допустимо `https://vk.com/...`)
        :param raw: вид возвращаемого результата. При True функция возвращается необработанный JSON, иначе сформированный вывод
        :return: информация о группе, если введена корректная ссылка, иначе None
        """
        group_id = group_id.split('vk.com/')[-1].split('/')[0].split('?')[0]
        try:
            r = self.api.groups.getById(group_id=group_id).get('groups')[0]
            if not raw:
                r = 'ID: {0}\nНазвание сообщества: {1}'.format(r['id'], r['name'])
            return r
        except Exception as e:
            if raw:
                return {'error': e}
            else:
                if (str(e) == '[100] One of the parameters specified was missing or invalid: group_id not domain') or \
                (str(e) == '[100] One of the parameters specified was missing or invalid: group_ids is undefined'):
                    return 'Введите корректную ссылку на группу'
                return f'Произошла ошибка: {e}'


    def get_user_info(self, user_id: str, raw: bool = False):
        """Возвращает информацию о пользователе через метод `users.get`

        :param user_id: ссылка на пользователя (вида `durov` или `id1`, допустимо `https://vk.com/...`)
        :param raw: вид возвращаемого результата. При True функция возвращается необработанный JSON, иначе сформированный вывод
        :return: информация о пользователе, если введена корректная ссылка, иначе None
        """
        user_id = user_id.split('vk.com/')[-1].split('/')[0].split('?')[0]
        r = self.api.users.get(user_ids=user_id)
        if not r:
            return 'Введите корректную ссылку на пользователя' if not raw else {'error': 'Введите корректную ссылку на пользователя'}
        if not raw:
            r = 'ID: {0}\nИмя: {1}\nФамилия: {2}'.format(r[0]['id'], r[0]['first_name'], r[0]['last_name'])
        return r

    def get_user_info_exec(self, user_id: str, raw: bool = False):
        """Возвращает информацию о пользователе через метод `users.get`, вызванный с помощью `execute`

        :param user_id: ссылка на пользователя (вида `durov` или `id1`, допустимо `https://vk.com/...`)
        :param raw: вид возвращаемого результата. При True функция возвращается необработанный JSON, иначе сформированный вывод
        :return: информация о пользователе, если введена корректная ссылка, иначе None
        """
        user_id = user_id.split('vk.com/')[-1].split('/')[0].split('?')[0]
        r = self.session.method('execute', {'code': 'return API.users.get({{"user_ids": "{0}"}});'.format(user_id)})
        if not r:
            return 'Введите корректную ссылку на пользователя' if not raw else {'error': 'Введите корректную ссылку на пользователя'}
        if not raw:
            r = 'ID: {0}\nИмя: {1}\nФамилия: {2}'.format(r[0]['id'], r[0]['first_name'], r[0]['last_name'])
        return r


if __name__ == "__main__":
    vktoken = 'vk1.a.ylZ-Un_TPTrh1sYn2wu_vNqLDAPXm_FZ5HR3T9AIbBzUwFerAyW373IpUTki-HVU2eL0qF93QXtnkI5Huf0WIeprd3nTwWOvwGyjHv64xjOybBFNTqG5rF1amTUWmLgcXcEKl9cIsIixRX30UBQSp7WDdJYDQyKnyp3uW0mKtVsUucRLgDOqn0dvyxIworGWDuBnrShZjqDYFNYv_e-8Mg'
    vk = VK(vktoken)
    ginfo = vk.get_group_info('ghnet6jdyj')
    uinfo = vk.get_user_info('rghhdfgh')
    print(ginfo)
    print(uinfo)
    u1info = vk.get_user_info_exec('dfghjdjdftj')
    print(u1info)
