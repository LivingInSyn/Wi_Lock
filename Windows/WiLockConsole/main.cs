using System;
using System.Collections.Generic;
using System.Collections.ObjectModel;
using System.Linq;
using System.Runtime.InteropServices;
using System.Text;
using System.Threading;
using System.Threading.Tasks;
using System.Configuration;

namespace WiLockConsole
{
    public class main
    {
        
        static void Main(string[] args)
        {
            //create the instances of classes we'll need
            wifi_status Status = new wifi_status();
            MachineLocker locker = new MachineLocker();

            //get the configs from the App.config file
            var networks_string = ConfigurationManager.AppSettings["TrustedNetworks"];
            string[] trusted_networks = networks_string.Split(',');

            //we'll look here to see if any of the networks are trusted
            bool trust_condition = false;


            while ( true )
            {
                Collection<string> ssids = Status.GetSSIDs();
                
                trust_condition = false;

                foreach (string ssid in ssids)
                {
                    //Console.WriteLine(ssid);
                    //I know this says idle TICK count, but it's ms, 1000 'ticks' to a second
                    uint idle = GetLastUserInput.GetIdleTickCount();
                    //Console.WriteLine(idle);

                    foreach (string network in trusted_networks)
                    {
                        //Console.WriteLine(network);
                        //this if checks to see if the current ssid is in the list of trusted networks
                        //if it is, makes trust_condition true
                        if (Array.IndexOf(trusted_networks, ssid) > -1 )
                        {
                            trust_condition = true;
                        }                        
                    }

                    //now, if trust condition != true, and if it's been more than 5 minutes, lock the machine
                    //we need to move idle to the app.config as well, 300000 is 5 minutes
                    if(trust_condition == false && idle > 300000)
                    {
                        locker.LockMachine();
                    }

                    Console.WriteLine("Currently Connected to: " + ssids);
                    Console.WriteLine("We've been idle for: " + idle);
                    Console.WriteLine("Trust Condition is: " + trust_condition);



                    
                }
                //Console.ReadLine();
                Thread.Sleep(1000);
                
            }
        }
    }
}
