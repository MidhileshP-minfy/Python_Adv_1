def generate_summary(data, group_by):
    """Generate a summary by grouping data."""
    summary = {}
    for item in data:
        if group_by not in item:
            continue

        group = item[group_by]
        if group not in summary:
            summary[group] = 0
        summary[group] += 1

    return summary