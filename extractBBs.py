import json

def main():
    with open("C:/Users/krish/Downloads/labeled_file_info.json", 'r') as f:
        data = json.load(f)
    names = [d["filename"] for d in data]
    locations = [d["latlon"] for d in data]
    lats = [loc[0] for loc in locations]
    longs = [longs[1] for longs in locations]
    longs = list(set(longs))
    lats = list(set(lats))
    coords = list(zip(lats, longs))
    print(len(coords))

    fileLists = []
    for lat in lats:
        fileNames = []
        for element in data:
            if lat in element["latlon"]:
                fileNames.append(element["filename"])
        fileLists.append(fileNames)
    total = 0
    for fileNames in fileLists:
        total += len(fileNames)
    print(total)

if __name__ == "__main__":
   main()


