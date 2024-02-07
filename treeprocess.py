# Borrowed code from Jeff

import csv


def passes_filter(row, top_four_genus):
    # Filter criteria:
    #   Only listed trees that have full species name supplied

    # if len(row['qSpecies']) < 3 or 'Tree(s) ::' in row['qSpecies']:
    #     return False
    # #   Only trees that have a lat and lng provided
    # elif len(row['Latitude']) < 2 or len(row['Longitude']) < 2:
    #     return False
    # #   Only trees with valid SiteInfo
    # elif len(row['qSiteInfo']) < 1 or row['qSiteInfo'] == ':':
    #     return False
    # #   Only trees that have a DBH provided
    # elif len(row['DBH']) < 1:
    #     return False
    # else:
    #     return True

    # Filter criteria:
    # Only trees that are one of the four top most common genus in the dataset with dates

    name = row["qSpecies"].split()
    # width = row["PlotSize"].split()
    genus = name[0]
    if (
        genus in top_four_genus
        and row["PlantDate"] != ""
        # and row["PlotSize"] != ""
        # and width[0] != "Width"
        # and len(width[0]) == 3
        # and width[0][0] == width[0][2]
    ):
        return True
    else:
        return False

    # think about what other filters you could run here...


# import and run passes_filter
data = []
header = []
with open("./Street_Tree_List-2022-01-30_FILTERED.csv", "r") as f:
    reader = csv.DictReader(f)

    genus_dic = {}
    header = reader.fieldnames

    for row in reader:
        name = row["qSpecies"].split()
        genus = name[0]
        if genus not in genus_dic:
            genus_dic[genus] = 1
        else:
            genus_dic[genus] += 1

    sorted_genus = sorted(genus_dic.items(), key=lambda x: x[1], reverse=True)
    top_four_genus_dic = sorted_genus[:4]
    # extracting key
    top_four_genus = [kvpair[0] for kvpair in top_four_genus_dic]
    print(top_four_genus)

    # Reset file pointer to the beginning of the file
    f.seek(0)

    for row in reader:
        if passes_filter(row, top_four_genus):
            # you might consider doing some additional processing here
            # e.g. splitting up qSpecies
            data.append(row)

print(len(data))

# export to new CSV
with open("Street_Tree_Filtered.csv", "w") as f:
    writer = csv.DictWriter(f, fieldnames=header)
    writer.writeheader()
    writer.writerows(data)
