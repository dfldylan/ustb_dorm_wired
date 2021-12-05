import serial
import time

# connect serial
ser = serial.Serial(port='COM3')
time.sleep(2)
ser.read_all()

while True:
    try:
        # initial
        ser.write('\n'.encode('utf8'))
        time.sleep(1)
        ser.read_all()

        # list interfaces status, find ADM ports
        ser.read_all()
        ser.write('dis int brief\n'.encode('utf8'))
        time.sleep(1)
        data = str(ser.read_all(), encoding='utf8')
        print(data)
        data = data.split('\n')

        ports = []
        for item in data:
            if item.find(r'ADM') != -1:
                port = item.split(r' ')[0]
                if port.find(r'GE') != -1:
                    ports.append(port)

        # handle ADM ports
        if len(ports) != 0:
            ser.read_all()
            ser.write('sys\n'.encode('utf8'))
            time.sleep(1)
            print(str(ser.read_all(), encoding='utf8'))

            for port in ports:
                ser.read_all()
                ser.write(('int ' + port + '\nundo shutdown\n').encode('utf8'))
                ser.write('quit\n'.encode('utf8'))
                time.sleep(1)
                print(str(ser.read_all(), encoding='utf8'))

            ser.write('quit\n'.encode('utf8'))
            time.sleep(1)
            print(str(ser.read_all(), encoding='utf8'))

        # find ports not in vlan 2002
        ports = []
        ser.read_all()
        ser.write('dis vlan 2002\n'.encode('utf8'))
        time.sleep(1)
        data = str(ser.read_all(), encoding='utf8')
        print(data)
        data = data.split(r'Untagged ports:')[-1]
        for port_num in [2, 3, 4, 5]:
            if data.find(r'GigabitEthernet1/0/' + str(port_num)) == -1:
                ports.append(str(port_num))

        # handle vlan 2002 if necessary
        if len(ports) != 0:
            ser.read_all()
            ser.write('sys\n'.encode('utf8'))
            time.sleep(1)
            print(str(ser.read_all(), encoding='utf8'))

            ser.write('vlan 2002\n'.encode('utf8'))
            time.sleep(1)
            print(str(ser.read_all(), encoding='utf8'))
            for port in ports:
                ser.read_all()
                ser.write(('port GE1/0/' + port + '\n').encode('utf8'))
                ser.write('quit\n'.encode('utf8'))
                time.sleep(1)
                print(str(ser.read_all(), encoding='utf8'))

            ser.write('quit\n'.encode('utf8'))
            time.sleep(1)
            print(str(ser.read_all(), encoding='utf8'))

        # # whether user-isolation enable
        # ser.read_all()
        # ser.write('dis user-isolation statistics\n'.encode('utf8'))
        # time.sleep(1)
        # data = str(ser.read_all(), encoding='utf8')
        # print(data)
        # data = data.split('\r\r\n')
        # if int(data[1].split(r': ')[1]) > 0:
        #     ser.read_all()
        #     ser.write('sys\n'.encode('utf8'))
        #     time.sleep(1)
        #     print(str(ser.read_all(), encoding='utf8'))
        #     ser.write('undo user-isolation vlan 2001 enable\nundo user-isolation vlan 2002 enable\n'.encode('utf8'))
        #     time.sleep(1)
        #     print(str(ser.read_all(), encoding='utf8'))
        #     ser.write('quit\n'.encode('utf8'))
        #     time.sleep(1)
        #     print(str(ser.read_all(), encoding='utf8'))

    except:
        pass
    print('')
    print(time.asctime( time.localtime(time.time()) ))
    print('')
    time.sleep(600)
