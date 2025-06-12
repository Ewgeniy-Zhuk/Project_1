import masks


def mask_account_card(meaning: str) -> str:
    """
    Функция определяющая, что подается на ввод и обрабатывает согласнно введенным данным
    """
    letters = ""
    numbers = ""
    for symbol in meaning:
        if symbol.isdigit():
            numbers += symbol
        else:
            letters += symbol
    if letters == "Счет ":
        return f"{letters}{masks.get_mask_account(numbers)}"
    else:
        return f"{letters}{masks.get_mask_card_number(numbers)}"


print(mask_account_card(input("Введите карту или счет")))


def get_date(date_string: str) -> str:
    """
    Функция, которая принимает на вход строку с датой в формате "2024-03-11T02:26:18.671407"
    и возвращает строку с датой в формате "ДД.ММ.ГГГГ"
    """
    year, month, day = date_string.split("T")[0].split("-")
    return f"{day}.{month}.{year}"


print(get_date(input("Введите дату")))