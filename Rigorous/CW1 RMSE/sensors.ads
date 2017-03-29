
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
-- Filename:            sensors.ads
--
-- Description:         Models the 3 sensors associated with the ATP system. Note that
--                      a single sensor reading is calculated using a majority vote
--                      algorithm.

package Sensors
   --# own State;
   --# initializes State;
is
   type Sensor_Type is (Proceed, Caution, Danger, Undef);
   subtype Sensor_Index_Type is Integer range 1..3;

   procedure Write_Sensors(Value_1, Value_2, Value_3: in Sensor_Type);
   --# global out State;
   --# derives State from Value_1, Value_2, Value_3;

   function Read_Sensor(Sensor_Index: in Sensor_Index_Type) return Sensor_Type;
   --# global in State;

   function Read_Sensor_Majority return Sensor_Type;
   --# global in State;

end Sensors;




