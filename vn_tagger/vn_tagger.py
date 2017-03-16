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

def tag_vn(path_in, path_out):
    """
    nguyenlabs-MacBook-Air-6:vn_tagger sonnguyen$ java -jar vn.hus.nlp.tagger-4.2.0.jar
    usage: VietnameseMaxentTagger
     -i <arg>   Input filename
     -o <arg>   Output filename
     -p         Use plain text format for saving tagging results.
     -t <arg>   Test filename
     -u         Use underscore character for separating syllables of words

    """
    args = ['vn.hus.nlp.tagger-4.2.0.jar', '-i', path_in, '-o', path_out]  # Any number of args to be passed to the jar file
    result = jarWrapper(*args)
    print '\n'.join(result)


if __name__ == '__main__':
    i = "input.txt"
    o = "output.txt"
    tag_vn(i, o)

