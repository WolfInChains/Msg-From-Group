import vk_api

print("Запуск бота...")
print("Авторизация...")

f = open("authorization.txt", "r")
group_token = f.read()

vk = vk_api.VkApi(token=group_token)
vk._auth_token()
vk.get_api()

print("\nБот запущен")


def send_msg(chat_id: int, message: str, attachment: str = ""):
    return vk.method("messages.send", {**locals(), "random_id": 0})


chat = int(input("\nВведите айди чата: "))

while True:
    try:
        a = input("Введите сообщение: ")
        send_msg(chat, f'{a}')
    except Exception as e:
        print(repr(e))
