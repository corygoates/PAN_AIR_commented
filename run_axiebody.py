import os
import glob
import subprocess as sp

def remove(filename):
    try:
        os.remove(filename)
    except FileNotFoundError:
        pass

if __name__=="__main__":

    # Clear old files
    for filename in glob.glob('f*'):
        remove(filename)
    for filename in glob.glob('rw*'):
        remove(filename)
    for filename in glob.glob('n*'):
        remove(filename)
    remove('agps')
    remove('panair.err')
    remove('panair.out')

    # Run
    with sp.Popen(['./a.out'], stdin=sp.PIPE, stdout=sp.PIPE) as pan_air_process:
        pan_air_process.communicate('axiebody.INP'.encode('utf-8'))