# Курсач Кристины: Оценка производительности обр портала компании
## Реализация ТЗ:
### 1. Общий контент делится на два типа: Курсы и справочники
Курс - набор уроков (от 4 до 16) по определенной Тематике;
    Тематика - одна из списка тематик
    Урок - объект, имеющий след. характеристики:
        Номер
        Тип урока:
            Видео (долгое, среднее, короткое)
            Текст (долгий, средний, короткий)
            Тест с ограничением по времени (долгий, средний, короткий)
        Длительность полного изучения:
            У Короткого: от 5 минут до 20 минут
            У Среднего: от 30 минут до 50 минут
            У Длинного: от 60 минут до 120 минут
        Сложность обработки для системы:
            У Текста: 1
            У Видео: 2
            У Теста: 3
Справочник - набор текстов, которыми могут пользоваться все пользователи. Имеют стандартный набор характеристик:
    Длительность: 10 минут
    Сложность обработки для системы: 1

### 2. Пользователь:
    Интересы по темам (3 темы)
        Набор тем примерно в 2 раза шире, чем набор Тем на портале
    Общее время на портале за один день (от 5 минут до 24 часов) (время1)
    Набор текущих подписок (случайно выбирается при генерации клиента одно из двух):
        Или пустой
            Он заполняться не будет
        Или занятый
            Заполняется следующим образом: берётся курс(ы) (случайно от 1 до 3),
            который существует на портале, берётся урок из этого курса (случайно),
            который пользователь посмотрел последним, начинает смотреть следующий урок

### 3. Ресурсов как таковых нет. Поэтому показателем симуляции будет только ВРЕМЯ.
Время, которое пользователь провел на портале, начиная с того момента, как он был сгенерирован, и оканчивая моментом, когда он сделал на портале все что хотел, или все что мог успеть сделать за то время, что у него было (время1 п.2).
