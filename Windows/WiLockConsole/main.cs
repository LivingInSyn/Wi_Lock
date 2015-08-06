using System;
using System.Collections.Generic;
using System.Collections.ObjectModel;
using System.Linq;
using System.Runtime.InteropServices;
using System.Text;
using System.Threading;
using System.Threading.Tasks;

namespace WiLockConsole
{
    public class main
    {
        
        static void Main(string[] args)
        {
            wifi_status Status = new wifi_status();
            while ( true )
            {
                Collection<string> ssids = Status.GetSSIDs();
                foreach (string ssid in ssids)
                {
                    Console.WriteLine(ssid);
                    uint test = GetLastUserInput.GetLastInputTime();
                    Console.WriteLine(test);

                }
                //Console.ReadLine();
                Thread.Sleep(1000);
                
            }
        }
    }
}
