import sdg_conn
import sys
import time
SDG1 = ""#############SGD1 IP###############
SDG2 = ""#############SDG2 IP###########

print ("Verify SNMP Traps Getting generated when Service-PIC UP or Down")
#############Connecting to SDG################
print("Connecting to SDG...")
sdg_conn.conn_open(SDG2, UNAME, PWD)###############ENter UNAME AND PWD#################
sdg_conn.redundancy_status()
print ("#######Waiting for Mastership#######")
local_peer_status = sdg_conn.mastership()
print local_peer_status
###################EXECUTING SDG2 LOGS When SDG1 is Master and SDG2 as Standby ####################
sdg_conn.sys_core_dumps()################System Core Dumps########################
sdg_conn.redundancy_status()
sdg_conn.clr_fw_fltr("IPF6-FBF-IMS-SOS")################Clearing IPF6-FBF-IMS-SOS stats###############
sdg_conn.clr_fw_fltr("ae62.3202-i")###############Clearing ae62.3202-i###############
sdg_conn.fw_fltr_stats("ae62.3202-i") #############firewall filter ae62.3202-i###############
sdg_conn.fw_fltr_stats("IPF6-FBF-IMS-SOS") #############firewall filter ae62.3202-i###############
while local_peer_status != "MASTER":
    local_peer_status = sdg_conn.mastership()
    print("\r Waiting for SDG2 to become Master..."),
    sys.stdout.flush()
    time.sleep(2)

###################EXECUTING SDG2 LOGS When SDG2 is Master and SDG1 as Standby ####################
sdg_conn.sys_core_dumps()################System Core Dumps########################
sdg_conn.redundancy_status()
sdg_conn.clr_fw_fltr("IPF6-FBF-IMS-SOS")################Clearing IPF6-FBF-IMS-SOS stats###############
sdg_conn.clr_fw_fltr("ae62.3202-i")###############Clearing ae62.3202-i###############
sdg_conn.fw_fltr_stats("ae62.3202-i") #############firewall filter ae62.3202-i###############
sdg_conn.fw_fltr_stats("IPF6-FBF-IMS-SOS") #############firewall filter ae62.3202-i###############

while local_peer_status != "STANDBY":
    local_peer_status = sdg_conn.mastership()
    print("\r Waiting for SDG1 to become Master and SDG2 to become standby..."),
    sys.stdout.flush()
    time.sleep(2)

###################EXECUTING SDG2 LOGS When SDG1 is Master and SDG2 as Standby ####################
sdg_conn.sys_core_dumps()################System Core Dumps########################
sdg_conn.redundancy_status()
sdg_conn.clr_fw_fltr("IPF6-FBF-IMS-SOS")################Clearing IPF6-FBF-IMS-SOS stats###############
sdg_conn.clr_fw_fltr("ae62.3202-i")###############Clearing ae62.3202-i###############
sdg_conn.fw_fltr_stats("ae62.3202-i") #############firewall filter ae62.3202-i###############
sdg_conn.fw_fltr_stats("IPF6-FBF-IMS-SOS") #############firewall filter ae62.3202-i###############
sdg_conn.redundancy_status()

sdg_conn.conn_close()