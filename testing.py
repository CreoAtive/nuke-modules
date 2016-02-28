import sys

class ChainElement(object):

    def __init__(self, type = '', value = None):
        object.__init__(self)

        self.type = type
        self.value = value

    def get(self):
        return self.value

class ChainValue(ChainElement):

    def __init__(self, value = None):
        ChainElement.__init__(self, 'value', value)

class ChainCondition(ChainElement):

    def __init__(self, condition = None):
        ChainElement.__init__(self, 'condition', condition)

class ChainThen(ChainElement):

    def __init__(self, then = None):
        ChainElement.__init__(self, 'then', then)

class Test(object):

    def __init__(self, name = ''):
        object.__init__(self)

        self._name = name
        self._chain = []

    def ensure(self, value):
        self._chain.append(ChainValue(value))

        return self

    def condition(self, method):
        self._chain.append(ChainCondition(method))

        return self

    def then(self, method):
        self._chain.append(ChainThen(method))

        return self

    def evaluate(self):
        print 'Start {test_name}'.format(test_name = self._name)

        value = None
        test_results = []
        conditions_count = len(filter(lambda x: isinstance(x, ChainCondition), self._chain))

        for index, chain_element in enumerate(self._chain):
            if index == 0:
                assert isinstance(chain_element, ChainValue)

            try:
                if isinstance(chain_element, ChainValue):
                    if hasattr(chain_element.get(), '__call__'):
                        value = chain_element.get()()
                    else:
                        value = chain_element.get()
                elif isinstance(chain_element, ChainCondition):
                    if value:
                        method = chain_element.get()

                        result = method(value)

                        test_results.append(result)
                elif isinstance(chain_element, ChainThen):
                    if value:
                        method = chain_element.get()

                        try:
                            result = method(value)
                        except Exception as e:
                            print e
                        else:
                            value = result
            except Exception as e:
                print e

        if len(test_results) == conditions_count and not False in test_results:
            print 'All conditions were met'
        else:
            print 'Conditions were not met'

        print 'Finished {test_name}'.format(test_name = self._name)
