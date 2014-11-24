def getmac_new():
	RES = []
	from ctypes import Structure, windll, sizeof
	from ctypes import POINTER, byref
	from ctypes import c_ulong, c_uint, c_ubyte, c_char , c_wchar
	MAX_ADAPTER_DESCRIPTION_LENGTH = 128
	MAX_ADAPTER_NAME_LENGTH = 256
	MAX_ADAPTER_ADDRESS_LENGTH = 8
	MIB_IF_OPER_STATUS_OPERATIONAL = 5
	NO_ERROR = 0
	ERROR_BUFFER_OVERFLOW = 111

	class IP_ADDR_STRING( Structure ):
		pass
	LP_IP_ADDR_STRING = POINTER( IP_ADDR_STRING )
	IP_ADDR_STRING._fields_ = [
		( "next", LP_IP_ADDR_STRING ),
		( "ipAddress", c_char * 16 ),
		( "ipMask", c_char * 16 ),
		( "context", c_ulong )]
	class IP_ADAPTER_INFO ( Structure ):
		pass
	LP_IP_ADAPTER_INFO = POINTER( IP_ADAPTER_INFO )
	IP_ADAPTER_INFO._fields_ = [
		( "next", LP_IP_ADAPTER_INFO ),
		( "comboIndex", c_ulong ),
		( "adapterName", c_char * ( MAX_ADAPTER_NAME_LENGTH + 4 ) ),
		( "description", c_char * ( MAX_ADAPTER_DESCRIPTION_LENGTH + 4 ) ),
		( "addressLength", c_uint ),
		( "address", c_ubyte * MAX_ADAPTER_ADDRESS_LENGTH ),
		( "index", c_ulong ),
		( "type", c_uint ),
		( "dhcpEnabled", c_uint ),
		( "currentIpAddress", LP_IP_ADDR_STRING ),
		( "ipAddressList", IP_ADDR_STRING ),
		( "gatewayList", IP_ADDR_STRING ),
		( "dhcpServer", IP_ADDR_STRING ),
		( "haveWins", c_uint ),
		( "primaryWinsServer", IP_ADDR_STRING ),
		( "secondaryWinsServer", IP_ADDR_STRING ),
		( "leaseObtained", c_ulong ),
		( "leaseExpires", c_ulong )]
	class MIB_IFROW ( Structure ):
		pass
	LP_MIB_IFROW = POINTER( MIB_IFROW )
	MIB_IFROW._fields_ = [
		( "wszName", c_wchar * 256 ),
		( "dwIndex", c_ulong ),
		( "dwType", c_ulong ),
		( "dwMtu", c_ulong ),
		( "dwSpeed", c_ulong ),
		( "dwPhysAddrLen", c_ulong ),
		( "bPhysAddr", c_ubyte * 8 ),
		( "dwAdminStatus", c_ulong ),
		( "dwOperStatus", c_ulong ),
		( "dwLastChange", c_ulong ),
		( "dwInOctets", c_ulong ),
		( "dwInNucastPkts", c_ulong ),
		( "dwInDiscards", c_ulong ),
		( "dwErrors", c_ulong ),
		( "dwInUnknownProtos", c_ulong ),
		( "dwOutOctets", c_ulong ),
		( "dwOutUcastPkts", c_ulong ),
		( "dwOutNUcastPkts", c_ulong ),
		( "dwOutErrors", c_ulong ),
		( "dwOutQLen", c_ulong ),
		( "dwDescrLen", c_ulong ),
		( "bDescr", c_ubyte * 256 ),
	]
	GetAdaptersInfo = windll.iphlpapi.GetAdaptersInfo
	GetAdaptersInfo.restype = c_ulong
	GetAdaptersInfo.argtypes = [LP_IP_ADAPTER_INFO, POINTER( c_ulong )]

	GetIfEntry = windll.iphlpapi.GetIfEntry
	GetIfEntry.restype = c_ulong
	GetIfEntry.argtypes = [LP_MIB_IFROW, ]

	addr = ""
	just_one_flag = True
	adapterList = ( IP_ADAPTER_INFO )()
	buflen = c_ulong( sizeof( adapterList ) )
	ret = GetAdaptersInfo( byref( adapterList ), byref( buflen ) )

	if ret == ERROR_BUFFER_OVERFLOW:
		just_one_flag = False
		lens = buflen.value / sizeof( adapterList )
		adapterList = ( IP_ADAPTER_INFO * lens )()
		ret = GetAdaptersInfo( byref( adapterList[0] ), byref( buflen ) )
	if ret == NO_ERROR and not just_one_flag:
		for adapter in adapterList:
			GatWay = None
			MibRow = MIB_IFROW()
			MibRow.dwIndex = adapter.index
			MibRow.dwType = adapter.type
			ret = GetIfEntry( byref( MibRow ) )
			if ret == NO_ERROR:
				GatWay = adapter.gatewayList.ipAddress
				if MibRow.dwOperStatus == MIB_IF_OPER_STATUS_OPERATIONAL and len( GatWay ) != 0:
					#addr = (MibRow.bPhysAddr[0], MibRow.bPhysAddr[1], MibRow.bPhysAddr[2], MibRow.bPhysAddr[3], MibRow.bPhysAddr[4], MibRow.bPhysAddr[5] )
					ST1 = ""
					for i in MibRow.bDescr:
						if i>=33:
							ST1 += chr(i)
					ST2 = ""
					for i in MibRow.wszName:
						ST2+= i
					RES.append([ST1,ST2])

	return RES
	
def GETMAC():
	import re
	ARR = getmac_new()
	for i in ARR:
		i[1] = re.sub("TCPIP_","NPF_",i[1])
	return ARR