
-- Author:              A. Ireland
--
-- Address:             School Mathematical & Computer Sciences
--                      Heriot-Watt University
--                      Edinburgh, EH14 4AS
--
-- E-mail:              a.ireland@hw.ac.uk
--
-- Last modified:       1/9/2016 
--
-- Filename:            alarm.ads
--
-- Description:         Models the alarm device associated
--                      with the ATP controller.


package Alarm
   --# own State;
   --# initializes State;
is
   procedure Enable;
   --# global out State;
   --# derives State from ;

   procedure Disable;
   --# global out State;
   --# derives State from ;

   function Enabled return Boolean;
   --# global in State;

end Alarm;



