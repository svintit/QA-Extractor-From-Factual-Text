from subprocess import Popen


processes = []

for counter in range(1):
    chrome_cmd = 'export BROWSER=chrome && python3 src/tests/functional_tests/test_extractor.py'
    firefox_cmd = 'export BROWSER=firefox && python3 src/tests/functional_tests/test_extractor.py'
    processes.append(Popen(chrome_cmd, shell=True))
    processes.append(Popen(firefox_cmd, shell=True))

for counter in range(1):
    processes[counter].wait()
