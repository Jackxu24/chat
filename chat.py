
def read_file(filename):
	lines = []
	with open(filename, 'r', encoding ='utf-8-sig') as f:
		for line in f:
			lines.append(line.strip())
	return lines #function execute 後return 翻出來for 後續運算

def convert(lines):
    new = []
    person = None
    for line in lines:
        if line == 'Allen':
            person = 'Allen'
            continue
        elif line == 'Tom':
            person = 'Tom'
            continue
        if person: #可以理解為person如果有value嘅話
            new.append(person + ': ' + line)
    return new

def write_file(filename, lines):
    with open(filename, 'w') as f:
        for line in lines:
            f.write(line + '\n')


def main():
    lines = read_file('input.txt')
    lines = convert(lines)
    write_file('output.txt', lines)
main() #programming execution point




