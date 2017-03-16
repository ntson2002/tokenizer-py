from subprocess import call, check_call

from subprocess import *

def jarWrapper(*args):
    process = Popen(['java', '-jar']+list(args), stdout=PIPE, stderr=PIPE)
    ret = []
    while process.poll() is None:
        line = process.stdout.readline()
        if line != '' and line.endswith('\n'):
            ret.append(line[:-1])
    stdout, stderr = process.communicate()
    ret += stdout.split('\n')
    if stderr != '':
        ret += stderr.split('\n')
    ret.remove('')
    return ret

def tokenize_vn(path_in, path_out):
    args = ['vn.hus.nlp.tokenizer-4.1.1.jar', '-i', path_in, '-o', path_out]  # Any number of args to be passed to the jar file
    result = jarWrapper(*args)
    print '\n'.join(result)


if __name__ == '__main__':
    i = "a.txt"
    o = "b.txt"
    tokenize_vn(i, o)

