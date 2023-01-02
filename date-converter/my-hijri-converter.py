import datetime
from bisect import bisect
import helpers


class Hijri:

    def __init__(self, year, month, day, validate=True):

        self._year = year
        self._month = month
        self._day = day

        if validate:
            pass

    @property
    def year(self):
        return self._year

    @property
    def month(self):
        return self._month

    @property
    def day(self):
        return self._day

    # Total Hijri months elapsed before the beginning of Hijri range.
    HIJRI_OFFSET = 1342 * 12

    # called when print() or str() function is invoked on an object
    def __str__(self):
        return self.isoformat()

    def isoformat(self):
        """Return date in ISO format i.e. ``YYYY-MM-DD``."""
        return f"{self._year:04}-{self._month:02}-{self._day:02}"

    def _month_index(self):
        prior_months = ((self.year - 1) * 12) + self.month - 1
        index = prior_months - self.HIJRI_OFFSET
        return index

    def to_julian(self):

        month_starts = helpers.MONTH_STARTS
        index = self._month_index()
        rjd = month_starts[index] + self._day - 1  # Reduced Julian Day (RJD)
        jdn = helpers.rjd_to_jdn(rjd)

        return jdn

    def to_gregorian(self):
        # Julian day number (JDN)
        jdn = self.to_julian()

        # January 1 of year 1 has ordinal number 1 - (DON) date original number
        don = helpers.jdn_to_ordinal(jdn)

        # fromordinal() => return the Gregorian date corresponding to a specified Gregorian ordinal
        return Gregorian.fromordinal(don)


class Gregorian(datetime.date):

    # Total Hijri months elapsed before the beginning of Hijri range.
    HIJRI_OFFSET = 1342 * 12

    def to_julian(self):
        # January 1 of year 1 has ordinal number 1 - (DON) date original number
        don = self.toordinal()
        # Julian day number (JDN)
        jdn = helpers.ordinal_to_jdn(don)
        return jdn

    def to_hijri(self):
        jdn = self.to_julian()

        rjd = helpers.jdn_to_rjd(jdn)  # Reduced Julian Day (RJD)

        # Bisect algorithm is to find a position in list where an element needs to be inserted to keep the list sorted.
        index = bisect(helpers.MONTH_STARTS, rjd) - 1

        months = index + self.HIJRI_OFFSET
        years = int(months / 12)
        year = years + 1
        month = months - (years * 12) + 1
        day = rjd - helpers.MONTH_STARTS[index] + 1

        return Hijri(year, month, day, validate=False)


# gregorian_date = Gregorian(2022, 12, 31)
# print(gregorian_date.to_hijri())


# hijri_date = Hijri(1444, 6, 7)
# print(hijri_date.to_gregorian())
