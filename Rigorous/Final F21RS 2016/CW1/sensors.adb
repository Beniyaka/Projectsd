package body Sensors
--# own State is AStack;
is
	--state is hidden and is comprised of an array and a pointer
	type Vector is array(Sensor_Index_Type) of Sensor_Type;
	type Stack is
		record
			Data: Vector;
			Pointer: Sensor_Index_Type;
		end record;
	AStack: Stack;


	procedure Write_Sensors(Value_1, Value_2, Value_3: in Sensor_Type)
	--# global in out AStack;
	--# derives AStack from Value_1, Value_2, Value_3, AStack;
	is
	begin
		AStack.Pointer := 1;
		AStack.Data(AStack.Pointer) := Value_1;
		AStack.Pointer := AStack.Pointer + 1;
		AStack.Data(AStack.Pointer) := Value_2;
		AStack.Pointer := AStack.Pointer + 1;
		AStack.Data(AStack.Pointer) := Value_3;
	end Write_Sensors;

	function Read_Sensor(Sensor_Index: in Sensor_Index_Type) return Sensor_Type
	--# global in AStack;
	is
	begin
		return AStack.Data(Sensor_Index);
	end Read_Sensor;

	function Read_Sensor_Majority return Sensor_Type
	--# global in AStack;
	--# return AResult => ((AStack.Data(1) /= AStack.Data(2) and AStack.Data(1) /= AStack.Data(3) and AStack.Data(2) /= AStack.Data(3)) -> AResult = Undef) and
	--# (AStack.Data(1) = AStack.Data(2) -> AResult = AStack.Data(1)) and
	--# (AStack.Data(1) = AStack.Data(3) -> AResult = AStack.Data(1)) and
	--# (AStack.Data(2) = AStack.Data(3) -> AResult = AStack.Data(2));
	is
		AResult: Sensor_Type;
	begin
		AResult := Undef;
		if AStack.Data(1) /= AStack.Data(2) AND AStack.Data(1) /= AStack.Data(3) AND AStack.Data(2) /= AStack.Data(3) then
			AResult := Undef;
		else
			if AStack.Data(1) = AStack.Data(2) then
				AResult := AStack.Data(1);
			elsif AStack.Data(1) = AStack.Data(3) then
				AResult := AStack.Data(1);
			elsif AStack.Data(2) = AStack.Data(3) then
				AResult := AStack.Data(2);
			end if;
		end if;

		return AResult;
	end Read_Sensor_Majority;

begin
	--simultaneous assignment using aggregate construct
	AStack.Data := Vector'(Sensor_Index_Type => Undef);
	AStack.Pointer := 1;
end Sensors;
