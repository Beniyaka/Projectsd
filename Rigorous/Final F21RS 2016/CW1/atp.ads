--# inherit Sensors, Alarm, Brakes, Speedo, Console;
package ATP
	--# own Train_Speed_Temp_Memory;
	--# initializes Train_Speed_Temp_Memory;
is
	procedure Control;
	--# global in Sensors.State;
	--#	in out Brakes.State;
	--#	in out Alarm.State;
	--#	in Speedo.Speed;
	--#	in out Train_Speed_Temp_Memory;
	--#	in out Console.SPAD_Cnt;
	--# derives Alarm.State from Sensors.State, Alarm.State, Brakes.State &
	--#	Brakes.State from Sensors.State, Train_Speed_Temp_Memory, Speedo.Speed, Brakes.State, Alarm.State &
	--#	Train_Speed_Temp_Memory from Speedo.Speed &
	--#	Console.SPAD_Cnt from Console.SPAD_Cnt, Sensors.State, Brakes.State;
end ATP;
