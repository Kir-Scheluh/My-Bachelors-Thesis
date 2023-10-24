import termplotlib as tpl


def horizontal_histogram(data, names):
    fig = tpl.figure()
    fig.barh(data, names, force_ascii=False)
    fig.show()
