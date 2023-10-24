from search_engines import Yahoo  # Работает
from search_engines import Startpage  # Работает
from search_engines import Ask  # Работает
from filter_search_results import filter_results
from data_visualization import horizontal_histogram


def general_search(query):
    result = {'Yahoo': filter_results(search_with_yahoo(str(query))),
              'Startpage': filter_results(search_with_startpage(str(query))),
              'Ask': filter_results(search_with_Ask(str(query)))}
    names = list(result.keys())
    data = []
    for i in result.values():
        data.append(len(i["hosts"]))
    horizontal_histogram(data, names)

    return result


def search_with_yahoo(query):
    engine = Yahoo()
    search_result = engine.search(str(query))
    output = {'hosts': search_result.hosts(), 'titles': search_result.titles(), 'links': search_result.links()}

    return output


def search_with_startpage(query):
    engine = Startpage()
    search_result = engine.search(str(query))
    output = {'hosts': search_result.hosts(), 'titles': search_result.titles(), 'links': search_result.links()}
    return output


def search_with_Ask(query):
    engine = Ask()
    search_result = engine.search(str(query))
    output = {'hosts': search_result.hosts(), 'titles': search_result.titles(), 'links': search_result.links()}
    return output


general_search('Влад бумага ютуб')
