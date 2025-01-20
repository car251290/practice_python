def breakingRecords(scores):
    # Write your code here
    # Initialize min_score and max_score to the first score
    min_score = scores[0]
    # Initialize min_count and max_count to 0
    max_score = scores[0]
    # Initialize min_count and max_count to 0
    min_count = 0
    max_count = 0
    # Loop through the scores
    for score in scores:
        if score < min_score:
            min_score = score
            min_count += 1
        if score > max_score:
            max_score = score
            max_count += 1
    return [max_count, min_count]
    
    
    
    