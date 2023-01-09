import sys
import markdown


def main():
    argv_count = len(sys.argv)
    command = sys.argv[1]
    inputfile = sys.argv[2]
    outputfile = sys.argv[3]

    if command == "markdown":
        if argv_count != 4:
            print("入力に間違いがあります")
            sys.exit()
        try:
            with open(inputfile, "r") as f:
                text = f.read()
            md = markdown.Markdown(extentions=["extra", "toc", "sane_lists", "codehilite"])
            html = md.convert(text)
            with open(outputfile, "w") as f:
                f.write(html)
        except FileNotFoundError as e:
            print(f"{inputfile} not found.")
    else:
        print("正しいコマンドを入力してください")




if __name__ == "__main__":
    main()