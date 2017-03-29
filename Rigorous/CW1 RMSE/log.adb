
-- Author:              A. Ireland
--
-- Address:             School Mathematical & Computer Sciences
--                      Heriot-Watt University
--                      Edinburgh, EH14 4AS
--
-- E-mail:              a.ireland@hw.ac.uk
--
-- Last modified:       18/10/2002
--
-- Filename:            log.adb
--
-- Description:         Provides logger that records state information on the
--                      component parts of the ATP system at run-time.

with Text_IO, Sensors, Speedo, Alarm, Brakes, Console;
use type Sensors.Sensor_Type;
package body Log is

   package Sensor_INOUT is new Text_IO.Enumeration_IO(Sensors.Sensor_Type);
   -- use Sensor_INOUT;
   package Integer_INOUT is new Text_IO.Integer_IO(Integer);
   -- use Integer_INOUT;

   Log_File: Text_IO.File_Type;

   procedure Update is
   begin
      Sensor_INOUT.Put(Log_File, Sensors.Read_Sensor(1), 10);
      Sensor_INOUT.Put(Log_File, Sensors.Read_Sensor(2), 10);
      Sensor_INOUT.Put(Log_File, Sensors.Read_Sensor(3), 10);
      Sensor_INOUT.Put(Log_File, Sensors.Read_Sensor_Majority, 10);
      Integer_INOUT.Put(Log_File, Speedo.Read_Speed, 2);
      if Alarm.Enabled then
         Text_IO.Put(Log_File, "     ON   ");
      else
         Text_IO.Put(Log_File, "     --   ");
      end if;
      if Brakes.Activated then
         Text_IO.Put(Log_File, "  ON    ");
      else
         Text_IO.Put(Log_File, "  --    ");
      end if;
      if Console.Reset_Enabled then
         Text_IO.Put(Log_File, "  ON ");
      else
         Text_IO.Put(Log_File, "  -- ");
      end if;
      Integer_INOUT.Put(Log_File, Console.SPAD_Cnt_Value, 6);
      Text_IO.New_Line(Log_File);
   end Update;

   procedure Open_File is
   begin
      Text_IO.Create(Log_File, Text_IO.Out_File, "log.dat");
      Text_IO.Put_Line(Log_File,
               "SENSOR-1  SENSOR-2  SENSOR-3  MAJORITY  SPEED  ALARM  BRAKES  RESET  SPADs");
      Text_IO.Put_Line(Log_File,
               "--------  --------  --------  --------  -----  -----  ------  -----  -----");
   end Open_File;

   procedure Close_File is
   begin
      Text_IO.Close(Log_File);
   end Close_File;

end Log;



