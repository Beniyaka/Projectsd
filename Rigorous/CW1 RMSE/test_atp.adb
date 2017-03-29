
-- Author:              A. Ireland
--
-- Address:             School Mathematical & Computer Sciences
--                      Heriot-Watt University
--                      Edinburgh, EH14 4AS
--
-- E-mail:              a.ireland@hw.ac.uk
--
-- Last modified:       13/10/2002
--
-- Filename:            test_atp.adb
--
-- Description:         Test harness for the ATP controller. Note that test data and
--                      results are managed via the Env and Log packages respectively.

with Env, Log, ATP;
procedure Test_ATP is
begin
   Env.Open_File;
   Log.Open_File;
   loop
      exit when Env.At_End;
      Env.Update;
      Log.Update;
      ATP.Control;
      Log.Update;
   end loop;
   Env.Close_File;
   Log.Close_File;
end Test_ATP;



