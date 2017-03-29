
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
-- Filename:            brakes.ads
--
-- Description:         Models the train braking subsystem associated
--                      with the ATP controller.

package Brakes
   --# own State;
   --# initializes State;
is
   procedure Activate;
   --# global out State;
   --# derives State from ;

   procedure Deactivate;
   --# global out State;
   --# derives State from ;

   function Activated return Boolean;
   --# global in State;

end Brakes;



