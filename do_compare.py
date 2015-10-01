import sys
import os
from subprocess import Popen, PIPE, STDOUT

RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
LIGHT_PURPLE = '\033[94m'
PURPLE = '\033[95m'
END = '\033[0m'

if __name__ == '__main__':
    try:
        src_dir = sys.argv[1]
        new_dir = sys.argv[2]
    except IndexError:
        print "Usage: python do_compare.py src_dir new_idr"
        sys.exit(0)
    diff_dir = 'changes'
    for root, dirs, files in os.walk('.'):
        if src_dir in root:
            for f in files:
                if f.endswith('png'):
                    print "%(purple)sCompare%(end)s %(red)s%(file_name)s%(end)s\n" % {'purple': PURPLE, 'end': END, 'file_name': f, 'red': RED}
                    src_f = "%s/%s" % (src_dir, f)
                    new_f = "%s/%s" % (new_dir, f)
                    diff_f = "%s/%s" % (diff_dir, f)
                    # print src_f, new_f, diff_f
                    proccess = Popen(["compare", "-extract", "1024x768", "-verbose", "-metric", "PAE", src_f, new_f, diff_f], stdout=PIPE, stderr=STDOUT, close_fds=True)
                    stdoutdata, stderrdata = proccess.communicate()
                    print stdoutdata
                    proccess.stdout.close()
                    print "----------------------------\n"


                    

