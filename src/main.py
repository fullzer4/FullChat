import argparse

def parse_arguments():
    parser = argparse.ArgumentParser(description=
        "My CLI Tool for manage notes in obsidian and synk with github"
    )
    parser.add_argument("-f", "--folder", help="Path to the folder valut")

    return parser.parse_args()

def main():
    args = parse_arguments()

if __name__ == "__main__":
    main()

