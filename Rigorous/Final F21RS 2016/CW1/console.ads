
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
-- Filename:            reset.adb
--
-- Description:         Models the console associated with the ATP system, i.e. 
--                      the reset mechanism that is required to disable the 
--                      trains's braking system, as well as a SPAD count. 

package  Console
  --# own Reset_Status, SPAD_Cnt;
  --# initializes Reset_Status, SPAD_Cnt;
is
--   Reset_Status: Boolean:= False;
--   SPAD_Cnt: Integer:= 0;
   
   procedure Enable_Reset;
      --# global out Reset_Status;
      --# derives Reset_Status from ; 

   procedure Disable_Reset;
     --# global out Reset_Status;
     --# derives Reset_Status from ;  

   function Reset_Enabled return Boolean;
     --# global in Reset_Status;  
   
   procedure Inc_SPAD_Cnt;
     --# global in out SPAD_Cnt;
     --# derives SPAD_Cnt from SPAD_Cnt;
   
   procedure Reset_SPAD_Cnt;
      --# global out SPAD_Cnt;
      --# derives SPAD_Cnt from ;
   
   function SPAD_Cnt_Value return Integer;
   --# global in SPAD_Cnt;  

end Console;



