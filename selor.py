def main():
    src_file = "data/French-Dutch-SELOR-8000-words.txt"
    template = "templates/selor.html"
    output = "www/selor.html"

    f = open(src_file, "r")
    content = f.readlines()
    lijst = []
    count = 0
    for line in content:
        if len(lijst) >= 25: break
        try:
            count += 1
            arr = line.rstrip().split("\t")
            fr = arr[0].strip(' "')
            nl = arr[1].strip(' "')
            lijst.append((fr, nl))
        except Exception as err:
            print("\n", count, line)
            print("Error:", err)
    f.close()

    t = open(template, "r")
    contents = t.read()
    t.close()

    table = ""
    for (fr, nl) in lijst:
        table += f"\t\t\t<tr>\n\t\t\t\t<td class='frans'>{fr}</td>\n\t\t\t\t<td class='nederlands'>{nl}</td>\n\t\t\t</tr>\n"

    contents = contents.replace('<!-- insert_data -->', table)

    o = open(output, "w")
    o.write(contents)
    o.close()
    

if __name__ == '__main__':
    main()