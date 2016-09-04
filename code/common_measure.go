package main

import "fmt"
import "regexp"

const (
    a = '^[m|M]'
    b = 'or'
    c = 'y$'
    d = '^[m|M]'
)

func main() {
    lines_seen := make(map[string]bool)
    
set := make(map[int]bool)
def common_measure():
    lines_seen = set()
    f1 = open('source.txt')
    with open('../common_measure/cm' + '_' + a + '_' + b + '_' + c + '_' + d + '.txt', 'w') as f2:
        f2.write('\n' + '[' + a + ', ' + b + ', ' + c + ', ' + d + ']\n\n')
        while True:
            for ending in [a, b, c, d]:
                for line in f1:
                    if re.search(ending, line) is not None and len(line) < 100:
                        if line not in lines_seen:
                            f2.write(line)
                            lines_seen.add(line)
                            break
                else:
                    return
            f2.write('\n')

common_measure()
