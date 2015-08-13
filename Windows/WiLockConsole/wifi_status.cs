using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using NativeWifi;
using System.Collections.ObjectModel;

namespace WiLockConsole
{
    public class wifi_status
    {
        WlanClient wlan;
        public wifi_status()
        {
            wlan = new WlanClient();
        }

        public Collection<String> GetSSIDs()
        {
            //get the ssids
            Collection<string> connectedSSIDs = new Collection<string>();
            
            foreach (WlanClient.WlanInterface wlanInterface in wlan.Interfaces)
            {
                try
                { 
                    string state = wlanInterface.InterfaceState.ToString();
                    if (state == "Connected")
                    { 
                        Wlan.Dot11Ssid ssid = wlanInterface.CurrentConnection.wlanAssociationAttributes.dot11Ssid;
                        connectedSSIDs.Add(new String(Encoding.ASCII.GetChars(ssid.SSID, 0, (int)ssid.SSIDLength)));
                              
                    }
                }
                catch (Exception e)
                {
                    Console.WriteLine(e.Message);
                }
            }
            return connectedSSIDs;
        }
    }
}
