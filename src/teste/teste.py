import signal
import time
import os
import sys


def import_pydevd(loader_path, port, suspend=False):
    # type: (str, int, bool) -> None
    if "DEBUG" in os.environ:
        dir_path = os.path.dirname(os.path.realpath(loader_path))
        filename = os.path.join(dir_path, "debug.txt")

        if os.path.isfile(filename):
            with open(filename, "r") as debug_file:
                pydev_path = debug_file.readline()
            pydev_path = pydev_path.replace('\n', '')

            if True or os.path.exists(pydev_path):

                try:
                    sys.path.index(pydev_path)
                except:
                    sys.path.append(pydev_path)
                print(sys.path)

                import pydevd
                pydevd.settrace('localhost', port=port, stdoutToServer=True, stderrToServer=True, suspend=suspend)

def signal_handler(signum, frame):
    print('Vou desligar em')
    signal.signal(signal.SIGTERM, signal.SIG_DFL)
    os.killpg(0, signal.SIGTERM)

def main():
    import_pydevd("/home/george/projects/fleet-control-device/data/server/bundles/teste/debug.txt", 9135, False)

    signal.signal(signal.SIGTERM, signal_handler)
    count = 0
    while True:
        count = count + 1
        print(str(count) + ". This prints once every 5secs.")

        time.sleep(10)


if __name__ == '__main__':
    main()
