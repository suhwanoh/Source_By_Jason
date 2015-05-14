def drop_first_last(grades):
    first, *middle, last = grades

#   * means include all parts except first, last. doesn't matter how many  you have

    avg = sum(middle)/len(middle)
    print(avg)



drop_first_last([10,50,20,40,40,59,39,20])
drop_first_last([59,48,59,60,90,90,10,49,85,49])
drop_first_last([10,20,30,40,50])