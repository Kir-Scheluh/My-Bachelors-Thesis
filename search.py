from search_engines import Yahoo  # Работает
from search_engines import Startpage  # Работает
from search_engines import Ask  # Работает
from filter_search_results import filter_results


def general_search(query):
    result = {'Yahoo': filter_results(search_with_yahoo(str(query))),
              'Startpage': filter_results(search_with_startpage(str(query))),
              'Ask': filter_results(search_with_Ask(str(query)))}

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


print(general_search('Влад бумага ютуб'))
