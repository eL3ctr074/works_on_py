import codesarr
import logpars


def ex1(file):
    count1 = 0
    count2 = 0
    count3 = 0
    for index in file.statusarr:
        code2 = codesarr.x2
        code4 = codesarr.x4
        code5 = codesarr.x5
        for elem in code2:
            if index == elem:
                count1 += 1
        for elem in code4:
            if index == elem:
                count2 += 1
        for elem in code5:
            if elem == index:
                count3 += 1
    print('Колличество запросов с кодами 20х: ', count1)
    print('Колличество запросов с кодами 40х: ', count2)
    print('Колличество запросов с кодами 50х: ', count3)


if __name__ == "__main__":
    test = logpars.Pars()
    filenam = "log.txt"

    test.initfile(filenam)

    # print(test.timefinder('20:34'))
    # print(test.sourcearr)

    # ex1(test)

    # test.urlfind()

    print(test.timebytime())

    # print('Список URL c кодом 500', test.urlfind('500'))
