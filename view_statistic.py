import pickle
import matplotlib.pyplot as plt


def get_statistics():
    with open('sim.pickle', 'rb') as reader:
        data = pickle.load(reader)
    return data


def popular_themes(statistics):
    x = []
    y = []
    for i in range(len(statistics)):
        client_res = statistics[i]['studiedResources']
        for res in client_res:
            if res['resource'].theme not in x:
                x.append(res['resource'].theme)
                y.append(1)
            else:
                y[x.index(res['resource'].theme)] += 1
    fig = plt.figure(figsize=(8, 6))
    plt.bar(x, y)
    plt.xticks(rotation=90)
    plt.ylabel('Кол-во просмотренного контента')
    plt.title('Количество просмотренного контента по Темам')
    plt.show()


def popular_lesson_types(statistics):
    x = ['Справочник', 'Текст', 'Видео', 'Тест']
    y = [0, 0, 0, 0]
    for i in range(len(statistics)):
        client_res = statistics[i]['studiedResources']
        for res in client_res:
            if res['resource'].type == 'Manual':
                y[0] += 1
            else:
                if res['lessonDifficulty'] == 2:
                    y[1] += 1
                elif res['lessonDifficulty'] == 3:
                    y[2] += 1
                else:
                    y[3] += 1
    fig = plt.figure(figsize=(8, 6))
    plt.bar(x, y)
    plt.xticks(rotation=90)
    plt.ylabel('Кол-во просмотренного контента')
    plt.title('Количество просмотренного контента по Типам Уроков')
    plt.show()


def get_general_statistic(statistics):
    statistic_values = {
        'Average time in queue': 0,
        'Clients amount': 0,
        'Clients gone': 0,
    }

    for i in range(len(statistics)):
        if statistics[i]['watchedContent'] is True:
            statistic_values['Clients amount'] +=1
            statistic_values['Average time in queue'] += \
                    int(statistics[i]['studiedResources'][0]['ST'])
        else:
            statistic_values['Clients gone'] +=1
    statistic_values['Average time in queue'] /= statistic_values['Clients amount']
    statistic_values['Average time in queue'] = round(statistic_values['Average time in queue'], 3)
    return statistic_values


def time_in_queue(statistics):
    y_user = []
    x_user = []
    for i in range(len(statistics)):
        if statistics[i]['watchedContent'] is True:
            y_user.append(int(statistics[i]['studiedResources'][0]['ST']))
            x_user.append(i)

    fig, ax = plt.subplots()
    ax.scatter(x_user, y_user, c='b')

    ax.set_facecolor('white')  # цвет области Axes
    ax.set_title('Время в очереди')  # заголовок для Axes

    fig.set_figwidth(8)  # ширина и
    fig.set_figheight(8)
    plt.show()



if __name__ == '__main__':
    statistic_values = get_statistics()

    gen_stat = get_general_statistic(statistic_values)
    print(f'Среднее время в очереди: {gen_stat["Average time in queue"]}\n'
        f'Обслуженных клиентов: {gen_stat["Clients amount"]}\n'
        f'Ушедших клиентов: {gen_stat["Clients gone"]}\n'
    )

    time_in_queue(statistic_values)
    popular_lesson_types(statistic_values)
    popular_themes(statistic_values)