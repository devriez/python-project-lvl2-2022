import argparse


def main():
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first_file_path', type=str)
    parser.add_argument('second_file_path', type=str)
    parser.add_argument(
        '-f', '--format',
        type=str,
        # default=2,
        help='set format of output'
    )
    args = parser.parse_args()
    print(args.first_file, args.second_file)


if __name__ == '__main__':
    main()
