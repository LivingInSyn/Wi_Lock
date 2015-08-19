using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Controls.Primitives;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Imaging;
using System.Windows.Navigation;
using System.Windows.Shapes;
using MahApps.Metro.Controls;
using WiLock.GuiHelpers;
using System.ComponentModel;
using WiLock.wiLockLogic;

namespace WiLock
{
    /// <summary>
    /// Interaction logic for MainWindow.xaml
    /// </summary>
    public partial class MainWindow : MetroWindow
    {
        public MainWindow()
        {
            InitializeComponent();

            MinimizeToTray.Enable(this);
            //create an instance of the WiLocker class which is the business logic
            WiLocker locker = new WiLocker();
        }

        //this handles the slider for if it's on or off
        private void echoChecked(object sender, RoutedEventArgs e)
        {
            Debug.WriteLine("Clicked");
            if ((sender as ToggleSwitch).IsChecked ?? false)
            {
                // Code for Checked state
                Debug.WriteLine("checked click");
            }
            else
            {
                Debug.WriteLine("not checked");
            }
        }

        //handles the Apply button
        private void clickApply(object sender, RoutedEventArgs e)
        {
            Debug.WriteLine("Apply Clicked");
            //get the text from the text boxes

        }

        //handles the cancel button
        private void clickCancel(object sender, RoutedEventArgs e)
        {
            Debug.WriteLine("Cancel Clicked");
            this.Close();
        }


        //This handles the behavior when we click the X on the window
        //we overrode this so that it would minimize to the tray
        protected override void OnClosing(CancelEventArgs e)
        {
            //trying to catch a thing here
            Debug.WriteLine("caught");
            e.Cancel = true;
            this.WindowState = WindowState.Minimized;
        }
    }
}
