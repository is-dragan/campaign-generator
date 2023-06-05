import datetime

def select_from_options(prompt, options):
    while True:
        print(f"{prompt} {str(options)}")
        value = input()
        if value in options:
            return value
        print("Неверный ввод, попробуйте еще раз.")

def input_custom(prompt):
    print(prompt)
    return input()

def week_number(dt):
    return dt.strftime('%Y') + 'W' + dt.strftime('%W')

def generate_campaign_name():
    channels = ['Email', 'Push']
    categories = ['Билеты', 'Ещё', 'Контент', 'Маркетинг', 'Продукт', 'ПСЖР', 'Реклама', 'Ресёрч', 'Usercom']
    markets = ['RU', 'AZ', 'BY', 'GE', 'KG', 'KZ', 'UZ']
    contents = ['Билеты', 'Направления', 'Продукт: Короче', 'ПСЖР: Вопросы', 'ПСЖР: Дайджест', 'ПСЖР: Топ-дайджест', 'Советы', 'Фан']
    weeks = ['Текущая', 'Следующая', 'Без недели']
    segments = ['Активные (3 месяца)', 'Вся база', 'Неактивные', 'Новые', 'Спящие (12+ месяцев)', 'Спящие (3-6 месяцев)', 'Спящие (6-12 месяцев)']
    subsegments = ['Не открывали', 'С букингами', 'С серчами, без букингов']

    channel = select_from_options("Выберите канал:", channels)
    category = select_from_options("Выберите категорию:", categories)
    market = select_from_options("Выберите рынок:", markets)
    content = select_from_options("Выберите содержание:", contents)
    campaign_theme = input_custom("Введите тему кампании:")
    week = select_from_options("Выберите неделю:", weeks)
    segment = select_from_options("Выберите сегмент:", segments)
    subsegment = input_custom("Введите подсегмент:")
    versions_number = input_custom("Введите количество версий:")
    iteration = input_custom("Введите номер итерации:")

    if week == 'Текущая':
        week = week_number(datetime.date.today())
    elif week == 'Следующая':
        week = week_number(datetime.date.today() + datetime.timedelta(days=7))

    campaign_name = f"[{category}] {channel} - {market} - {content}"
    if campaign_theme != "":
        campaign_name += f" - {campaign_theme}"
    campaign_name += f" {week} - {segment}"
    if subsegment != "":
        campaign_name += f" - {subsegment}"
    if versions_number != "" and iteration != "":
        campaign_name += f" - i{iteration}.v1-{versions_number}"
    elif versions_number != "":
        campaign_name += f" - v1-{versions_number}"
    elif iteration != "":
        campaign_name += f" - i{iteration}"
    return campaign_name

if __name__ == "__main__":
    print(generate_campaign_name())
