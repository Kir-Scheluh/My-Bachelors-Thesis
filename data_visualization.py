import termplotlib as tpl


def horizontal_histogram(data, names):
    fig = tpl.figure()
    fig.barh(data, names, force_ascii=False)
    fig.show()


horizontal_histogram([15, 23, 8], ["Yahoo", "Ask", "Startpage"])
