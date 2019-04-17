"""
Counting Valleys:
Based on a list of inputs denoteding a +1 or -1 in elevation, count how many valleys exist in a path
"""

def counting_valleys(path: list) -> int:
    """
    Valleys are counted  not by the total cahnge in elevation but, whenever the elevation count is
    coming back up from negative to zero, we know that we have an exited valley
    Params: path - A list of letters 'D' or 'U' that denotes descending or ascending a valley
    Returns: valley_count a count of defined  "valleys"
    """
    valley_count = 0 # Sentinel for counting the number of valleys
    elevation = 0 # Tracks the elevation
    for change in path: # We loop over the list in order to find the path
        if change == "D": # if we are desceding into a valley
            elevation -= 1
        else: # if we are ascending
            elevation += 1
            if elevation == 0: # if weve reached sea-level by asceding we know we've ended a valley
                valley_count += 1
                
    return valley_count
        

if __name__ == "__main__":
    print(counting_valleys(['D','D','U','U','U','U','D','D']))