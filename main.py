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
        
        soh = round((capacity / rated_capacity) * 100, 2)  # Calculate SoH percentage
        
        if soh >= 80:
            counts["healthy"] += 1
        elif 62 <= soh < 80:
            counts["exchange"] += 1
        elif soh < 62:
            counts["failed"] += 1

    return counts

# Test cases to verify the correct classification of battery health
def test_bucketing_by_health():
    print("Testing battery classification by SoH...\n")

    # Example test case from the problem
    present_capacities = [113, 116, 80, 95, 92, 70]
    counts = count_batteries_by_health(present_capacities)
    assert counts["healthy"] == 2
    assert counts["exchange"] == 3
    assert counts["failed"] == 1
    print("Test case 1 passed.")

    # Boundary test case: SoH exactly at the boundary of healthy
    present_capacities = [120, 96, 72]  # 100%, 80%, 60% SoH
    counts = count_batteries_by_health(present_capacities)
    assert counts["healthy"] == 2  # 100% and 80% should be healthy
    assert counts["exchange"] == 0
    assert counts["failed"] == 1  # 60% should be failed
    print("Test case 2 passed.")

    # Edge case: Present capacity less than 0 (should be ignored)
    present_capacities = [-10, 120, 90]  # One invalid, two valid capacities
    counts = count_batteries_by_health(present_capacities)
    assert counts["healthy"] == 1 
    assert counts["exchange"] == 1
    assert counts["failed"] == 0
    print("Test case 3 passed.")

    # All batteries failed
    present_capacities = [50, 60, 70]  # All below 62%
    counts = count_batteries_by_health(present_capacities)
    assert counts["healthy"] == 0
    assert counts["exchange"] == 0
    assert counts["failed"] == 3
    print("Test case 4 passed.")

    # Empty list 
    present_capacities = []
    counts = count_batteries_by_health(present_capacities)
    assert counts["healthy"] == 0
    assert counts["exchange"] == 0
    assert counts["failed"] == 0
    print("Test case 5 passed.")

    # All batteries exactly on the edge of 'exchange'
    present_capacities = [74.4, 74.4, 74.4]  # 62% SoH for all
    counts = count_batteries_by_health(present_capacities)
    assert counts["healthy"] == 0
    assert counts["exchange"] == 3  # All batteries are exactly at 62%
    assert counts["failed"] == 0
    print("Test case 6 passed.")

    # Mix of the valid and invalid values 
    present_capacities = [-5, -10, 115, 90, 60]  # Two invalid, three valid
    counts = count_batteries_by_health(present_capacities)
    assert counts["healthy"] == 1  # 115% SoH
    assert counts["exchange"] == 1 # 90% SoH
    assert counts["failed"] == 1  # 60% failed
    print("Test case 7 passed.")

    # Boundary test case: Boundary just below exchange and just above failed
    present_capacities = [74.8, 74.4]  # SoH close to exchange/failure boundary
    counts = count_batteries_by_health(present_capacities)
    assert counts["healthy"] == 0  # No healthy batteries
    assert counts["exchange"] == 2  # Both batteries are in exchange range
    assert counts["failed"] == 0    # None are failed
    print("Test case 8 passed.")


    # A wide range of batteries, including edge cases, negative values, and extreme values
    present_capacities = [-20, 60, 72, 80, 81, 100, 110, 125, 130, 0, 50, 90]
    counts = count_batteries_by_health(present_capacities)
    assert counts["healthy"] == 4  # 100, 110, 125, 130
    assert counts["exchange"] == 3  # 80, 81, 90
    assert counts["failed"] == 4    # 60, 72, 0, 50
    print("Test case 9 passed.")




if __name__ == '__main__':
    test_bucketing_by_health()
