######################################################
###                                                ###
### M410 ch1.py V0.1                               ###
### For operating Modbus to Serial Adapter         ###
###                                                ###
### Created By Simon Maselli                       ###
### 24 July 2017                                   ###
###                                                ###
### Copyright Minnovation 2017                     ###
######################################################

from uModBus.serial import Serial
from uModBus.tcp import TCP

import machine, time, ustruct

def getData(P1,P2):
    
    uart_id = 0x01
    modbus_obj = Serial(uart_id, pins=(P1,P2))

    slave_addr=2              ################ EDIT TO SUIT APPLICATION - Supplied by Device Docs
	starting_address=62594    ################ EDIT TO SUIT APPLICATION - Supplied by Device Docs
    register_quantity=1       ################ EDIT TO SUIT APPLICATION - Supplied by Device Docs
	signed=True               ################ EDIT TO SUIT APPLICATION - Supplied by Device Docs
    
    result=''

    for y in range(0,2):
        try:
            register_value = modbus_obj.read_holding_registers(slave_addr, starting_address, register_quantity, signed)
            result = ustruct.unpack('>f', register_value)
        except Exception as e:
            print('Waking up Slave')
            pass
    try:
        return(result[0])
    except:
        return

#while True:    #### UNHASH FOR TESTING
    #print(getData())    ###UNHASH FOR TESTING
