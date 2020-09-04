# -*- coding: utf-8 -*- 
import sdg_conn
import time
SDG1 = "107.239.97.194"
SDG2 = "107.239.97.202"

print("Verify SRd state Standby (Warned) by triggering redundancy events specified under WARNEV policy  on standby SDG")
#############Connecting to SDG################
print("Connecting to SDG...")
sdg_conn.conn_open(SDG1, "pv111p", "pv111p")
sdg_conn.redundancy_status()
print ("#######Waiting for Mastership#######")
local_peer_status = sdg_conn.mastership()
print local_peer_status
if local_peer_status == "MASTER":
    print ("Executing Test Case since SDG1 is the Master")
###################EXECUTING SDG1 LOGS####################
    sdg_conn.sys_core_dumps()################System Core Dumps########################
    sdg_conn.clear_svc("traffic-load-balance statistics")############clear traffic-load-balance statistics###########
    sdg_conn.clear_svc("sessions")############clear services sessions###########
    #sdg_conn.instance_stats("INTERNET") ##############INTERNET Summary Statistics##########
    #sdg_conn.virtual_service("406-DEF-HTTP") ##############406-DEF-HTTP Summary Statistics##########
    sdg_conn.d_port_logs("21")####################Traffic Flow for port 21#########################
    sdg_conn.d_port_logs("80")####################Traffic Flow for port 80#########################
    sdg_conn.d_port_logs("53")####################Traffic Flow for port 53#########################
    sdg_conn.show_conf("interfaces ae62 statistics") #############interfaces ae62 statistics###############   
    sdg_conn.show_conf("bgp summary") #############bgp summary###############
    sdg_conn.show_conf("vrrp summary") #############vrrp summary###############
    sdg_conn.svc_summary("nat mappings") #############NAT Mappings Summary###############
    sdg_conn.show_conf("services nat mappings detail") #############NAT Mappings Summary###############
    sdg_conn.config_change("set interfaces ae62 disable") ############Disabling interface ae62#########
    sdg_conn.redundancy_status() ###########Redundancy Status###############
    sdg_conn.sys_core_dumps()###########System Core Dumps###############
    sdg_conn.clear_svc("traffic-load-balance statistics")############clear traffic-load-balance statistics###########
    sdg_conn.clear_svc("sessions")############clear services sessions###########
    #sdg_conn.instance_stats("INTERNET") ##############INTERNET Summary Statistics##########
    #sdg_conn.virtual_service("406-DEF-HTTP") ##############406-DEF-HTTP Summary Statistics##########
    sdg_conn.d_port_logs("21")####################Traffic Flow for port 21#########################
    sdg_conn.d_port_logs("80")####################Traffic Flow for port 80#########################
    sdg_conn.d_port_logs("53")####################Traffic Flow for port 53#########################
    sdg_conn.show_conf("interfaces ae62 statistics") #############interfaces ae62 statistics###############   
    sdg_conn.show_conf("bgp summary") #############bgp summary###############
    sdg_conn.show_conf("vrrp summary") #############vrrp summary###############
    sdg_conn.svc_summary("nat mappings") #############NAT Mappings Summary###############
    sdg_conn.show_conf("services nat mappings detail") #############NAT Mappings Summary###############
    time.sleep(60)
    sdg_conn.config_change("delete interfaces ae62 disable") ############Enabling interface ae62#########
    sdg_conn.redundancy_status() ###########Redundancy Status###############
    time.sleep(5)
    sdg_conn.redundancy_status() ###########Redundancy Status###############
    sdg_conn.redundancy_set("ACQU_MSHIP_MANUAL_EV") ###########Membership Change############
    sdg_conn.redundancy_status() ###########Redundancy Status###############
    sdg_conn.sys_core_dumps()
    sdg_conn.clear_svc("traffic-load-balance statistics")############clear traffic-load-balance statistics###########
    sdg_conn.clear_svc("sessions")############clear services sessions###########
    #sdg_conn.instance_stats("INTERNET") ##############INTERNET Summary Statistics##########
    #sdg_conn.virtual_service("406-DEF-HTTP") ##############406-DEF-HTTP Summary Statistics##########
    sdg_conn.d_port_logs("21")####################Traffic Flow for port 21#########################
    sdg_conn.d_port_logs("80")####################Traffic Flow for port 80#########################
    sdg_conn.d_port_logs("53")####################Traffic Flow for port 53#########################
    sdg_conn.show_conf("interfaces ae62 statistics") #############interfaces ae62 statistics###############
    sdg_conn.show_conf("bgp summary") #############bgp summary###############
    sdg_conn.show_conf("vrrp summary") #############vrrp summary###############
    sdg_conn.svc_summary("nat mappings") #############NAT Mappings Summary###############
    sdg_conn.show_conf("services nat mappings detail") #############NAT Mappings Summary###############
    sdg_conn.conn_close()

        




