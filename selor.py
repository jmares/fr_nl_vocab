import math 
wordpairs_per_page = 25
first_page = None
prev_page = None
next_page = None
last_page = None
src_file = "data/French-Dutch-SELOR-8000-words.txt"
html_template = "templates/selor.html"
navbar_template = "templates/navbar.html"
output_dir = "www/"
output_filename = "selor"
output_filetype = "html"





def main():

    # read file and add wordpairs to a list
    f = open(src_file, "r")
    content = f.readlines()
    wordpairs = []
    count = 0
    for line in content:
        try:
            count += 1
            arr = line.rstrip().split("\t")
            fr = arr[0].strip(' "')
            nl = arr[1].strip(' "')
            wordpairs.append((fr, nl))
        except Exception as err:
            print("\n", line)
            print("Error:", err)
    f.close()
    #print(wordpairs[:25])

    page_number = 0
    first_page = f"{output_filename}1.{output_filetype}"
    number_of_pages = math.ceil(len(wordpairs)/wordpairs_per_page)
    last_page = f"{output_filename}{number_of_pages}.{output_filetype}"

    while len(wordpairs) > 0:
        lijst = wordpairs[:wordpairs_per_page]
        page_number += 1

        t = open(html_template, "r")
        contents = t.read()
        t.close()
        table = ""
        for (fr, nl) in lijst:
            table += f"\t\t\t<tr>\n\t\t\t\t<td class='frans'>{fr}</td>\n\t\t\t\t<td class='nederlands'>{nl}</td>\n\t\t\t</tr>\n"

        t = open(navbar_template, "r")
        navbar = t.read()
        t.close()

        prev_page = f"{output_filename}{page_number-1}.{output_filetype}"
        next_page = f"{output_filename}{page_number+1}.{output_filetype}"
        navbar = navbar.replace('<!-- insert_pagenumber -->', str(page_number))
        navbar = navbar.replace('<!-- insert_firstpage -->', first_page)
        navbar = navbar.replace('<!-- insert_lastpage -->', last_page)
        navbar = navbar.replace('<!-- insert_prevpage -->', prev_page)
        navbar = navbar.replace('<!-- insert_nextpage -->', next_page)
        
        contents = contents.replace('<!-- insert_data -->', table)
        contents = contents.replace('<!-- insert_navbar -->', navbar)
        
        output_file = f"{output_dir}{output_filename}{page_number}.{output_filetype}"
        print(output_file)

        o = open(output_file, "w")
        o.write(contents)
        o.close()

        del wordpairs[:wordpairs_per_page]




    

if __name__ == '__main__':
    main()