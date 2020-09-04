from jnpr.junos import Device
from jnpr.junos.utils.config import Config
from lxml import etree
import time


def conn_open(node, uname, pwd):
    global dev
    dev = Device(host=node, user=uname, passwd=pwd, port=22).open()

    

def conn_close():
    dev.close()

def mastership():
    redundancy_info = dev.rpc.get_services_redundancy_group_information({'format': 'json'})
    return (str((redundancy_info)['rg-information'][0]['rg-state-information'][0]['services-rg-information'][0]['services-rg-rs-information'][0]['local-rs-state'][0]['data']))

def sys_core_dumps():
    ###########System Core Dumps###############
    print("##################System Core Dumps####################")
    system_core_dumps = dev.rpc.get_system_core_dumps({'format': 'text'})
    print(etree.tostring(system_core_dumps))

def fw_fltr_stats(filter):
    try:
        for i in range(0, 4):
            print("################" + filter + " Stats####################")
            config = dev.rpc.cli("show firewall filter " + filter, format='text')
            print(etree.tostring(config))
    except TypeError:
        print("Couldn't get any information regarding the Query!!!")

def clear_svc(svc):
    ############clear services###########
    print ("##################clear services " + svc + "###################")
    clear_svc_tlb = dev.rpc.cli("clear services " + svc, format='text')

def clr_fw_fltr(svc):
    ############clearing firewall services###########
    print ("##################clear firewall filter " + svc + "###################")
    clear_svc_tlb = dev.rpc.cli("clear firewall filter " + svc, format='text')

def instance_stats(instance):
    print ("##################" + instance + " summary###################")
    dev.rpc.cli("clear services traffic-load-balance statistics instance " + instance, format='text')
    for i in range(0, 4):
		traffic_loadbalance_statistics = dev.rpc.cli("show services traffic-load-balance statistics instance " + instance + " summary", format='text')
		print(etree.tostring(traffic_loadbalance_statistics))
		time.sleep(2)

def virtual_service(vs):
    print ("##################" + vs + " summary###################")
    dev.rpc.cli("clear services traffic-load-balance statistics virtual-service " + vs, format='text')
    for i in range(0, 4):
		virtual_service_statistics = dev.rpc.cli("show services traffic-load-balance statistics virtual-service " + vs, format='text')
		print(etree.tostring(virtual_service_statistics))
		time.sleep(2)

def show_conf(cmd):
    try:
        print("################" + cmd + " ####################")
        config = dev.rpc.cli("show " + cmd, format='text')
        return(etree.tostring(config))
    except TypeError:
        print("Couldn't get any information regarding the Query!!!")
#def show_conf(cmd):
#    print("################" + cmd + " ####################")
#    config = dev.rpc.cli("show " + cmd, format='text')
#    print(etree.tostring(config))

def svc_summary(cmd):
    print("################" + cmd + " Summary####################")
    summary = dev.rpc.cli("show services " + cmd + " summary", format='text')
    print(etree.tostring(summary))

def config_change(cmd):
    with Config(dev, mode='private') as cu:  
        cu.load(cmd, format='set')
        cu.pdiff()
        cu.commit()
        time.sleep(2)

def ping(context, ip):
    print("############Ping statistics for routing instance " + context + " : ##############")
    result = dev.rpc.ping(instance=context, host=ip, count='4')
    if result.find("ping-success") is not None:
        print ("%s is reachable" %ip)
    else:
        print ("%s is not reachable" %ip)


def RI_Summary(instance):
    print("############Routing Instance " + instance + " configuration Summary##############")
    config_summary = dev.cli("show configuration routing-instances " + instance +"|display set")
    print (config_summary)

    

def redundancy_status():
    redundancy_output = dev.rpc.get_services_redundancy_group_information({'format': 'text'})
    print("##########Redundancy Group Information############")
    print(etree.tostring(redundancy_output))

def redundancy_set(event):
    event_change = dev.rpc.request_services_redundancy_set(id = "1", redundancy_event = event, trigger=True)
    print("##########Changing Redundancy Event to: " + event +"############")
    print(etree.tostring(event_change))

def pic_slot_toggle(fpc_slot, pic_slot, online_offline):
    pic_toggle = dev.rpc.cli("request chassis pic fpc-slot " + fpc_slot + " pic-slot " + pic_slot +" " + online_offline)
    print(etree.tostring(pic_toggle))

def fpc_slot_toggle(fpc_slot, online_offline):
    pic_toggle = dev.rpc.cli("request chassis fpc slot " + fpc_slot +" " + online_offline)
    print(etree.tostring(pic_toggle))

def d_port_logs(port):
    print ("Displaying port "+port+ " logs")
    try:
        for i in range(0, 2):
            a = dev.rpc.cli("show services sessions destination-port " + port+" limit 10")
            print (etree.tostring(a))
    except TypeError:
        print("Traffic has Either stopped or Not Running")

def service_set(svc):
    try:
        for i in range(0, 4):
            a = dev.rpc.cli("show services sessions service-set " + svc)
            print (etree.tostring(a))
    except TypeError:
        print("Traffic has Either stopped or Not Running")


###############CCF Code#########################
def sfw_d_port(svc_set, dst_pfx):
    try:
        return("Displaying destination prefix "+dst_pfx+ " logs")
        for i in range(0, 2):
            a = dev.rpc.cli("show services sessions service-set "+svc_set+" destination-prefix "+dst_pfx+" limit 10")
            return(etree.tostring(a))
    except TypeError:
        return("Traffic has Either stopped or Not Running")

def show_route(cmd):
    prt1 = ("################" + cmd + " ####################")
    try:
        config = dev.rpc.cli("show route table " + cmd, format='text')
        prt2 = (etree.tostring(config))
        return prt1, prt2
    except TypeError:
        return("Couldn't get any information regarding the Query!!!")