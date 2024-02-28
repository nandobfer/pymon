import psutil, time, os

black_list = ['MicrosoftHost.exe', 'taskhost.exe']

while True:
    processes = sorted(psutil.process_iter(['pid', 'name', 'cpu_percent']), key=lambda d: d.info['cpu_percent'], reverse=True)
    os.system('cls')
    for process in processes:
        if process.info['cpu_percent'] > 0:
            print(process.info)

        for unwanted in black_list:
            if process.info['name'] == unwanted:
                print()
                try:
                    cpu_percent = process.info['cpu_percent']
                    process.terminate()
                    print(f'killed {process.info["name"]}, cpu_percent: {cpu_percent}')
                except:
                    print(f'couldnt terminate {process.info}')
                    pass

    time.sleep(10)

