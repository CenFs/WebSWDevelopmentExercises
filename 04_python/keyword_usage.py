def keyword_usage(stri, lst):
    strwords = stri.split()
    tu = ()
    for word in lst:
        flag = 0
        # print "word: " + word
        for strword in strwords:
            # print "strword: " + strword
            if (strword == word):
                tu += (True,)
                flag = 1
                break
        if (flag == 0):
            tu += (False,)
    return tu