from datetime import date
# ...r = returned | ...e = expected
dayr, monthr, yearr = map(int, input().split())
daye, monthe, yeare = map(int, input().split())
returned_date = date(yearr, monthr, dayr)
expected_date = date(yeare, monthe, daye)
diff = returned_date - expected_date
print(diff)
if yearr > yeare:
    fine = 10000
elif yearr < yearr:
    fine = 0
elif monthr > monthe:
    fine = 500 * (monthr - monthe)
elif dayr > daye:
    fine = 15 * (dayr - daye)
else:
    fine = 0

print(fine)
