with Sensors, Alarm, Brakes, Speedo, Console;
package body ATP
is
	--used within atp package only
	Train_Speed_Temp_Memory: Speedo.Speed_Type;

	procedure Control
	is
		Sensors_Value: Sensors.Sensor_Type;
	begin
		if not Brakes.Activated then
			Sensors_Value := Sensors.Read_Sensor_Majority;
			case Sensors_Value is
				when Sensors.Proceed =>
					if Alarm.Enabled then
						Alarm.Disable;
					end if;
				when Sensors.Caution =>
					if Alarm.Enabled then
						if Speedo.Read_Speed >= Train_Speed_Temp_Memory then
							Brakes.Activate;
						end if;
					end if;
					Alarm.Enable;
				when Sensors.Danger =>
					Brakes.Activate;
					Alarm.Enable;
					Console.Inc_SPAD_Cnt;
				when others =>
					Alarm.Enable;
			end case;
		else
			Alarm.Disable;
			Brakes.Deactivate;
		end if;

		Train_Speed_Temp_Memory := Speedo.Read_Speed;
	end Control;

begin
	Train_Speed_Temp_Memory := 0;
end ATP;
