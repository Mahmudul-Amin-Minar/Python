list_ = list(map(int, input().split()))

list_.sort(reverse = True)
print(list_)

def list_sorting_by_len(list_):

    def len_func(l):
        return len(l)
    
    list_.sort(reverse = True, key=len_func)
    print(list_)

list_sorting_by_len(['Ford', 'Mitsubishi', 'BMW', 'VW'])