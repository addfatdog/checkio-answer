from datetime import date

# 2014-01-03 01:12:13 6009

def total_cost(bill_list):
  day_dict = {}
  sum_to_pay = 0

  for bill in bill_list:
    splited_data = bill.split(' ')
    call_time = (int(splited_data[2]) + 59) / 60

    year_month_day = splited_data[0].split('-')
    year, month, day = map(int, year_month_day)
    call_data = date(year, month, day)

    if call_data in day_dict:
      day_dict[call_data] = day_dict[call_data] + call_time
    else:
      day_dict[call_data] = call_time

  for everyday in day_dict:

    if day_dict[everyday] <= 100:
      sum_to_pay += day_dict[everyday]
    else:
      sum_to_pay += (100 + (day_dict[everyday] - 100)*2)

  return sum_to_pay


if __name__ == '__main__':
  #These "asserts" using only for self-checking and not necessary for auto-testing
  assert total_cost((u"2014-01-01 01:12:13 181",
                     u"2014-01-02 20:11:10 600",
                     u"2014-01-03 01:12:13 6009",
                     u"2014-01-03 12:13:55 200")) == 124, "Base example"
  assert total_cost((u"2014-02-05 01:00:00 1",
                     u"2014-02-05 02:00:00 1",
                     u"2014-02-05 03:00:00 1",
                     u"2014-02-05 04:00:00 1")) == 4, "Short calls but money..."
  assert total_cost((u"2014-02-05 01:00:00 60",
                     u"2014-02-05 02:00:00 60",
                     u"2014-02-05 03:00:00 60",
                     u"2014-02-05 04:00:00 6000")) == 106, "Precise calls"
