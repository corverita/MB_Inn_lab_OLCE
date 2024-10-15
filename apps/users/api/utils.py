class QuerysetSorter:
    @staticmethod
    def bubble_sort(queryset, attr, ascendant=False):
        ascendant = True if ascendant == 'true' else False
        
        queryset = list(queryset)
        n = len(queryset)
        for i in range(n):
            for j in range(0, n-i-1):
                if ascendant:
                    if getattr(queryset[j], attr) > getattr(queryset[j+1], attr):
                        queryset[j], queryset[j+1] = queryset[j+1], queryset[j]
                else:
                    if getattr(queryset[j], attr) < getattr(queryset[j+1], attr):
                        queryset[j], queryset[j+1] = queryset[j+1], queryset[j]
        return queryset