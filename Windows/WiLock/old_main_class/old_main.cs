using System;
using System.Collections.Generic;
using System.Collections.ObjectModel;
using System.Linq;
using System.Runtime.InteropServices;
using System.Text;
using System.Threading;
using System.Threading.Tasks;
using System.Configuration;
using WiLock.LockingClass;
using WiLock.WifiClasses;

namespace WiLockConsole
{
    /*public class main
    {
        


        static void Main(string[] args)
        {
            //create the instances of classes we'll need
            wifi_status Status = new wifi_status();
            MachineLocker locker = new MachineLocker();

            int trust_time = 0;
            int no_trust_time = 0;
            string[] trusted_networks = null;

            //get the configs from the App.config file
            //the trusted networks...
            try
            {
                var networks_string = ConfigurationManager.AppSettings["TrustedNetworks"];
                trusted_networks = networks_string.Split(',');
            }
            catch (Exception e)
            {
                Console.WriteLine("Error in the Trusted networks config");
                Environment.Exit(0);
            }
            //the no Trust time
            try
            { 
                no_trust_time = int.Parse(ConfigurationManager.AppSettings["NoTrustTime"]);
            }
            catch (Exception e)
            {
                Console.WriteLine("Error in the No Trust Time setting, is it an Int?");
                Environment.Exit(0);
            }
            try
            {
                trust_time = int.Parse(ConfigurationManager.AppSettings["TrustedTime"]);
            }
            catch (Exception e)
            {
                Console.WriteLine("Error in the Trusted Time setting, is it an Int?");
                Environment.Exit(0);
            }


            //we'll look here to see if any of the networks are trusted
            bool trust_condition = false;


            while ( true )
            {
                Collection<string> ssids = Status.GetSSIDs();
                
                trust_condition = false;

                //I know this says idle TICK count, but it's ms, 1000 'ticks' to a second
                uint idle = GetLastUserInput.GetIdleTickCount();

                foreach (string ssid in ssids)
                {
                    
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
                    if(trust_condition == false && idle > no_trust_time)
                    {
                        locker.LockMachine();
                    }
                    else if (trust_time != 0)
                    {
                        if(idle > trust_time)
                        {
                            locker.LockMachine();
                        }
                    }

                                        
                }
                Console.WriteLine("Currently Connected to: " + ssids);
                Console.WriteLine("We've been idle for: " + idle);
                Console.WriteLine("Trust Condition is: " + trust_condition);
                Thread.Sleep(1000);
                
            }
        }
    }*/
}
