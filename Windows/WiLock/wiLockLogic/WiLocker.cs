using System;
using System.Collections.Generic;
using System.Collections.ObjectModel;
using System.Configuration;
using System.Linq;
using System.Text;
using System.Threading;
using System.Threading.Tasks;
using WiLock.LockingClass;
using WiLock.WifiClasses;

namespace WiLock.wiLockLogic
{
    public class WiLocker
    {
        int trust_time = 0;
        int no_trust_time = 0;
        string[] trusted_networks = null;
        bool trust_condition;
        bool runApp;
        wifi_status Status;
        MachineLocker locker;

        public WiLocker()
        {
            Status = new wifi_status();
            locker = new MachineLocker();

            try
            {
                var networks_string = ConfigurationManager.AppSettings["TrustedNetworks"];
                trusted_networks = networks_string.Split(',');
            }
            catch (Exception e)
            {
                Console.WriteLine("Error in the Trusted networks config");
                //Environment.Exit(0);
            }
            //the no Trust time
            try
            {
                no_trust_time = int.Parse(ConfigurationManager.AppSettings["NoTrustTime"]);
            }
            catch (Exception e)
            {
                Console.WriteLine("Error in the No Trust Time setting, is it an Int?");
                //Environment.Exit(0);
            }
            try
            {
                trust_time = int.Parse(ConfigurationManager.AppSettings["TrustedTime"]);
            }
            catch (Exception e)
            {
                Console.WriteLine("Error in the Trusted Time setting, is it an Int?");
                //Environment.Exit(0);
            }

            trust_condition = false;

            runApp = true;
        }

        //NOW ADD RUN METHOD
        public void run()
        {
            while (runApp)
            {
                Collection<string> ssids = Status.GetSSIDs();

                trust_condition = false;

                uint idle = GetLastUserInput.GetIdleTickCount();

                //WE NEED TO FIND A WAY TO CHECK FOR AIRPLANE MODE!

                foreach (string ssid in ssids)
                {

                    foreach (string network in trusted_networks)
                    {
                        //Console.WriteLine(network);
                        //this if checks to see if the current ssid is in the list of trusted networks
                        //if it is, makes trust_condition true
                        if (Array.IndexOf(trusted_networks, ssid) > -1)
                        {
                            trust_condition = true;
                        }
                    }

                    //now, if trust condition != true, and if it's been more than 5 minutes, lock the machine
                    //we need to move idle to the app.config as well, 300000 is 5 minutes
                    if (trust_condition == false && idle > no_trust_time)
                    {
                        locker.LockMachine();
                    }
                    else if (trust_time != 0)
                    {
                        if (idle > trust_time)
                        {
                            locker.LockMachine();
                        }
                    }


                }
                Thread.Sleep(1000);

            }
        }


        /// <summary>
        /// This function tells the run loop to run the logic or not
        /// </summary>
        /// <param name="active">true allows the logic to run, false makes it stop</param>
        public void activate(bool active)
        {
            runApp = active;
        }
        
        //ADD UPDATE SETTINGS METHOD

        /// <summary>
        /// Change the trust and no trust times, also changes the config file
        /// </summary>
        /// <param name="trust">the trust time</param>
        /// <param name="noTrust">the no trust time</param>
        public void setTimes(int trust, int noTrust)
        {
            trust_time = trust;
            no_trust_time = noTrust;
            ConfigurationManager.AppSettings["TrustedTime"] = trust.ToString();
            ConfigurationManager.AppSettings["NoTrustTime"] = noTrust.ToString();
        }


    }
}
