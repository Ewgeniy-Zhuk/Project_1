def get_mask_card_number(number_card: str) -> str:
    """
    Функция  принимает на вход номер карты в виде числа и возвращает маску номера по правилу
    XXXX XX** **** XXXX
    """

    if len(number_card) == 16:
        mask_card = str(number_card[:6] + "******" + number_card[12:])
        number_card_output = " ".join(mask_card[i: i + 4] for i in range(0, len(mask_card), 4))
        return number_card_output
    else:
        return "Не корректный номер карты !"


print(get_mask_card_number(input("Введите номер карты")))


def get_mask_account(number_account: str) -> str:
    """
    Функция принимает на вход номер счета в виде числа и возвращает маску номера по правилу **XXXX
    """
    number_account_output = str("**" + number_account[-4:])
    return number_account_output


print(get_mask_account((input("Введите номер счета"))))
