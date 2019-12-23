import pickle
import matplotlib.pyplot as plt


def get_statistics():
    with open('sim.pickle', 'rb') as reader:
        data = pickle.load(reader)
    return data


def get_general_statistic(statistics):
    statistic_values = {
        'Average time in queue': 0,
        'Clients amount': 0,
        'Clients gone': 0
    }

    for i in range(len(statistics)):
        if statistics[i]['watchedContent'] is True:
            statistic_values['Clients amount'] +=1
            statistic_values['Average time in queue'] += \
                    int(statistics[i]['studiedResources'][0]['ST'] - \
                    statistics[i]['wentToPortal'])
        else:
            statistic_values['Clients gone'] +=1
    statistic_values['Average time in queue'] //= statistic_values['Clients amount']
    return statistic_values


def time_in_queue(statistics):
    y_user = []
    x_user = []
    for i in range(len(statistics)):
        if statistics[i]['watchedContent'] is True:
            y_user.append(int(statistics[i]['studiedResources'][0]['ST'] - statistics[i]['wentToPortal']))
            x_user.append(i)

    fig, ax = plt.subplots()
    ax.scatter(x_user, y_user, c='b')

    ax.set_facecolor('white')  # цвет области Axes
    ax.set_title('Time in queue')  # заголовок для Axes

    fig.set_figwidth(8)  # ширина и
    fig.set_figheight(8)
    plt.show()



if __name__ == '__main__':
    statistic_values = get_statistics()

    gen_stat = get_general_statistic(statistic_values)
    print(f'Average time in queue: {gen_stat["Average time in queue"]}\n'
        f'Clients amount: {gen_stat["Clients amount"]}\n'
        f'Clients gone: {gen_stat["Clients gone"]}\n'
    )

    time_in_queue(statistic_values)