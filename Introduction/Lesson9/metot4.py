def decorator_metot(metot):
    def sarmal_metot():
        print("sarmal metot çalıştı! {}'metodundan önce".format(metot.__name__))
        return metot()
    return sarmal_metot


@decorator_metot
def printer_metot():
    print("Printer metodu çalıştı!")


printer_metot()