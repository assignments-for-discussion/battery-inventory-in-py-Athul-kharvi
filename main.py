
def count_batteries_by_health(present_capacities):
  rated_capacity = 120  # All batteries are assumed to have the same rated capacity

   counts = {
        "healthy": 0,
        "exchange": 0,
        "failed": 0
    }

   # Classify batteries based on their SoH
    for capacity in present_capacities:
        # Ignore negative capacity as invalid data
        if capacity < 0:
            continue
        
        soh = (capacity / rated_capacity) * 100  # Calculate SoH percentage
        
        if soh > 80:
            counts["healthy"] += 1
        elif 62 <= soh <= 80:
            counts["exchange"] += 1
        elif soh < 62:
            counts["failed"] += 1

    return counts
    
  return {
    "healthy",
    "exchange": 0,
    "failed": 0
  }


def test_bucketing_by_health():
  print("Counting batteries by SoH...\n")
  present_capacities = [113, 116, 80, 95, 92, 70]
  counts = count_batteries_by_health(present_capacities)
  assert(counts["healthy"] == 2)
  assert(counts["exchange"] == 3)
  assert(counts["failed"] == 1)
  print("Done counting :)")


if __name__ == '__main__':
  test_bucketing_by_health()
