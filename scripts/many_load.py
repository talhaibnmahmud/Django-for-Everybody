import csv

from unesco.models import Category, States, Region, Iso, Site


def run():
    fhand = open('unesco/whc-sites-2018-clean.csv')
    reader = csv.reader(fhand)
    next(reader)

    Category.objects.all().delete()
    States.objects.all().delete()
    Region.objects.all().delete()
    Iso.objects.all().delete()
    Site.objects.all().delete()

    for row in reader:
        print(row)

        c, created = Category.objects.get_or_create(name=row[7])
        s, created = States.objects.get_or_create(name=row[8])
        r, created = Region.objects.get_or_create(name=row[9])
        i, created = Iso.objects.get_or_create(name=row[10])

        try:
            y = int(row[3])
        except:
            y = None

        try:
            long = float(row[4])
        except:
            long = None

        try:
            lat = float(row[5])
        except:
            lat = None

        try:
            area = float(row[6])
        except:
            area = None

        site = Site(
            name=row[0],
            description=row[1],
            justification=row[2],
            year=y,
            longitude=long,
            latitude=lat,
            area_hectares=area,

            category=c,
            states=s,
            region=r,
            iso=i
        )

        site.save()
