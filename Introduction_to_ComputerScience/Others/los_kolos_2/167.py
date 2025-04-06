def main(word):
    def fun(w, i, flag):
        leng = len(w)
        g = ['a', 'e', 'i', 'o', 'u', 'y']
        if w[i] in g:
            if flag:
                return 0
            else:
                flag = True

        if leng - 1 == i:
            if flag:
                return 1
            else:
                return 0

        if flag:
            return fun(w, i + 1, True) + fun(w, i + 1, False)
        else:
            return fun(w, i + 1, False)


    # end def

    return fun( word, 0 , False )

# end def

print( main("alicja") )
