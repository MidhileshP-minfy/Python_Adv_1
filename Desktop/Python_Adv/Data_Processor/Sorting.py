def filter_data(data, criteria):
    """Filter data based on criteria dictionary."""
    result = []
    for item in data:
        matches = True
        for key, value in criteria.items():
            if key not in item or item[key] != value:
                matches = False
                break
        if matches:
            result.append(item)
    return result

def sort_data(data, key, reverse=False):
    """Sort data by a specific key."""
    return sorted(data, key=lambda x: x.get(key, ''), reverse=reverse)
