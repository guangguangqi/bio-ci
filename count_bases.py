# count_bases.py
def calculate_gc(sequence):
    sequence = sequence.upper()
    g_count = sequence.count('G')
    c_count = sequence.count('C')
    total = len(sequence)
    if total == 0:
        return 0
    return (g_count + c_count) / total * 100

# Simple test to make sure it works
if __name__ == "__main__":
    test_seq = "ATGCATGC"
    result = calculate_gc(test_seq)
    print(f"Testing sequence: {test_seq}")
    print(f"GC Content: {result}%")
    
    # Assert ensures the code gives the correct scientific answer
    assert result == 50.0, "Error: GC calculation is wrong!"
    print("All tests passed successfully!")
    print("check check")  
