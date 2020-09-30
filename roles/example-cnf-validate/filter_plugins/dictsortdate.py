#!/usr/bin/python
class FilterModule(object):
    def filters(self):
        return {
            'dictsortdate': self.dictsortdate,
        }

    def dictsortdate(self, list_to_sort):
        return sorted(list_to_sort, key=lambda x: x['eventTime'])
