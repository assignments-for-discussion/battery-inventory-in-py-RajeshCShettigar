def count_batteries_by_health(present_capacities):
    SoH=[]
    #SoH list maintain the SoH value of each battery
    healthy_battery_count=0
    exchange_battery_count=0
    failed_battery_count=0

    #counting of batteries in each category
    for battery in present_capacities:
        curr_battery_SoH=(battery/120)*100
        SoH.append(curr_battery_SoH)
        if(curr_battery_SoH>=80):
            healthy_battery_count+=1
        elif(curr_battery_SoH>=60 and curr_battery_SoH<80):
            exchange_battery_count+=1
        else:
            failed_battery_count+=1

    #return the count of batteries in each category
    return {
       "healthy":healthy_battery_count,
       "exchange":exchange_battery_count,
       "failed":failed_battery_count
       }


def test_bucketing_by_health():
  print("Counting batteries by SoH...\n")
  present_capacities = [113, 116, 80, 95, 92, 70]
  counts = count_batteries_by_health(present_capacities)
  assert(counts["healthy"] == 2)
  assert(counts["exchange"] == 3)
  assert(counts["failed"] == 1)
  print(counts)
  print("Done counting :)")

if __name__ == '__main__':
  test_bucketing_by_health()
