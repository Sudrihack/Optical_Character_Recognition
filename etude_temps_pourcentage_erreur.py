import xlwt
import time
import entrainement as tr

def xlwrite(values, times, kopti, pourcentages) :
    book, sheet1 = xlinit()
    i = 4
    for n in range(len(times) -1):
        i = i+1
        sheet1.write(i, 0, values[n])
        sheet1.write(i, 1, kopti[n])
        sheet1.write(i, 2, pourcentages[n])
        sheet1.write(i, 3, times[n])
    book.save("etude_comparative.xls")


def xlinit():
    book = xlwt.Workbook(encoding = "utf-8")

    sheet1 = book.add_sheet("Sheet 1")  

    sheet1.write(0, 0, "values")
    sheet1.write(0, 1, "k")
    sheet1.write(0, 2, "percentage error")
    sheet1.write(0, 3, "times")

    return book, sheet1

def main():
    values, times, kopti, pourcentages = [], [], [], []
    values = [20, 40, 80, 160, 320, 640, 1280, 2460, 4920, 9840, 20000, 40000, 50000]
    print(values)
    
    for i in values:
        print("for", i, "values ...")
        start_time = time.time()
        k, percent = tr.main(s = i)
        newtime =  time.time() - start_time
        
        kopti.append(k)
        times.append(newtime)
        pourcentages.append(percent)

        xlwrite(values, times, kopti, pourcentages)
    xlwrite(values, times, kopti, pourcentages)


if __name__ == '__main__':
    main()  