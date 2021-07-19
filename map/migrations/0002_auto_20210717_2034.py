# Generated by Django 3.2.5 on 2021-07-17 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='unit',
            name='building',
        ),
        migrations.RemoveField(
            model_name='unit',
            name='corpus',
        ),
        migrations.RemoveField(
            model_name='unit',
            name='street',
        ),
        migrations.AddField(
            model_name='unit',
            name='address',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Адрес'),
        ),
        migrations.AlterField(
            model_name='unit',
            name='district',
            field=models.CharField(choices=[(None, 'Выберите район'), ('Заводской район', 'Заводской'), ('Центральный район', 'Центральный'), ('Куйбышевский район', 'Куйбышевский'), ('Новоильинский раон', 'Новоильинский'), ('Орджоникидзевский район', 'Орджоникидзевский'), ('Кузнецкий район', 'Кузнецкий'), ('Алексеевка', 'Алексеевка'), ('Анисимово', 'Анисимово'), ('Апанас', 'Апанас'), ('Атаманово', 'Атаманово'), ('Баевка', 'Баевка'), ('Бардина', 'Бардина'), ('Бедарево', 'Бедарево'), ('Безруково', 'Безруково'), ('Бенжереп 1-й', 'Бенжереп 1'), ('Березово', 'Березово'), ('Боровково', 'Боровково'), ('Букино', 'Букино'), ('Верхний Калтан', 'Верхний Калтан'), ('Веселый', 'Веселый'), ('Гавриловка', 'Гавлировка'), ('Елань', 'Елань'), ('Ерунаково', 'Ерунаково'), ('Есаулка', 'Есаулка'), ('Загорский', 'Звгорский'), ('Зеленый Луг', 'Зеленый Луг'), ('Иганино', 'Иганино'), ('Ильинка', 'Ильинка'), ('Казанково', 'Казанково'), ('Калтан', 'Калтан'), ('Керегешь', 'Керегешь'), ('Ключи', 'Ключи'), ('Костенково', 'Костенково'), ('Красинск', 'Красинск'), ('Красная Орловка', 'Красная Орловка'), ('Красулино', 'Красулино'), ('Кругленькое', 'Кругленькое'), ('Крутая', 'Крутая'), ('Кузедеево', 'Кузедеево'), ('Кульчаны', 'Кульчаны'), ('Куртуково', 'Куртуково'), ('Лыс', 'Лыс'), ('Малиновка', 'Малиновка'), ('Малышев лог', 'Малышев Лог'), ('Металлургов', 'Металлургов'), ('Мир', 'Мир'), ('Митино', 'Митино'), ('Михайловка', 'Михайловка'), ('Мостовая', 'Мостовая'), ('Мунай', 'Мунай'), ('Недорезово', 'Недорезово'), ('Осинники', 'Осинники'), ('Осиновое Плесо', 'Осиновое Плесо'), ('Подгорный', 'Подгорный'), ('Подкорчияк', 'Подкорчияк'), ('Постоянный', 'Постоянный'), ('Пушкино', 'Пушкино'), ('Рассвет', 'Рассвет'), ('Сарбала', 'Сарбала'), ('Сары-Чумыш', 'Сары Чумыш'), ('Северный', 'Северный'), ('Сметанино', 'Сметанино'), ('Сосновка', 'Сосновка'), ('Староабашево', 'Староабашево'), ('Степной', 'Степной'), ('Тайлеп', 'Тайлеп'), ('Тальжино', 'Тальжино'), ('Таргай', 'Таргай'), ('Таргайский Дом Отдыха', 'Таргайский Дом Отдыха'), ('Терехино', 'Терехино'), ('Увал', 'Увал'), ('Усково', 'Усково'), ('Успенка', 'Успенка'), ('Усть-Аскарлы', 'Усть Аскарлы'), ('Федоровка', 'Федоровка'), ('Черемза', 'Черемза'), ('Черный Калтан', 'Черный Калтан'), ('Чистая Грива', 'Чистая Грива'), ('Чистогорский', 'Чистогорский'), ('Чичербаево', 'Чичербаево'), ('Шорохово', 'Шорохово'), ('Шушталеп', 'Шушталеп'), ('Южный', 'Южный')], default='Выберите район', max_length=100, null=True, verbose_name='Район города'),
        ),
    ]