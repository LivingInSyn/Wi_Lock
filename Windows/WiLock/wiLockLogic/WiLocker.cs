using System;
using System.Collections.Generic;
using System.Configuration;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace WiLock.wiLockLogic
{
    public class WiLocker
    {
        int trust_time = 0;
        int no_trust_time = 0;
        string[] trusted_networks = null;
        bool trust_condition;

        public WiLocker()
        {
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
        }

        //NOW ADD RUN METHOD

        //ADD UPDATE SETTINGS METHOD

        //ADD SET METHOD for the times
    }
}
