import difflib
import csv


def preprocess_name(name):
    """Pre-process school names by replacing exact matches of certain terms."""
    name_parts = name.split()
    replacements = {
        "dr": "doutor",
        "dr.": "doutor",
        "drº": "doutor",
        "dra": "doutora",
        "dra.": "doutora",
        "drª": "doutora",
        "eb": "escola básica",
        "e.b.": "escola básica",
        "e. b.": "escola básica",
        "s.": "são",
        "2,3": "2/3",
        "eb1": "escola básica 1",
        # Add more exact match replacements if needed
    }
    processed_parts = [replacements.get(part, part) for part in name_parts]
    return " ".join(processed_parts)


def normalize_name(name):
    """Normalize school name by converting to lowercase."""
    name = name.lower()
    return name


def group_school_names(school_names):
    """Group similar school names, avoiding duplicates."""
    normalized_names = [normalize_name(name) for name in school_names]
    preprocessed_names = [preprocess_name(name) for name in normalized_names]

    # Remove exact duplicates after preprocessing
    unique_preprocessed_names = list(set(preprocessed_names))

    grouped = {}

    for name in unique_preprocessed_names:
        found = False
        for key in grouped.keys():
            if difflib.SequenceMatcher(None, name, key).ratio() > 0.8:
                grouped[key].append(name)
                found = True
                break
        if not found:
            grouped[name] = [name]

    return grouped


def save_to_csv(grouped_names, filename="grouped_schools.csv"):
    """Save grouped names to a CSV file."""
    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow(["Reference Name", "Similar Names"])
        for key, group in grouped_names.items():
            # Remove the representative name from the group
            filtered_group = [name for name in group if name != key]
            similar_names = str(sorted(filtered_group)) if filtered_group else ""
            csv_writer.writerow([key, similar_names])


def read_school_names(filename):
    """Read school names from a file."""
    with open(filename, "r") as file:
        return file.read().splitlines()


# Example usage
filename = "school_names.txt"  # Replace with your file name
school_names = read_school_names(filename)

grouped_names = group_school_names(school_names)
save_to_csv(grouped_names)
