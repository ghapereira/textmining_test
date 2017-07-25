import re

def main():
    base_file_name = 'data/shake_copy.txt'
    with open(base_file_name, 'r') as fp:
        split_file(fp)


def split_file(fp):
    line_buffer = []

    line_n_minus_1 = ''
    line_n_minus_2 = ''
    subfile_name = ''


    for line in fp:
        # Inner texts have 'by William Shakespeare' as prefix
        match_obj = re.match('by William Shakespeare', line)

        if match_obj:
            # Write previous file
            write_file_buffer(subfile_name, line_buffer)
            line_buffer = []

            next_line = '\n'

            # Find next line containing a text
            while next_line == '\n':
                next_line = fp.readline()

            subfile_name = line_n_minus_2.replace(' ', '_')
            subfile_name = subfile_name.strip('\n')
            print('Reading text "{}"'.format(subfile_name))

        else:
            line_buffer.append(line)

        line_n_minus_2 = line_n_minus_1
        line_n_minus_1 = line

def write_file_buffer(subfile_name, line_buffer):
    with open('data/works/{}.txt'.format(subfile_name), 'w+') as fp:
        [fp.write(line) for line in line_buffer]


if __name__ == '__main__':
    main()
