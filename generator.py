import streamlit as st
from datetime import date
from datetime import timedelta
import calendar

def get_week_number(week_type):
    today = date.today()
    if week_type == 'Текущая':
        return today.strftime("%YW%W")
    elif week_type == 'Следующая':
        next_week = today + timedelta(days=7)
        return next_week.strftime("%YW%W")
    else:
        return ""

def campaign_generator():
    st.title('Генератор названий кампаний')

    channel = st.selectbox('Выберите канал:', ['Email', 'Push'])
    category = st.selectbox('Выберите категорию:', ['Билеты', 'Ещё', 'Контент', 'Маркетинг', 'Продукт', 'ПСЖР', 'Реклама', 'Ресёрч', 'Usercom'])
    market = st.selectbox('Выберите рынок:', ['RU', 'AZ', 'BY', 'GE', 'KG', 'KZ', 'UZ'])
    content = st.selectbox('Выберите содержание:', ['Билеты', 'Направления', 'Продукт: Короче', 'ПСЖР: Вопросы', 'ПСЖР: Дайджест', 'ПСЖР: Топ-дайджест', 'Советы', 'Фан'])
    campaign_theme = st.text_input('Введите тему кампании:')
    week = st.selectbox('Выберите неделю:', ['Текущая', 'Следующая', 'Без недели'])
    segment = st.selectbox('Выберите сегмент:', ['Активные (3 месяца)', 'Вся база', 'Неактивные', 'Новые', 'Спящие (12+ месяцев)', 'Спящие (3-6 месяцев)', 'Спящие (6-12 месяцев)'])
    subsegment = st.text_input('Введите подсегмент:')
    num_versions = st.text_input('Введите число версий:')
    iteration = st.text_input('Введите итерацию:')
    
    category_dict = {
        'ПСЖР': 'ПСЖР',
        'Маркетинг': 'Marketing',
        'Контент': 'Content',
        'Реклама': 'Adv',
        'Билеты': 'Cheaptickets',
        'Продукт': 'Product',
        'Ресёрч': 'Research',
        'Ещё': 'Ещё',
        'Usercom': 'Usercom'
    }

    content_dict = {
        'Билеты': 'Билеты',
        'Направления': 'Направления',
        'Продукт: Короче': 'Продукт: Короче',
        'ПСЖР: Вопросы': 'ПСЖР: Вопросы',
        'ПСЖР: Дайджест': 'ПСЖР: Дайджест',
        'ПСЖР: Топ-дайджест': 'ПСЖР: Топ-дайджест',
        'Советы': 'Советы',
        'Фан': 'Фан'
    }

    campaign_name = f"[{category_dict[category]}] {channel} - {market} - {content_dict[content]}"
    if campaign_theme:
        campaign_name += f" - {campaign_theme}"
    campaign_name += f" {get_week_number(week)} - {segment}"
    if subsegment:
        campaign_name += f" - {subsegment}"
    if num_versions and iteration:
        campaign_name += f" - i{iteration}.v1-{num_versions}"
    elif num_versions:
        campaign_name += f" - v1-{num_versions}"
    elif iteration:
        campaign_name += f" - i{iteration}"

    if st.button('Сгенерировать имя кампании'):
        st.success(campaign_name)

if __name__ == "__main__":
    campaign_generator()
