
-- Author:              A. Ireland
--
-- Address:             School Mathematical & Computer Sciences
--                      Heriot-Watt University
--                      Edinburgh, EH14 4AS
--
-- E-mail:              a.ireland@hw.ac.uk
--
-- Last modified:       25/9/2013 
--
-- Filename:            speedo.ads
--
-- Description:         Models the speedo device associated with the ATP system.

package Speedo
   --# own Speed;
   --# initializes Speed;
is

   subtype Speed_Type is Integer range 0..150;

   procedure Write_Speed(S: in Speed_Type);
   --# global out Speed;
   --# derives Speed from S;

   function Read_Speed return Speed_Type;
   --# global in Speed;

end Speedo;



