import sdg_conn
import sys
import time
SDG1 = "" ############ENTER SDG1 IP#############
SDG2 = ""################Enter SGD2 IP##############

print("Verify SNMP Traps Getting generated when Service-PIC UP or Down")
#############Connecting to SDG################
print("Connecting to SDG...")
sdg_conn.conn_open(SDG1, UNAME, PWD)#################Enter UNAME and PWD#############

sdg_conn.redundancy_status()
print ("#######Waiting for Mastership#######")
local_peer_status = sdg_conn.mastership()
print local_peer_status
if local_peer_status == "MASTER":
###################EXECUTING SDG1 LOGS When SDG1 is Master and SDG2 as Standby ####################
    sdg_conn.sys_core_dumps()################System Core Dumps########################
    sdg_conn.redundancy_status()
    sdg_conn.clr_fw_fltr("IPF6-FBF-IMS-SOS")################Clearing IPF6-FBF-IMS-SOS stats###############
    sdg_conn.clr_fw_fltr("ae62.3202-i")###############Clearing ae62.3202-i###############
    sdg_conn.fw_fltr_stats("ae62.3202-i") #############firewall filter ae62.3202-i###############
    sdg_conn.fw_fltr_stats("IPF6-FBF-IMS-SOS") #############firewall filter ae62.3202-i###############
    time.sleep(10)
    ##################Releasing the Mastership to SDG2 from SDG1 Manually########################
    sdg_conn.redundancy_set("RELS_MSHIP_MANUAL_EV")

    sdg_conn.redundancy_status()
    time.sleep(10)
    sdg_conn.sys_core_dumps()################System Core Dumps########################
    sdg_conn.clr_fw_fltr("IPF6-FBF-IMS-SOS")################Clearing IPF6-FBF-IMS-SOS stats###############
    sdg_conn.clr_fw_fltr("ae62.3202-i")###############Clearing ae62.3202-i###############
    sdg_conn.fw_fltr_stats("ae62.3202-i") #############firewall filter ae62.3202-i###############
    sdg_conn.fw_fltr_stats("IPF6-FBF-IMS-SOS") #############firewall filter ae62.3202-i###############
    time.sleep(10)

##################Acquiring the Mastership frpm SDG2 to SDG1 Manually########################
    sdg_conn.redundancy_set("ACQU_MSHIP_MANUAL_EV")

    sdg_conn.redundancy_status()
    sdg_conn.sys_core_dumps()################System Core Dumps########################
    sdg_conn.clr_fw_fltr("IPF6-FBF-IMS-SOS")################Clearing IPF6-FBF-IMS-SOS stats###############
    sdg_conn.clr_fw_fltr("ae62.3202-i")###############Clearing ae62.3202-i###############
    sdg_conn.fw_fltr_stats("ae62.3202-i") #############firewall filter ae62.3202-i###############
    sdg_conn.fw_fltr_stats("IPF6-FBF-IMS-SOS") #############firewall filter ae62.3202-i###############
    sdg_conn.redundancy_status()

    sdg_conn.conn_close()





